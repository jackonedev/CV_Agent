import ast
import re
from typing import List

from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

neo4j_vector = Neo4jVector.from_existing_graph(
    embedding=embeddings,
    index_name="keyelements",
    node_label="KeyElement",
    text_node_properties=["id"],
    embedding_node_property="embedding",
    retrieval_query="RETURN node.id AS text, score, {} AS metadata",
)


def get_potential_nodes(question: str, k: int = 40) -> List[str]:
    data = neo4j_vector.similarity_search(question, k=k)
    return [retrieve.page_content for retrieve in data]


def parse_function(input_str):

    pattern = r"(\w+)(?:\((.*)\))?"

    match = re.match(pattern, input_str)
    if match:
        function_name = match.group(1)
        raw_arguments = match.group(2)

        arguments = []
        if raw_arguments:
            try:

                parsed_args = ast.literal_eval(f"({raw_arguments})")

                arguments = (
                    list(parsed_args)
                    if isinstance(parsed_args, tuple)
                    else [parsed_args]
                )
            except (ValueError, SyntaxError):

                arguments = [raw_arguments.strip()]

        return {"function_name": function_name, "arguments": arguments}
    else:
        return None