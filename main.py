from fastapi import FastAPI
from config import settings
import uvicorn
import aiohttp

app = FastAPI()


# fetch from an external API endpoint that is async
async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


@app.get("/api/fetch_async")
async def fetch_async():
    url = "http://www.example.com/api/"
    response = await fetch(url)
    return {"content": response}


@app.get("/api/")
def read_root():
    return {"Environment": settings.environment, "Debug": settings.debug}


if __name__ == "__main__":
    if settings.environment == "dev":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# guide for running in production specifically
# step 1: Open terminal and navigate to the project directory
# cd path\to\your\project
# step 2: set environment variables for the environment
# $env:ENVIRONMENT = "prod"
# $env:DEBUG = "False"
# step 3: run uvicorn command
# uvicorn main:app --host 0.0.0.0 --port 8000 --w 4 --log-level info
