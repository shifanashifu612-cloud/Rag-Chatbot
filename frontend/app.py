import streamlit as st
import requests

st.title("RAG AI Chatbot")

question = st.text_input("Ask a question")

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "session_id": "user1",
            "question": question
        }
    )

    st.write(response.json())