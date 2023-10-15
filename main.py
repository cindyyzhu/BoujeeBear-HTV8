import uvicorn

from fastapi import FastAPI
from flashcards import words, record_text

app = FastAPI()


@app.get("/speech")
def txt2speech():
    record_text()
    words()
    return {"test": "World"}

if __name__ == "__main__":
    # Start the Uvicorn server to run the FastAPI application
    uvicorn.run("main:app", port=5000, log_level="info")
