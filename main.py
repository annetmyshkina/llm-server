import httpx
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="LLM Service")


@app.get("/")
async def root():
    return {"message": "Hello from LLM Service!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
