from fastapi import FastAPI
from config import settings
import uvicorn
import aiohttp

app = FastAPI(
    title="My API",
    description="API Description",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


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
    else:
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False, workers=4)

# guide for running in production specifically
# create a start_dev.bat or start_prod.bat file
# see files in project directory
