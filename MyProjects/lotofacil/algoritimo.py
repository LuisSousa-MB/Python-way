from db import conecta_db
from contagem_dezenas_bd import ContagemDezenas
import random

session, Base = conecta_db()

dezenas_analisadas = 12
qnt_jogos = 12

def dezenas_mais_sorteadas(qtd_dezenas):

    dezenas = []
    for contagem in session.query(ContagemDezenas).order_by(ContagemDezenas.vezes_sorteada.desc()).limit(qtd_dezenas):
        dezenas.append(contagem.dezena)
    
    return dezenas

def dezenas_menos_sorteadas(qtd_dezenas):
    dezenas = []
    for contagem in session.query(ContagemDezenas).order_by(ContagemDezenas.vezes_sorteada).limit(qtd_dezenas):
        dezenas.append(contagem.dezena)
    
    return dezenas

def gerar_listas_dezenas(mais, menos):
    listas_dezenas = []
    
    for x in range(6):
        lista_10_mais_5_menos = pop_number(mais,10) + pop_number(menos, 5)
        lista_10_menos_5_mais = pop_number(menos, 10) + pop_number(mais, 5)
        if sorted(lista_10_mais_5_menos) not in listas_dezenas:
            listas_dezenas.append(sorted(lista_10_mais_5_menos))
        if sorted(lista_10_menos_5_mais) not in listas_dezenas:
            listas_dezenas.append(sorted(lista_10_menos_5_mais))
    return listas_dezenas

def pop_number(lista, numbers):
    list_to_pop = [x for x in lista]
    luck_numbers = []
 
    for i in range (0, numbers):
        luck = random.randint(1,5)
        if luck != 3:
            print("Adicionando !!!", list_to_pop[0])
            luck_numbers.append(list_to_pop[0])
            list_to_pop.pop(0)
        else:
            number = random.sample(list_to_pop, 1)
            print("Adicionando >>>", number[0])
            luck_numbers.append(number[0])
            list_to_pop.remove(number[0])

    return luck_numbers
        


menos = dezenas_menos_sorteadas(dezenas_analisadas)
mais = dezenas_mais_sorteadas(dezenas_analisadas+1)
listas_jogos = gerar_listas_dezenas(mais,menos)


print("\n\nAs dezenas mais sorteadas foram {}.\nAs dezenas menos sorteadas foram {}.".format(mais,menos))
print("\nAqui estão {} jogos criados com base nessas informaçoes:".format(qnt_jogos))

for jogo in listas_jogos:
    print("\n{}".format(jogo))