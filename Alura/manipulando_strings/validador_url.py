import re

url = "https://www.bytebank.com/cambio"

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
valida = padrao_url.match(url) #Match  Search: Busca pelo padrão na string Match: Compara a strig ao padrão
if not valida:
    raise ValueError("A URL não é válida...")
else:
    print("URL válida!")