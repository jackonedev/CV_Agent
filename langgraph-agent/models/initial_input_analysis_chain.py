import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from models.prompts.initial_input_analysis_prompts import (
    initial_input_plan_system,
)

# Loading environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o", temperature=0.1, top_p=0, api_key=openai_api_key
)

# Model 7: Previous prompt analysis
initial_input_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            initial_input_plan_system,
        ),
        (
            "human",
            ("{question}"),
        ),
    ]
)

initial_input_chain = initial_input_prompt | model | StrOutputParser()
