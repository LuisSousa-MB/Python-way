import requests

class BuscarEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("O cep informado não é válido.")

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def busca_endereço(self):
        r = requests.get("https://viacep.com.br/ws/{}/json/".format(self.cep))
        endereco = r.json()
        for key in endereco:
            if key != "complemento" and key != "ibge" and key != "gia" and key != "ddd" and key != "siafi":
                print(key,"=", endereco[key])