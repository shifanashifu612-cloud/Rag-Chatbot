import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./data/chroma_db"
)

collection = client.get_or_create_collection(
    name="rag_collection"
)

print("Document count:", collection.count())


def add_documents(chunks):

    for chunk in chunks:

        collection.add(
            documents=[chunk],
            ids=[str(uuid.uuid4())]
        )

    print(
        "Current document count:",
        collection.count()
    )


def search_documents(query):

    print("Searching:", query)

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    print("Results:", results)

    return results