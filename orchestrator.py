"""Orchestrator for Project 22."""

import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.base import generate_session_id, log_agent_response
from agents.summary_agent import summarize
from agents.blocker_detector_agent import detect_blockers
from agents.sprint_progress_estimator_agent import estimate_progress

AGENT_SEQUENCE = (
    ("Summary Agent", summarize),
    ("Blocker Detector", detect_blockers),
    ("Sprint Progress Estimator", estimate_progress),
)


class Orchestrator:
    """Run the async standup agents in a consistent order."""

    def generate_session_id(self) -> str:
        return generate_session_id()

    def run_workflow(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        session_id = self.generate_session_id()
        results = {}

        log_agent_response(
            session_id,
            "Workflow Input",
            "\n".join(
                f"- {key.replace('_', ' ').title()}: {value or 'Not provided'}"
                for key, value in inputs.items()
            ),
            {"kind": "input"},
        )

        for agent_name, agent_runner in AGENT_SEQUENCE:
            results[agent_name] = agent_runner(session_id, inputs)

        return {"session_id": session_id, "results": results}
