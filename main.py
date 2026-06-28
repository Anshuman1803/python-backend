from fastapi import FastAPI;
from app.api.v1.routes.homeRoute import router as home_router;
app = FastAPI();

app.include_router(home_router);


