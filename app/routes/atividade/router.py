from fastapi import APIRouter, HTTPException, Path, Depends
from database.config import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
