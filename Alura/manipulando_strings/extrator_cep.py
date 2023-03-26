import re

endereco = "Rua Bela vista 32A, Cantinho do céu, São Paulo, SP, 04849-567"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match  Search: Busca pelo padrão na string Match: Compara a strig ao padrão

if busca:
    cep = busca.group()
    print(cep)
else:
    print("CEP não encontrado.")