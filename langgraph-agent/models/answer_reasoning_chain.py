import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from models.prompts.answer_reasoning_prompts import (
    answer_reasoning_system_prompt,
)
from models.schemas.answer_reasoning_schemas import AnswerReasonOutput

# Loading environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o", temperature=0.0, top_p=0.1, api_key=openai_api_key
)


# Model 6: answer_reasoning
answer_reasoning_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            answer_reasoning_system_prompt,
        ),
        (
            "human",
            (
                """\
Question: {question}
Notebook: {notebook}"""
            ),
        ),
    ]
)

answer_reasoning_chain = (
    answer_reasoning_prompt | model.with_structured_output(AnswerReasonOutput)
)
