import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from models.prompts.atomic_fact_prompts import atomic_fact_check_system
from models.schemas.atomic_fact_schemas import AtomicFactOutput

# Loading environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o-mini", temperature=0.0, top_p=0.1, api_key=openai_api_key
)


# Model 3: Atomic fact checker
atomic_fact_check_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            atomic_fact_check_system,
        ),
        (
            "human",
            (
                """\
Question: {question}
Plan: {rational_plan}
Previous actions: {previous_actions}
Notebook: {notebook}
Atomic facts: {atomic_facts}"""
            ),
        ),
    ]
)

atomic_fact_chain = atomic_fact_check_prompt | model.with_structured_output(
    AtomicFactOutput
)
