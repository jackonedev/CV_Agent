import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from models.prompts.initial_node_prompts import (
    initial_node_system,
)
from models.schemas.initial_node_schemas import (
    InitialNodes,
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


# Model 2: Initial nodes Selection
initial_node_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            initial_node_system,
        ),
        (
            "human",
            (
                """\
Question: {question}
Plan: {rational_plan}
Nodes: {nodes}"""
            ),
        ),
    ]
)

initial_nodes_chain = initial_node_prompt | model.with_structured_output(InitialNodes)