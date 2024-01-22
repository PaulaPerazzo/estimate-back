from fastapi import FastAPI
from internal import admin
from routers import project, user
from os import environ as env
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir Rotas
app.include_router(user.router, tags=["User"])
app.include_router(project.router, tags=["Project"])
app.include_router(admin.router,tags=["Admin"])

# Get da Main
@app.get("/", tags=["Main"])
async def root():
    return {"message": f"V1.0.1 API EstiMate"}