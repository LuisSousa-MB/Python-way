
def Teste():
    print("\nteste")

    conta1 = criar_conta("João",3532,343.3,500)
    conta2 = criar_conta("Maria",3054,90.9,1000)
    extrato(conta1)
    print("\nteste")
    extrato(conta2)

    depositar(conta1,300)
    saque(conta2,50)
    extrato(conta1)
    extrato(conta2)


def criar_conta(titular,numero,saldo,limite):
    conta = {"Titular":titular,"Número": numero, "Saldo":saldo, "Limite": limite}
    return conta

def depositar(conta,valor):
    conta["Saldo"] += valor

def saque(conta,valor):
    conta["Saldo"] -= valor

def extrato(conta):
    print("Titular:",conta["Titular"])
    print("Número:",conta["Número"])
    print("O saldo da conta é R${}\nLimite disponivel R${}".format(conta["Saldo"],conta["Limite"]))

if (__name__ == "__main__"):
    Teste()
