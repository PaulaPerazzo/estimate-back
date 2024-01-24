from fastapi import APIRouter, HTTPException, Path, Depends
from database.config import SessionLocal
from sqlalchemy.orm import Session
from database.schemas import UsuarioSchema,RequestUsuario,Response
from usuario import usuario_routes
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
async def create_usuario(request: RequestUsuario, db: Session = Depends(get_db)):
    usuario_routes.f_create_usuario(db, usuario=request)
    return Response(status="Ok",
                    code="200",
                    message="Usuario criado",
                    result=request).dict(exclude_none=True)


@router.get("/")
async def get_usuario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios_list = usuario_routes.f_get_usuario_all(db, skip, limit)
    if len(usuarios_list) != 0:
        return Response(status="Ok", code="200", message="Usuarios coletados", result=usuarios_list)
    else:
        return Response(status="Ok", code="200", message="Nenhum usuário foi encontrado", result=None)

@router.get("/{usuario_id}")
def read_user(usuario_id: int, db: Session = Depends(get_db)):
    _usuario = usuario_routes.f_get_usuario_by_id(db, usuario_id)
    if _usuario is None:
        return Response(status="Ok", code="200", message=f"Usuário com o ID {usuario_id} não encontrado.", result=None).dict(exclude_none=True)
    else:
        return Response(status="Ok", code="200", message="Usuario coletado", result=_usuario).dict(exclude_none=True)


@router.post("/")
async def update_usuario(request: RequestUsuario, db: Session = Depends(get_db)):

    fuso_horario = pytz.timezone('America/Sao_Paulo')
    data_atual = datetime.now().astimezone(fuso_horario)
    _usuario = usuario_routes.f_update_usuario(usuario_id = request.parameter.id, nome= request.parameter.nome,email= request.parameter.email
                                   ,senha= request.parameter.senha,experiencia= request.parameter.experiencia,data_cadastro= datetime.now(),
                                   tipo = request.parameter.tipo,horas_semanais =  request.parameter.horas_semanais,empresa_id = request.parameter.empresa_id,
                                   cargo_atual= request.parameter.cargo_atual,nickname=request.parameter.nickname,especialista = request.parameter.especialista)
    return Response(status="Ok", code="200", message="Update feito com sucesso", result=_usuario)


@router.delete("/{usuario_id}")
async def delete_usuario(usuario_id:int,  db: Session = Depends(get_db)):
    usuario_routes.f_remove_usuario(db, usuario_id)
    return Response(status="Ok", code="200", message="Delete feito com sucesso", result= usuario_id).dict(exclude_none=True)