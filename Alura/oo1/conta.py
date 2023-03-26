class Conta():
    def __init__(self,titular,numero,saldo,limite = 1000.0):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Titular:",self.__titular)
        print("Número:",self.__numero)
        print("O saldo da conta é R${}\nLimite disponivel R${}".format(self.__saldo,self.__limite))
    
    def depositar(self,valor):
        if self.__saldo < 0:
            self.__limite += valor
            if self.__limite > 1000.0:
                self.__limite = 1000.0
        self.__saldo += valor

    def __pode_sacar(self,valor):
        if self.__saldo >= 0:
            valor_disponivel = self.__saldo + self.__limite
        else:
            valor_disponivel = self.__limite
        if valor_disponivel >= valor:
            return True
    
    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        elif self.__pode_sacar(valor):
            if self.__saldo > 0:     
                debitar_do_limite = (valor - self.__saldo )
            else:
                debitar_do_limite = valor
            #print("Usando {} do limite".format(debitar_do_limite))
            self.__limite -= debitar_do_limite
            #print("Removendo {} do saldo".format(valor))
            self.__saldo -= valor
            #print("saldo: ", self.__saldo)
            return True
        else:
            print("Saldo ou limite insuficientes para esta operação...")

    def transferir(self,valor,destino):
        if self.sacar(valor):
            destino.depositar(valor)
        else:
            print("A conta de origem não possui saldo suficiente para esta operação.")

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_numero(self):
        return self.__numero
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,valor):
        self.__limite = valor

    @staticmethod
    def taxa_de_transferencia():
        return 5.5


