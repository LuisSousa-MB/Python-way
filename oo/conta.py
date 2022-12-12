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
    
    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        elif self.__saldo + self.__limite >= valor :
            self.__limite -= abs(self.__saldo - valor)
            self.__saldo -= valor
            return True
        else:
            print("Saldo ou limite insuficientes para esta operação...")

    def transferir(self,valor,destino):
        if self.sacar(valor):
            destino.depositar(valor)
        else:
            print("A conta de origem não possui saldo suficiente para esta operação.")