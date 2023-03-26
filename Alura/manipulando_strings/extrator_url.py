import re

class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
            
    def valida_url(self):
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        valida = padrao_url.match(self.get_url_base())
        if not valida:
            raise ValueError("O endereço {} não corresponde a uma url valida para esta operação.".format(self.get_url_base()))        
        elif not self.url:
            raise ValueError("A Url está vazia...")            

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        if indice_interrogacao > 0:
            url_base = self.url[0:indice_interrogacao]    
        else:
            url_base = self.url
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_paramentros = self.url[indice_interrogacao+1:]
        return url_paramentros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor =  self.get_url_parametros()[indice_valor:]
        else:
            valor =  self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return "URL: " + self.url + "\nURL base: " + self.get_url_base() + "\nParêmetros: " + self.get_url_parametros()
    
    def __eq__(self, other) :
        return self.url == other.url

extrator_url = ExtratorUrl("https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
#extrator_url = ExtratorUrl("")

print("O tamanho da URl é de {} caracteres.".format(len(extrator_url)))
print(extrator_url)
parametro_quantidade = extrator_url.get_valor_parametro("quantidade")
parametro_moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
parametro_moeda_destino = extrator_url.get_valor_parametro("moedaDestino")

dolar = 5.25

if parametro_moeda_origem == "real" and parametro_moeda_destino == "dolar":
    conversao = float(parametro_quantidade)/ dolar
    simbolo = "USD"
elif parametro_moeda_origem == "dolar" and parametro_moeda_destino == "real":
    conversao = float(parametro_quantidade) * dolar
    simbolo = "R$"

print(parametro_quantidade)
print(parametro_moeda_origem)
print(parametro_moeda_destino)
print("O valor da converão é {} {}".format(simbolo,round(conversao,2)))