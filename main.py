from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from config import settings
import uvicorn

app = FastAPI()


# Data model

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/api/")
def read_root():
    return {"Environment": settings.environment, "Debug": settings.debug}


if __name__ == "__main__":
    if settings.environment == "dev":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    else:
        uvicorn.run("main:app", host="127.0.0.1", port=8000, workers=1)
