from fastapi import FastAPI
from contextlib import asynccontextmanager
import threading

from app.routes import router
from app.database import create_tables
from app.event_consumer import consume_events

@asynccontextmanager
async def lifespan(server: FastAPI):
    # 🌱 Startup: create DB tables and start RabbitMQ consumer
    create_tables()
    threading.Thread(target=consume_events, daemon=True).start()
    yield
    # 🧹 Shutdown: add cleanup here if needed

app = FastAPI(title="Billing Service", lifespan=lifespan)

app.include_router(router)
