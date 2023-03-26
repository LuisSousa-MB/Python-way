url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

#Sanitização da URL


#validação da URL
url_valida = len(url) > 0
if url_valida:
    #Separa a URL base e os parâmetros
    indice_interrogacao = url.find('?')
    url_base = url[0:indice_interrogacao]
    url_paramentros = url[indice_interrogacao+1:]

    moeda_origem = "moedaOrigem"
    moeda_destino = "moedaDestino"
    quantidade = "quantidade"
    #Busca o valor de um parâmetro
    parametro_busca = quantidade
    indice_parametro = url_paramentros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    indice_e_comercial = url_paramentros.find('&', indice_valor)
    if indice_e_comercial == -1:
        valor =  url_paramentros[indice_valor:]
    else:
        valor =  url_paramentros[indice_valor:indice_e_comercial]
        
    print(valor)
else:
    raise ValueError("A Url está vazia...")