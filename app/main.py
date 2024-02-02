from api.routers import api_router
from dotenv import dotenv_values, load_dotenv
from fastapi.staticfiles import StaticFiles
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from .database import Database

from fastapi import FastAPI, HTTPException

# Load environment variables from .env file
load_dotenv()
ENV_VARS = dotenv_values()

app = FastAPI()
db = Database(
    host=ENV_VARS["DATABASE_HOST"],
    port=ENV_VARS["DATABASE_PORT"],
    database=ENV_VARS["DATABASE_NAME"],
    user=ENV_VARS["DATABASE_USER"],
    password=ENV_VARS["DATABASE_PASSWORD"],
)


limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(HTTPException, _rate_limit_exceeded_handler)

# Add the router to the `app` object
app.include_router(api_router, prefix="/api")

# Serve static files including favicon
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.router.on_startup
async def startup_event():
    await db.connect()


@app.router.on_shutdown
async def shutdown_event():
    await db.disconnect()
