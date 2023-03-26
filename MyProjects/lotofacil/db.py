from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def conecta_db():

    Base = declarative_base()

    engine = create_engine("postgresql://root:root@172.28.0.2:5432/root")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    return session, Base