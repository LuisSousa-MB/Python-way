from collections import defaultdict

texto = "Bem bem bem bem  vindo meu nome é Elias irei falar sobre os meus gostos eu gosto muito de cachorros e gatos eu gosto também de beber café"

texto = texto.lower()

aparicoes = defaultdict(int)

for palavra in texto.split():
    aparicoes[palavra] += 1

print(aparicoes)