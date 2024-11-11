import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from models.prompts.rational_prompts import rational_plan_system

# Loading environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o-mini", temperature=0.0, top_p=0.1, api_key=openai_api_key
)


# Model 1: Rational chain
rational_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            rational_plan_system,
        ),
        (
            "human",
            ("{question}"),
        ),
    ]
)

rational_chain = rational_prompt | model | StrOutputParser()
