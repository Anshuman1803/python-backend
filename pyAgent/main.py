from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.routes.homeRoute import router as home_router
from app.db import MongoDBConnection


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB when the application starts
    await MongoDBConnection.dbConnect()

    yield

    # Disconnect from MongoDB when the application shuts down
    await MongoDBConnection.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(home_router)