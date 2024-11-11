import asyncio
import logging.config
from datetime import datetime

from langchain_text_splitters import TokenTextSplitter
from models.input_chain import input_chain
from utils.client import graph
from utils.file_extraction import extract_docx
from utils.utils import encode_md5

# Set log level to DEBUG for all neo4j_graphrag.* loggers
logging.config.dictConfig(
    {
        "version": 1,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            }
        },
        "loggers": {
            "root": {
                "handlers": ["console"],
            },
            "neo4j_graphrag": {
                "level": "DEBUG",
            },
        },
    }
)


async def process_document(
    text, document_name, chunk_size=2000, chunk_overlap=200
):
    start = datetime.now()
    print(f"Started extraction at: {start}")
    text_splitter = TokenTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    texts = text_splitter.split_text(text)
    print(f"Total text chunks: {len(texts)}")
    tasks = [
        asyncio.create_task(
            input_chain.ainvoke(
                {
                    "input": chunk_text,
                    "context": "Agustin Federico Stigliano GenAI Developer CV",
                }
            )
        )
        for index, chunk_text in enumerate(texts)
    ]
    results = await asyncio.gather(*tasks)
    print(f"Finished LLM extraction after: {datetime.now() - start}")
    docs = [el.dict() for el in results]
    for index, doc in enumerate(docs):
        doc["chunk_id"] = encode_md5(texts[index])
        doc["chunk_text"] = texts[index]
        doc["index"] = index
        for af in doc["atomic_facts"]:
            af["id"] = encode_md5(af["atomic_fact"])
    # Import chunks/atomic facts/key elements
    graph.query(
        """\
MERGE (d:Document {id:$document_name})
WITH d
UNWIND $data AS row
MERGE (c:Chunk {id: row.chunk_id})
SET c.text = row.chunk_text,
    c.index = row.index,
    c.document_name = row.document_name
MERGE (d)-[:HAS_CHUNK]->(c)
WITH c, row
UNWIND row.atomic_facts AS af
MERGE (a:AtomicFact {id: af.id})
SET a.text = af.atomic_fact
MERGE (c)-[:HAS_ATOMIC_FACT]->(a)
WITH c, a, af
UNWIND af.key_elements AS ke
MERGE (k:KeyElement {id: ke})
MERGE (a)-[:HAS_KEY_ELEMENT]->(k)
""",
        params={"data": docs, "document_name": document_name},
    )
    # Create next relationships between chunks
    graph.query(
        """\
MATCH (c:Chunk)<-[:HAS_CHUNK]-(d:Document)
WHERE d.id = $document_name
WITH c ORDER BY c.index WITH collect(c) AS nodes
UNWIND range(0, size(nodes) -2) AS index
WITH nodes[index] AS start, nodes[index + 1] AS end
MERGE (start)-[:NEXT]->(end)
""",
        params={"document_name": document_name},
    )
    print(f"Finished import at: {datetime.now() - start}")


async def main(file_path, document_name):

    # Executing neo4j query for building nodes
    graph.query(
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Chunk) REQUIRE c.id IS UNIQUE"
    )
    graph.query(
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:AtomicFact) REQUIRE c.id IS UNIQUE"
    )
    graph.query(
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:KeyElement) REQUIRE c.id IS UNIQUE"
    )

    text = extract_docx(file_path)

    await process_document(
        text, document_name, chunk_size=800, chunk_overlap=100
    )


if __name__ == "__main__":

    asyncio.run(
        main(
            file_path="db_files/docx/Agus_Stigliano-GenAI_Developer.docx",
            document_name="Agustin Federico Stigliano CV",
        )
    )

    print("Done!", end="\n\n")
