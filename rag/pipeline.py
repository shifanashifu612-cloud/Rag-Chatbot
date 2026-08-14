from vectorstore.chroma_store import search_documents

def retrieve_context(query):

    print("Searching:", query)

    results = search_documents(query)

    print("Results:", results)

    docs = results["documents"][0]

    return "\n".join(docs)