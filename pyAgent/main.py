from fastapi import FastAPI;
from app.api.v1.routes.homeRoute import router as home_router;
from  app.configs import settings;

app = FastAPI();

app.include_router(home_router);


