from datetime import date

class Funcionario:

    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario
    
    def idade(self):
        splited_date = self._data_nascimento.split("/")
        ano_nascimento = splited_date[-1]
        data_atual = date.today().year
        idade =  int(data_atual) - int(ano_nascimento)
        return idade

    def sobrenome(self):
        nome_completo = self._nome.strip()
        splited_name = nome_completo.split(" ")
        return splited_name[-1]
    
    def bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("O sálario é muito alto para receber o bonus")
        return valor

    def _eh_socio(self):
        sobrenomes = ["Bragança", "Windsor", "Bourbon", "Yamato", "Al Saud", "Khan", "Tudor", "Ptolomeu"]
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)
        
    def descrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo
 
    def __str__(self):
        return f'NOME: {self._nome}\nIDADE: {self.idade()} \nSALARIO: { self._salario}'