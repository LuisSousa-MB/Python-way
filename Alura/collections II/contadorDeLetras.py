from collections import defaultdict, Counter

texto_1 = """
    O presidente Luiz Inácio Lula da Silva (PT) realizou um pronunciamento nesta segunda-feira, 23, 
    durante viagem à Argentina e falou sobre a troca no comando do Exército brasileiro – 
    ocorrida no último sábado, 21, quando o general Júlio César de Arruda foi demitido com menos de um mês
     após assumir o cargo. Em sua fala, o chefe do Executivo ressaltou que havia escolhido o comandante da Força,
      mas que sua decisão não deu certo. “Eu tirei e escolhi outro [comandante]. Tive uma boa conversa com o comandante 
      [Tomás Ribeiro Miguel Paiva] e ele pensa exatamente com tudo o que eu tenho falado com a questão das Forças Armadas.
       As Forças não servem a um político, ela não existe para servir a um político”, disse o presidente após pontuar que as 
       funções dos militares é garantira soberania brasileira contra possíveis inimigos externos. Júlio César de Arruda assumiu o
        cargo de comando do Exército no dia 30 de dezembro, de maneira interina, ainda nos últimos dias do governo Bolsonaro após
         um acerto junto à equipe de transição de Lula. No dia 6 de janeiro, o ministro da Defesa, José Múcio Monteiro confirmou 
         que Arruda permaneceria no cargo. Dois dias após a confirmação, manifestantes invadiram e depredaram a sede dos Três Poderes 
         – Congresso Nacional, Palácio do Planalto e Supremo Tribunal Federal (STF), em Brasília. Com isso, o presidente Lula passou 
         a destacar sua falta de confiança com o agora ex-comandante do Exército.
"""

texto_2 = """
    No último sábado, 21, o ministro da Defesa participou de uma reunião com o presidente Lula e confirmou a troca no comando da Força.
     Aos jornalistas, Múcio confessou que a troca acontecera devido aos acontecimentos em Brasília no dia 8 de janeiro, que causaram uma
      “fratura no nível de confiança” entre o governo federal e a instituição. “Nós achávamos que nós precisávamos estancar isso logo
       de início até pra que nós pudéssemos superar esse episódio”, completou o chefe da pasta após ressaltar as tentativas do governo
        federal numa aproximação entre o Palácio do Planalto e as Forças Armadas. Em seguida, Lula oficializou em suas redes sociais a troca:
         “Hoje, junto com o ministro da Defesa, José Múcio, conversei com o general Tomás Miguel Ribeiro Paiva, o novo comandante do Exército.
          Desejo um bom trabalho ao general”. A citação do suposto alinhamento do novo general com o governo federal refere-se aos
           posicionamentos recentes de Tomás Paiva enquanto comandante militar do Sudeste. No último dia 18 de janeiro, o militar discursou
            à sua tropa e conclamou respeito das Forças Armadas ao resultado eleitoral. “Ser militar é ser profissional, respeitar a hierarquia
             e a disciplina. É ser coeso, íntegro, ter espírito de corpo e defender a pátria. É ser uma instituição de Estado, apolítica e 
             apartidária. Não interessa quem está no comando, a gente vai cumprir a missão do mesmo jeito. Também é o regime do povo. Alternância de
              poder. É o voto, e quando a gente vota, tem que respeitar o resultado da urna. Não interessa. Tem que respeitar. É essa a convicção
               que a gente tem que ter, mesmo que a gente não goste. Nem sempre a gente gosta, nem sempre é o que a gente queria. Não interessa. 
               Esse é o papel da instituição de Estado, da instituição que respeita os valores da pátria. Somos Estado”, declarou.
"""


conta_letras = defaultdict(int)
palavras_texto_1 = texto_1.lower().split()
for palavra in palavras_texto_1:
    for x in palavra:
        conta_letras[x] += 1

#print(conta_letras)

def analisa_frequencia_letras(texto):
    contador_texto_1 = Counter(texto.lower())

    total_letras = sum(contador_texto_1.values())

    proporcoes = [(letra, frequencia/total_letras) for letra, frequencia in contador_texto_1.items()]
    mais_frequentes = Counter(dict(proporcoes)).most_common(10)
    for char, proporcao in mais_frequentes:
        print("{} => {}%".format(char, round(proporcao * 100,2)))

analisa_frequencia_letras(texto_1)
#print(conta_letras,"\n\n", contador_texto_1)