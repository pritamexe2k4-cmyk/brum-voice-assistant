"""
LiveKit Voice AI Agent with Multi-Agent RAG System
==================================================

Architecture:
    Voice Input → STT → Multi-Agent System → TTS → Voice Output
"""

import contextlib
import logging
import signal
import threading
from pathlib import Path

from dotenv import load_dotenv

from livekit.agents import (
    NOT_GIVEN,
    Agent,
    AgentFalseInterruptionEvent,
    AgentSession,
    AgentServer,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    RunContext,
    cli,
)

from livekit.agents import metrics as lk_metrics
from livekit.agents.llm import function_tool

from livekit.plugins import (
    cartesia,
    deepgram,
    langchain,
    noise_cancellation,
    silero,
)

from livekit.plugins.turn_detector.multilingual import MultilingualModel

from metrics_logger import get_metrics_logger
from multi_agent_rag import graph


# ============================================================
# WINDOWS SIGNAL HANDLING FIX
# ============================================================

try:
    import livekit.agents.ipc.supervised_proc as sp

    @contextlib.contextmanager
    def _safe_mask_ctrl_c():
        """Safe SIGINT masking that only runs in main thread."""

        if threading.current_thread() is threading.main_thread():
            old = signal.signal(signal.SIGINT, signal.SIG_IGN)

            try:
                yield
            finally:
                signal.signal(signal.SIGINT, old)
        else:
            yield

    sp._mask_ctrl_c = _safe_mask_ctrl_c

except (ImportError, AttributeError):
    pass


# ============================================================
# LOGGING
# ============================================================

logger = logging.getLogger("agent")


# ============================================================
# LIVEKIT AGENT SERVER
# ============================================================

server = AgentServer()


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

_REPO_ROOT = Path(__file__).resolve().parents[1]

for _env_name in (".env.local", ".env"):
    _env_path = _REPO_ROOT / _env_name

    if _env_path.exists():
        load_dotenv(_env_path)
        break


# ============================================================
# ASSISTANT
# ============================================================

class Assistant(Agent):
    """
    Voice AI Assistant with Multi-Agent RAG capabilities.
    """

    def __init__(self) -> None:

        super().__init__(
            instructions="""
You are a friendly, helpful voice assistant for Soffotech.

What you can help with:
- Knowledge base: AI/ML, climate change, modern history,
  blockchain, health and wellness.
- Real-time information: weather, currency exchange rates,
  and current time in timezones.

How to speak:
- Sound natural and human.
- Keep responses short by default, usually 1-3 sentences.
- If the user greets you or asks who you are, introduce yourself
  briefly as the Soffotech voice assistant.
- Do not mention internal tools, function calls, or system steps.
- Avoid emojis, markdown, headings, and bullet-heavy formatting.
"""
        )

    @function_tool
    async def sample_function(
        self,
        context: RunContext,
        param: str,
    ):
        """
        Sample function tool.
        """

        logger.info(f"Sample function called with: {param}")

        return "Sample function response"


# ============================================================
# PREWARM
# ============================================================

def prewarm(proc: JobProcess):
    """
    Pre-load heavy models and initialize systems.
    """

    logger.info("Starting pre-warm sequence...")


    # --------------------------------------------------------
    # METRICS LOGGER
    # --------------------------------------------------------

    metrics = get_metrics_logger(
        log_file="metrics/agent_metrics.json"
    )

    proc.userdata["metrics"] = metrics

    logger.info("Metrics logger initialized")


    # --------------------------------------------------------
    # LOAD VAD
    # --------------------------------------------------------

    logger.info("Loading VAD model...")

    proc.userdata["vad"] = silero.VAD.load()


    # --------------------------------------------------------
    # PRE-WARM RAG
    # --------------------------------------------------------

    logger.info("Pre-warming RAG system...")

    try:

        from rag_system import get_rag_system

        get_rag_system()

        proc.userdata["rag_ready"] = True

        logger.info(
            "RAG system pre-warmed successfully"
        )

    except Exception as e:

        logger.error(
            f"Warning: Could not pre-warm RAG system: {e}"
        )

        proc.userdata["rag_ready"] = False


# ============================================================
# REGISTER PREWARM WITH AGENT SERVER
# ============================================================

server.setup_fnc = prewarm


# ============================================================
# LIVEKIT ENTRYPOINT
# ============================================================

@server.rtc_session()
async def entrypoint(ctx: JobContext):

    """
    Main LiveKit voice agent entrypoint.
    """


    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    metrics = ctx.proc.userdata.get("metrics")

    if metrics:

        metrics.increment_query_count()

        logger.info(
            f"Session started "
            f"(Query #{metrics.total_queries})"
        )


    # --------------------------------------------------------
    # LOG CONTEXT
    # --------------------------------------------------------

    ctx.log_context_fields = {
        "room": ctx.room.name,
    }


    # --------------------------------------------------------
    # CREATE AGENT SESSION
    # --------------------------------------------------------

    session = AgentSession(

        # ----------------------------------------------------
        # LLM / MULTI-AGENT RAG
        # ----------------------------------------------------

        llm=langchain.LLMAdapter(
            graph=graph
        ),


        # ----------------------------------------------------
        # SPEECH TO TEXT
        # ----------------------------------------------------

        stt=deepgram.STT(
            model="nova-3",
            language="multi",
        ),


        # ----------------------------------------------------
        # TEXT TO SPEECH
        # ----------------------------------------------------

        tts=cartesia.TTS(
            voice="6f84f4b8-58a2-430c-8c79-688dad597532"
        ),


        # ----------------------------------------------------
        # TURN DETECTION
        # ----------------------------------------------------

        turn_detection=MultilingualModel(),


        # ----------------------------------------------------
        # VAD
        # ----------------------------------------------------

        vad=ctx.proc.userdata["vad"],


        # ----------------------------------------------------
        # PREEMPTIVE GENERATION
        # ----------------------------------------------------

        preemptive_generation=True,
    )


    # ========================================================
    # FALSE INTERRUPTION HANDLER
    # ========================================================

    @session.on("agent_false_interruption")
    def _on_agent_false_interruption(
        ev: AgentFalseInterruptionEvent
    ):

        logger.info(
            "False positive interruption detected"
        )

        session.generate_reply(
            instructions=ev.extra_instructions
            or NOT_GIVEN
        )


    # ========================================================
    # METRICS COLLECTION
    # ========================================================

    usage_collector = (
        lk_metrics.UsageCollector()
    )


    @session.on("metrics_collected")
    def _on_metrics_collected(
        ev: MetricsCollectedEvent
    ):

        # LiveKit metrics

        lk_metrics.log_metrics(
            ev.metrics
        )

        usage_collector.collect(
            ev.metrics
        )


        # ----------------------------------------------------
        # CUSTOM METRICS
        # ----------------------------------------------------

        custom_metrics = (
            ctx.proc.userdata.get("metrics")
        )


        if (
            custom_metrics
            and hasattr(ev.metrics, "ttft")
        ):

            # ------------------------------------------------
            # TTFT
            # ------------------------------------------------

            if ev.metrics.ttft:

                custom_metrics.record_metric(
                    "ttft",
                    ev.metrics.ttft,
                    metadata={
                        "pipeline": "voice"
                    },
                )


            # ------------------------------------------------
            # STT LATENCY
            # ------------------------------------------------

            if hasattr(
                ev.metrics,
                "stt_latency",
            ):

                custom_metrics.record_metric(
                    "stt_latency",
                    ev.metrics.stt_latency,
                    metadata={
                        "provider": "deepgram",
                        "model": "nova-3",
                    },
                )


            # ------------------------------------------------
            # LLM LATENCY
            # ------------------------------------------------

            if hasattr(
                ev.metrics,
                "llm_latency",
            ):

                custom_metrics.record_metric(
                    "llm_inference",
                    ev.metrics.llm_latency,
                    metadata={
                        "provider": "langchain",
                        "backend": "multi-agent",
                    },
                )


            # ------------------------------------------------
            # TTS LATENCY
            # ------------------------------------------------

            if hasattr(
                ev.metrics,
                "tts_latency",
            ):

                custom_metrics.record_metric(
                    "tts_generation",
                    ev.metrics.tts_latency,
                    metadata={
                        "provider": "cartesia",
                    },
                )


    # ========================================================
    # SHUTDOWN LOGGING
    # ========================================================

    async def log_usage():

        summary = (
            usage_collector.get_summary()
        )

        logger.info(
            f"LiveKit Usage Summary: {summary}"
        )


        custom_metrics = (
            ctx.proc.userdata.get("metrics")
        )

        if custom_metrics:

            custom_metrics.log_summary()

            custom_metrics.save_to_json()


    ctx.add_shutdown_callback(
        log_usage
    )


    # ========================================================
    # START SESSION
    # ========================================================

    await session.start(

        agent=Assistant(),

        room=ctx.room,

        room_input_options=RoomInputOptions(

            noise_cancellation=(
                noise_cancellation.BVC()
            ),

        ),

    )


    # ========================================================
    # CONNECT TO LIVEKIT ROOM
    # ========================================================

    await ctx.connect()


# ============================================================
# START AGENT SERVER
# ============================================================

if __name__ == "__main__":
    cli.run_app(server)