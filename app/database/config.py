from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from os import environ as env

URL_DATABASE = "mysql+pymysql://root:password@mysql:3306/estimate_db" ## muda isso aqui

connection_string = URL.create(
    'postgresql',
    username='koyeb-adm',
    password='bA3rHPq8RcjV',
    host='ep-wispy-sun-a4atox3i.us-east-1.pg.koyeb.app',
    database='koyebdb',
)

# engine = create_engine(env['DATABASE_URL'])
# engine = create_engine(URL_DATABASE)
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()
