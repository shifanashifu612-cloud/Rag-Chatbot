from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def generate_response(prompt):
    return llm.invoke(prompt)