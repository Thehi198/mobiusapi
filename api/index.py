from fastapi import FastAPI

app = FastAPI()

@app.get("/api/server/python")
def hello_world():
    return {"message": "Hello World"}