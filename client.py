import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/one_para/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/two_para/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

st.title("FASTAPI LangServe")
input_text1= st.text_input("Write about ")
input_text2=st.text_input("Explain this ")


if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))