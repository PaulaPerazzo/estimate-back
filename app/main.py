from fastapi import FastAPI
from routes.usuario import router as router_usuario
from routes.projeto import router as router_projeto
from routes.avaliacao import router as router_avaliacao
from routes.atividade import router as router_atividade
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
app.include_router(router_usuario.router, prefix="/user", tags=["Usuario"])
app.include_router(router_projeto.router, prefix="/project", tags=["Projeto"])
app.include_router(router_avaliacao.router, prefix="/rating", tags=["Avaliação"])
app.include_router(router_atividade.router, prefix="/task", tags=["Atividade"])

# Get da Main
@app.get("/", tags=["Root"])
async def root():
    return {"message": f"V1.0.1 API EstiMate"}