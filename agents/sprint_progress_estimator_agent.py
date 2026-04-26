"""Sprint progress estimator agent for Project 22."""

from agents.base import run_agent_task


def estimate_progress(session_id: str, context_data: dict) -> str:
    """Estimate delivery confidence from the current standup signal."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Sprint Progress Estimator",
        context_data=context_data,
        objective=(
            "Estimate whether the sprint is on track, at risk, or slipping based "
            "on what the team reported today."
        ),
        sections=[
            "Delivery forecast",
            "Evidence behind the forecast",
            "Manager callouts",
        ],
        extra_guidance=(
            "Use language like on track, watch closely, or at risk. Explain what "
            "signal in the update led to that read."
        ),
    )
