from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import os

DB_USER = os.environ.get['DB_USER']
DB_PASSW = os.environ.get['DB_PASSW']
DB_HOST = os.environ.get['HOST']
DB_NAME = os.environ.get['NAME']

mysql_route = f'msyql:///{DB_USER}:{DB_PASSW}@{DB_HOST}/{DB_NAME}'
engine = create_engine(mysql_route)
db_sesion = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_sesion.query_property()


def init_db() -> None:
    Base.metadata.create_all(bin=engine)
