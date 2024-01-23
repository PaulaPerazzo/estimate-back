from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from os import environ as env

URL_DATABASE = "mysql+pymysql://root:password@localhost:3306/estimate_db" ## muda isso aqui
# engine = create_engine(env['DATABASE_URL'])
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()
