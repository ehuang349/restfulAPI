from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from config import settings

app = FastAPI()


# Data model

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/api/")
def read_root():
    print(f"Environment: {settings.environment} Debug: {settings.debug}")
    return {"Environment": settings.environment, "Debug": settings.debug}

