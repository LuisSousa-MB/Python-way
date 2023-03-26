import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import conecta_db

session, Base = conecta_db()

class Resultado(Base):
    __tablename__ = 'resultados_lotofacil'
    concurso = Column(Integer, primary_key=True)
    dezenas = Column(String)


# URL base para obter resultados de loterias
url_base = "https://apiloterias.com.br/app/resultado?"

# Parâmetros obrigatórios
loteria = "lotofacil"
token = "l4WAWuYWInvwfkV"

# Dicionário para armazenar resultados
resultados_lotofacil = {}
concurso_atual = 2731
concurso = 2729

""" while int(concurso) < concurso_atual :
    concurso += 1

    # Monta URL completa para requisição
    url = f"{url_base}loteria={loteria}&token={token}&concurso={concurso}"

    # Faz requisição e armazena resposta
    response = requests.get(url)

    # Verifica se houve erro na requisição
    if response.status_code != 200:
        break

    # Converte resposta para dicionário
    resultado = response.json()
    print(resultado)
    
    n_concurso = str(resultado["numero_concurso"])
    dezenas = resultado["dezenas"]
    #print(dezenas, n_concurso)
    # Armazena resultado no dicionário
    resultados_lotofacil[n_concurso] = dezenas
    #time.sleep(0.5)
    # print(resultados_lotofacil)

  
    resultado = Resultado(concurso=n_concurso, dezenas=",".join(dezenas))
    session.add(resultado)

    session.commit() """