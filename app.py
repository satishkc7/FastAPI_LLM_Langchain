from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes

import uvicorn

import os
from langchain_community.llms import Ollama

from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] =os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version="1.0",
    description = "A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)

#First model openai
model1 = ChatOpenAI()

##second model Ollama
model2 = Ollama(model = "Mistral")
prompt1 = ChatPromptTemplate.from_template("Write me something about {topic} in a paragraph")
prompt2 = ChatPromptTemplate.from_template("Write me something about {topic} in two paragraph and the second paragraph only contains two sentences")

add_routes(
    app,
    prompt1|model1,
    path = "/onepara"
)

add_routes(
    app,
    prompt2|model2,
    path = "/twopara"
)

if __name__ == "__main__":
    uvicorn.run(app,host = "localhost", port = 8000)
