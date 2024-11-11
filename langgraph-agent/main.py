from typing import Literal

from inference_call import (
    answer_reasoning,
    atomic_fact_check,
    chunk_check,
    initial_node_selection,
    neighbor_select,
    rational_plan_node,
)
from langgraph.graph import END, START, StateGraph
from models.schemas.state_schemas import InputState, OutputState, OverallState


def atomic_fact_condition(
    state: OverallState,
) -> Literal["neighbor_select", "chunk_check"]:
    if state.get("chosen_action") == "stop_and_read_neighbor":
        return "neighbor_select"
    elif state.get("chosen_action") == "read_chunk":
        return "chunk_check"


def chunk_condition(
    state: OverallState,
) -> Literal["answer_reasoning", "chunk_check", "neighbor_select"]:
    if state.get("chosen_action") == "termination":
        return "answer_reasoning"
    elif state.get("chosen_action") in [
        "read_subsequent_chunk",
        "read_previous_chunk",
        "search_more",
    ]:
        return "chunk_check"
    elif state.get("chosen_action") == "search_neighbor":
        return "neighbor_select"


def neighbor_condition(
    state: OverallState,
) -> Literal["answer_reasoning", "atomic_fact_check"]:
    if state.get("chosen_action") == "termination":
        return "answer_reasoning"
    elif state.get("chosen_action") == "read_neighbor_node":
        return "atomic_fact_check"


def main():
    langgraph = StateGraph(OverallState, input=InputState, output=OutputState)
    langgraph.add_node(rational_plan_node)
    langgraph.add_node(initial_node_selection)
    langgraph.add_node(atomic_fact_check)
    langgraph.add_node(chunk_check)
    langgraph.add_node(answer_reasoning)
    langgraph.add_node(neighbor_select)

    langgraph.add_edge(START, "rational_plan_node")
    langgraph.add_edge("rational_plan_node", "initial_node_selection")
    langgraph.add_edge("initial_node_selection", "atomic_fact_check")
    langgraph.add_conditional_edges(
        "atomic_fact_check",
        atomic_fact_condition,
    )
    langgraph.add_conditional_edges(
        "chunk_check",
        chunk_condition,
    )
    langgraph.add_conditional_edges(
        "neighbor_select",
        neighbor_condition,
    )
    langgraph.add_edge("answer_reasoning", END)

    return langgraph.compile()
