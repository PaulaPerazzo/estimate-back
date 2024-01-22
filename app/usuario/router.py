from fastapi import APIRouter, HTTPException, Path, Depends
from ..database.config import SessionLocal
from sqlalchemy.orm import Session
from ..database.schemas import UsuarioSchema,RequestUsuario,Response
import usuario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_usuario(request: RequestUsuario, db: Session = Depends(get_db)):
    usuario.create_usuario(db, usuario=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)


@router.get("/")
async def get_usuario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _usuario = usuario.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_usuario)

@router.get("/{usuario_id}")
def read_user(usuario_id: int, db: Session = Depends(get_db)):
    _usuario = usuario.get_usuario_by_id(db, usuario_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_usuario).dict(exclude_none=True)


@router.post("/")
async def update_usuario(request: RequestUsuario, db: Session = Depends(get_db)):
    _book = usuario.update_usuario(usuario_id = request.parameter.id, nome= request.parameter.nome,email= request.parameter.email
                                   ,senha= request.parameter.senha,experiencia= request.parameter.experiencia,data_cadastro= request.parameter.data_cadastro,
                                   tipo = request.parameter.tipo,horas_semanais =  request.parameter.horas_semanais,empresa_id = request.parameter.empresa_id,
                                   cargo_atual= request.parameter.cargo_atual,nickname=request.parameter.nickname,especialista = request.parameter.especialista)
    return Response(status="Ok", code="200", message="Success update data", result=_book)


@router.delete("/{usuario_id}")
async def delete_book(usuario_id:int,  db: Session = Depends(get_db)):
    usuario.remove_usuario(db, usuario_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)