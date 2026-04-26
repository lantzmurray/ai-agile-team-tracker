import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))
sys.path.insert(0, PROJECT_ROOT)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from agents.base import get_session_history
from orchestrator import Orchestrator
from components import render_app_footer, run_with_status_updates

st.set_page_config(page_title="Agile Team Standup Tracker", layout="wide")


def render_session_log(session_id: str) -> None:
    """Expose the collaboration log so the system is easy to present and debug."""
    history = get_session_history(session_id)
    if not history:
        return

    st.subheader("Collaboration Log")
    for entry in history:
        timestamp = entry["timestamp"].replace("T", " ")
        with st.expander(f"{entry['agent']} · {timestamp}", expanded=False):
            st.markdown(entry["content"])


def main():
    st.title("Agile Team Standup Tracker")
    st.caption(
        "Support software teams with an AI-powered asynchronous standup system."
    )

    st.sidebar.title("Standup Input")
    daily_update = st.text_area(
        "Daily Update",
        height=240,
        placeholder=(
            "Yesterday: shipped the API client.\n"
            "Today: finishing integration tests.\n"
            "Blockers: waiting on staging credentials."
        ),
    )

    if st.button("Run Standup Agents", type="primary"):
        if not daily_update.strip():
            st.warning("Paste a standup update so the agents can analyze it.")
            return

        inputs = {"daily_update": daily_update.strip()}
        orch = Orchestrator()
        output = run_with_status_updates(
            lambda: orch.run_workflow(inputs),
            start_message="Agents are analyzing the standup update..."
        )

        st.success(f"Workflow Complete! Session ID: {output['session_id']}")

        for agent, response in output["results"].items():
            with st.expander(f"{agent} Response", expanded=True):
                st.markdown(response)

        render_session_log(output["session_id"])


    render_app_footer()

if __name__ == "__main__":
    main()
