"""Blocker detector agent for Project 22."""

from agents.base import run_agent_task


def detect_blockers(session_id: str, context_data: dict) -> str:
    """Identify blockers, likely impact, and next unblocking moves."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Blocker Detector",
        context_data=context_data,
        objective=(
            "Look for blockers, dependencies, or ambiguous delivery risks inside "
            "the standup text and suggest practical unblocking actions."
        ),
        sections=[
            "Current blockers",
            "Impact and urgency",
            "Recommended unblock steps",
        ],
        extra_guidance=(
            "If no blocker is explicit, call out the most likely hidden risk and "
            "label it as an inference."
        ),
    )
