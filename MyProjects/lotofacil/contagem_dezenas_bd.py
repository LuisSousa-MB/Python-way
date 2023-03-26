from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from collections import defaultdict
from recuperaresultados import Resultado
from db import conecta_db

session, Base = conecta_db()

class ContagemDezenas(Base):
    __tablename__ = "contagem_dezenas"
    dezena = Column(String, primary_key=True)
    vezes_sorteada = Column(Integer)

dezenas = []
for resultado in session.query(Resultado).all():
    dezenas.extend(resultado.dezenas.split(","))

contagem_dezenas = defaultdict(int)
for dezena in dezenas:
    contagem_dezenas[dezena] += 1

for dezena, vezes_sorteada in contagem_dezenas.items():
    cont = session.query(ContagemDezenas).filter_by(dezena=dezena).first()
    if cont:
        cont.vezes_sorteada = vezes_sorteada
    else:
        session.add(ContagemDezenas(dezena=dezena, vezes_sorteada=vezes_sorteada))

print("Feito")
session.commit()
