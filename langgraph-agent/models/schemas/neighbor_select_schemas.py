from pydantic import BaseModel, Field


class NeighborOutput(BaseModel):
    rational_next_move: str = Field(
        description="""Based on the given question, rational plan, previous actions, and
notebook content, analyze how to choose the next action."""
    )
    chosen_action: str = Field(
        description="""You have the following Action Options:
1. read_neighbor_node(key element of node): Choose this action if you believe that any of the
neighboring nodes may contain information relevant to the question. Note that you should focus
on one neighbor node at a time.
2. termination(): Choose this action if you believe that none of the neighboring nodes possess
information that could answer the question."""
    )

