from fastapi import APIRouter, HTTPException, Path, Depends
from database.config import SessionLocal
from sqlalchemy.orm import Session
from database.schemas import ProjetoSchema,RequestProjeto,Response
from routes.projeto import functions as projeto_routes
from datetime import datetime
import pytz

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_projeto(request: RequestProjeto, db: Session = Depends(get_db)):
    projeto_routes.f_create_projeto(db, projeto=request)
    return Response(status="Ok",
                    code="200",
                    message="Projeto criado",
                    result=request).dict(exclude_none=True)


@router.get("/")
async def get_projetos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projetos_list = projeto_routes.f_get_projeto_all(db, skip, limit)
    if len(projetos_list) != 0:
        return Response(status="Ok", code="200", message="Projetos coletados", result=projetos_list)
    else:
        return Response(status="Ok", code="200", message="Nenhum projeto foi encontrado", result=None)

@router.get("/{projeto_id}")
def get_projeto_por_id(projeto_id: int, db: Session = Depends(get_db)):
    _projeto = projeto_routes.f_get_projeto_by_id(db, projeto_id)
    if _projeto is None:
        return Response(status="Ok", code="200", message=f"Projeto com o ID {projeto_id} não encontrado.", result=None).dict(exclude_none=True)
    else:
        return Response(status="Ok", code="200", message="Projeto coletado", result=_projeto).dict(exclude_none=True)


@router.post("/")
async def update_projeto(request: RequestProjeto,projeto_id: int, db: Session = Depends(get_db)):

    fuso_horario = pytz.timezone('America/Sao_Paulo')
    data_atual = datetime.now().astimezone(fuso_horario)
    _projeto = projeto_routes.f_update_projeto(db,projeto_id = projeto_id, nome= request.nome,
                                               descricao= request.descricao,
                                               data_inicio= request.data_inicio,
                                               data_conclusao_prevista= request.data_conclusao_prevista,
                                               data_conclusao_real= request.data_conclusao_real,
                                               num_desenvolvedores= request.num_desenvolvedores,
                                               horas_desenvolvimento= request.horas_desenvolvimento,
                                               stack= request.stack,
                                               senioridade= request.senioridade,
                                               area= request.area)
    return Response(status="Ok", code="200", message="Update feito com sucesso", result=request)


@router.delete("/{projeto_id}")
async def delete_projeto(projeto_id:int,  db: Session = Depends(get_db)):
    projeto_routes.f_remove_projeto(db, projeto_id)
    return Response(status="Ok", code="200", message="Delete feito com sucesso", result= f'ID: {projeto_id}').dict(exclude_none=True)