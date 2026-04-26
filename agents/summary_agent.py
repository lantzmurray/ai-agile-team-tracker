"""Standup summary agent for Project 22."""

from agents.base import run_agent_task


def summarize(session_id: str, context_data: dict) -> str:
    """Condense daily standup text into a leadership-friendly snapshot."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Summary Agent",
        context_data=context_data,
        objective=(
            "Summarize the team's daily update into a concise view of what moved, "
            "what is in flight, and what needs leadership attention."
        ),
        sections=[
            "Team snapshot",
            "Highlights and momentum",
            "Items to watch",
        ],
        extra_guidance=(
            "Keep the tone crisp like a real async standup digest. Separate facts "
            "from inferred momentum."
        ),
    )
