import os

from langchain_community.graphs import Neo4jGraph
from dotenv import load_dotenv

load_dotenv()


# Connect to the Neo4j database
URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

graph = Neo4jGraph(
    refresh_schema=False,
    url=URI,
    username=AUTH[0],
    password=AUTH[1],
)