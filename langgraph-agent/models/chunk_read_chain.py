import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from models.prompts.chunk_read_prompts import (
    chunk_read_system_prompt,
)
from models.schemas.chunk_read_schemas import (
    ChunkOutput,
)


# Loading environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.0,
    top_p=0.1,
    api_key=openai_api_key
)



# Model 5: Chunk checker
chunk_read_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            chunk_read_system_prompt,
        ),
        (
            "human",
            (
                """\
Question: {question}
Plan: {rational_plan}
Previous actions: {previous_actions}
Notebook: {notebook}
Chunk: {chunk}"""
            ),
        ),
    ]
)

chunk_read_chain = chunk_read_prompt | model.with_structured_output(ChunkOutput)