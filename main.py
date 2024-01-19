from fastapi import FastAPI
from internal import admin
from routers import project, user

app = FastAPI()

# Incluir Rotas
app.include_router(user.router, tags=["User"])
app.include_router(project.router, tags=["Project"])
app.include_router(admin.router,tags=["Admin"])

# Get da Main
@app.get("/", tags=["Main"])
async def root():
    return {"message": "V1.0.0 API EstiMate"}