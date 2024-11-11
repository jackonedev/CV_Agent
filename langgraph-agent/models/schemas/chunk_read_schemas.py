from pydantic import BaseModel, Field


class ChunkOutput(BaseModel):
    updated_notebook: str = Field(
        description="""First, combine your previous notes with new insights and findings about the
question from current text chunks, creating a more complete version of the notebook that contains
more valid information."""
    )
    rational_next_move: str = Field(
        description="""Based on the given question, rational plan, previous actions, and
notebook content, analyze how to choose the next action."""
    )
    chosen_action: str = Field(
        description="""1. search_more(): Choose this action if you think that the essential information necessary to
answer the question is still lacking.
2. read_previous_chunk(): Choose this action if you feel that the previous text chunk contains
valuable information for answering the question.
3. read_subsequent_chunk(): Choose this action if you feel that the subsequent text chunk contains
valuable information for answering the question.
4. termination(): Choose this action if you believe that the information you have currently obtained
is enough to answer the question. This will allow you to summarize the gathered information and
provide a final answer."""
    )
