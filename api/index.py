from fastapi import FastAPI
import json
import time
import os
import pinecone
from langchain.embeddings import CohereEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import ConversationalRetrievalChain
from langchain.schema import Document
from langchain.chat_models import ChatAnthropic
from pydantic import BaseModel

# load api keys *required for vercel deployments*
from dotenv import load_dotenv
load_dotenv()

# import api keys and init models
PINECONE_KEY = os.environ.get("pinecone_key")
COHERE_KEY = os.environ.get("cohere_key")
ANTHROPIC_KEY = os.environ.get("anthropic_api_key")
pinecone.init(api_key=PINECONE_KEY, environment="us-central1-gcp")
embedding_dimension = 4096
embedding_model = CohereEmbeddings(cohere_api_key=COHERE_KEY, model="embed-english-v2.0")
llm = ChatAnthropic(model="claude-instant-v1", anthropic_api_key=ANTHROPIC_KEY)

#initialize fastapi
app = FastAPI()

#define data model
class query(BaseModel):
    question: str
    namespace: str
    index: str
    chat_history: list

class Index(BaseModel):
    name: str


@app.post("/api/server/query")  # You might want to use POST for creating resources
async def search_exe(request_body: Index):
    index_dict = request_body.dict()
    index_dict["status"] = "success"  # Add "status" field to the response
    return index_dict