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

class index(BaseModel):
    name: str


#search function
# def search(question, namespace, index, chat_history=[], model='anthropic', k=4):
#     """Search pinecone index for a given question.

#     Args:
#         question: The question being answered
#         namespace: The namespace to search
#         index: The index in which the specified namespace is contained
#         chat_history: The chat history formatted as [("Q", "A"), ("Q", "A")...]
#         model: The model used to interpret the question (choose from "palm" or "anthropic")
#         k: The number of responses returned

#     Returns:
#         tuple: The delay in seconds and the output as a dictionary

#             (
#                 delay, 
#                 {
#                     "question": question, 
#                     "result": result, 
#                     "documents": 
#                         [
#                             {"content": content, "source": source,}
#                             {"content": content, "source": source,}
#                                             ...
#                         ]
#                 }
#             )
#     """


#     docsearch = Pinecone.from_existing_index(index, embedding_model, namespace=namespace)
#     chat_history = [(item[0], item[1]) for item in chat_history]

#     qa = ConversationalRetrievalChain.from_llm(llm,docsearch.as_retriever(search_kwargs=dict(k=k)), return_source_documents=True,)

#     start = time.perf_counter()
#     xc = qa({"question": question, "chat_history": chat_history})
#     delay = time.perf_counter()-start


#     #format output
#     output = {"question": question, "result": xc["answer"], "documents": [{"content": doc.page_content, "source": doc.metadata} for doc in xc["source_documents"]]}
#     output["delay"] = delay 
#     return (delay, output)



@app.post("/api/server/query")
async def searchexe(request_body: index):
    #output = search(query.question, query.namespace, query.index, query.chat_history)
    output = {"name": request_body.name,
              "test": 1,}
    return output