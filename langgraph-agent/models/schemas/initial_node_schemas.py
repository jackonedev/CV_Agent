from typing import List

from pydantic import BaseModel, Field


class Node(BaseModel):
    key_element: str = Field(
        description="""Key element or name of a relevant node"""
    )
    score: int = Field(
        description="""Relevance to the potential answer by assigning
a score between 0 and 100. A score of 100 implies a high likelihood of relevance to the answer,
whereas a score of 0 suggests minimal relevance."""
    )


class InitialNodes(BaseModel):
    initial_nodes: List[Node] = Field(
        description="List of relevant nodes to the question and plan"
    )
