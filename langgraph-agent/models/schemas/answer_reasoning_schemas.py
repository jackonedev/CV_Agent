from pydantic import BaseModel, Field


class AnswerReasonOutput(BaseModel):
    analyze: str = Field(
        description="""You should first analyze each notebook content before providing a final answer.
    During the analysis, consider complementary information from other notes and employ a
majority voting strategy to resolve any inconsistencies."""
    )
    final_answer: str = Field(
        description="""When generating the final answer, ensure that you take into account all available information."""
    )
