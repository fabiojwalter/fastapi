from api.routers import api_router
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables from .env file
load_dotenv()

app = FastAPI()


# Adiciona o router ao objeto `app`
app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, port=int(os.getenv("API_PORT")), host=os.getenv("API_HOST"))
