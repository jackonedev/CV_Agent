

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from models.prompts.neighbor_select_prompts import (
    neighbor_select_system_prompt,
)
from models.schemas.neighbor_select_schemas import (
    NeighborOutput,
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




# Model 4: Neighbor selection
neighbor_select_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            neighbor_select_system_prompt,
        ),
        (
            "human",
            (
                """\
Question: {question}
Plan: {rational_plan}
Previous actions: {previous_actions}
Notebook: {notebook}
Neighbor nodes: {nodes}"""
            ),
        ),
    ]
)

neighbor_select_chain = neighbor_select_prompt | model.with_structured_output(
    NeighborOutput
)
