from fastapi import FastAPI
from pydantic import BaseModel
from src.routes import contact
import uvicorn

app = FastAPI()

app.include_router(contact.router, prefix='/api')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)