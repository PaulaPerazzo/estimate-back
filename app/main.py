from fastapi import FastAPI
from internal import admin
from usuario import usuario
from os import environ as env
from fastapi.middleware.cors import CORSMiddleware
import database.model as model
from database.config import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir Rotas
app.include_router(usuario.router,prefix="/usuario", tags=["User"])
app.include_router(admin.router,tags=["Admin"])

# Get da Main
@app.get("/", tags=["Main"])
async def root():
    return {"message": f"V1.0.1 API EstiMate"}