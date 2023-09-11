from fastapi import FastAPI

app = FastAPI()

@app.get("/api/server/query")
def hello_world():
    return {"message": "Hello World"}