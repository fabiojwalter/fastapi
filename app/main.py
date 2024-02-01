from api.routers import api_router
from fastapi import FastAPI
from dotenv import dotenv_values, load_dotenv
import os
import uvicorn

# Load environment variables from .env file
load_dotenv()
ENV_VARS = dotenv_values()

app = FastAPI()


# Adiciona o router ao objeto `app`
app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, port=int(ENV_VARS["API_PORT"]), host=ENV_VARS["API_HOST"])
