from sqlalchemy.orm import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ as env

engine = create_engine(env['DATABASE_URL'])
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)
Base = declarative_base