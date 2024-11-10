import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from models.prompts.input_prompts import input_message
from models.schemas.input_schemas import Extraction

# Loading environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1, api_key=openai_api_key)

# Model 0: Input (Injest) chain
input_prompt = ChatPromptTemplate(
    [
        ("system", input_message),
        ("human", "context: {context}-\n\n{input}"),
    ]
)

input_chain = input_prompt | model.with_structured_output(Extraction)