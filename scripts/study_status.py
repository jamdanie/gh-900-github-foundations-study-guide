"""Local teaching example; this does not update a GitHub Project."""


def study_status(state):
    """Map a practice state to a board label, rejecting unknown states."""
    states = {"open": "Todo", "working": "In Progress", "closed": "Done"}
    key = state.strip().lower()
    if key not in states:
        raise ValueError(f"Unknown study state: {state!r}")
    return states[key]
