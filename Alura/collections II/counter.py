from collections import Counter

texto = "Bem vindo meu nome é Elias irei falar sobre os meus gostos eu gosto muito de cachorros e gatos eu gosto também de beber café"

texto = texto.lower()

meu_texto = Counter(texto.split())

print(meu_texto)