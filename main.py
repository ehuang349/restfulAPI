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
        uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=4)


# command below to start virtual environment if not automatic .\.venv\Scripts\activate
# the path above will run the activate script that is built in to start the virtual environment.
# If you want to deactivate it, use the .\.venv\Scripts\deactivate
# you know the virtual environment is activated in terminal by the identity (.venv)

#command below; this assumes you already started the virtual environment at the root of your project
# python main.py
