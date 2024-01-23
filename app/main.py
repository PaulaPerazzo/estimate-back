from fastapi import FastAPI
from routers.user import db_dependency
from os import environ as env
from fastapi.middleware.cors import CORSMiddleware
import models
from fastapi import FastAPI, status
from models import UserBase

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3306",
    "http://localhost:3307",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir Rotas
# app.include_router(user.router, tags=["User"])
# app.include_router(project.router, tags=["Project"])
# app.include_router(admin.router,tags=["Admin"])

# Get da Main

@app.get("/", tags=["Main"])
async def root():
    return {"message": f"V1.0.1 API EstiMate"}