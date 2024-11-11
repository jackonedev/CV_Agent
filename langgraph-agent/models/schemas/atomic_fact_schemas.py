from pydantic import BaseModel, Field


class AtomicFactOutput(BaseModel):
    updated_notebook: str = Field(
        description="""First, combine your current notebook with new insights and findings about
the question from current atomic facts, creating a more complete version of the notebook that
contains more valid information."""
    )
    rational_next_action: str = Field(
        description="""Based on the given question, the rational plan, previous actions, and
notebook content, analyze how to choose the next action."""
    )
    chosen_action: str = Field(
        description="""1. read_chunk(List[ID]): Choose this action if you believe that a text chunk linked to an atomic
fact may hold the necessary information to answer the question. This will allow you to access
more complete and detailed information.
2. stop_and_read_neighbor(): Choose this action if you ascertain that all text chunks lack valuable
information."""
    )
