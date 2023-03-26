from abc import ABCMeta,abstractmethod
import random
import time

class Conta(metaclass=ABCMeta):

    def __init__(self, numConta, agencia, nome, cpf):
        self.numConta = numConta
        self.agencia = agencia
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0
        

    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    @abstractmethod
    def rotinaMensal():
        pass

    def __str__(self):
        return ">>Número da agência: {}\nNúmero da conta:  {}\nNome do Cliente: {}\nCPF: {}\nSaldo: {}<<".format(self.agencia,self.numConta,self.nome,self.cpf,self.saldo)

class ContaPoupanca(Conta):
    def __init__(self, numConta, agencia, nome, cpf):
        super().__init__(numConta, agencia, nome, cpf)
        self.juros = 0.0088
        self.tipo = 12

    def rotinaMensal(self):
        juros = round(self.saldo * self.juros, 2)
        print("Depositando R${} na conta {} referente aos juros mensais.".format(juros, self.numConta))
        self.deposita(juros)

class ContaCorrente(Conta):
    def __init__(self, numConta, agencia, nome, cpf):
        super().__init__(numConta, agencia, nome, cpf)
        self.taxa = 17.55
        self.tipo = 1

    def rotinaMensal(self):
        print("Descontando R${} da conta {} referente a cesta de serviços mensais.".format(self.taxa, self.numConta))
        self.saque(self.taxa)

class ContaInvestimento(Conta):
    def __init__(self, numConta, agencia, nome, cpf, investimento):
        super().__init__(numConta, agencia, nome, cpf)
        self.investimento = str(investimento).upper()
        self.investimentoA = 0.0
        self.investimentoB = 0.0
        self.investimentoC = 0.0

    def variaveisDoInvestimento(self):
        self.investimentoA = float(random.random()) + float(random.randrange(0, 1))
        self.investimentoB = random.random() + random.randrange(-2, 6)
        self.investimentoC = random.random() + random.randrange(-6, 18) 
        self.investimentoD = random.random() + random.randrange(-10, 30)
        self.investimentoE = random.random() + random.randrange(-15, 45) + random.randrange(-15, 10) + random.randrange(-15, 10) + random.randrange(-15, 1)

    def alterarInvestimento(self, novoInvestimento):
        if self.investimento != novoInvestimento:
            self.Investimento = novoInvestimento
        else:
            print("A conta já está configurada para esse investimento.")

    def rotinaMensal(self):
        investimentoAtual = 0.0
        dividendoMes = 0.0
        def formatDec(valor):
            x = round(valor,2)
            return x
        self.variaveisDoInvestimento()
        if self.investimento == "A":
            investimentoAtual = formatDec(self.investimentoA)
        elif self.investimento == "B":
            investimentoAtual = formatDec(self.investimentoB)
        elif self.investimento == "C":
            investimentoAtual = formatDec(self.investimentoC)
        elif self.investimento == "D":
            investimentoAtual = formatDec(self.investimentoD)
        elif self.investimento == "E":
            investimentoAtual = formatDec(self.investimentoE)
        else:
            print("O investimento não consta em nossa base de dados.")
            return
        
        if investimentoAtual > 0:
            dividendoMes = formatDec(self.saldo * (investimentoAtual/100))
            print("O investimento '{}' teve uma performance positiva de {}%.\Foram depositados R${} na conta {} referente aos dividendos mensais do investimento.".format(self.investimento, investimentoAtual, dividendoMes, self.numConta))
            self.deposita(dividendoMes)
        else:
            dividendoMes = round(self.saldo * (investimentoAtual/100),2)
            print("O investimento '{}' teve uma performance negativa de {}%.\nHouve um prejuizo de R${} na conta{}.".format(self.investimento, investimentoAtual, dividendoMes, self.numConta))
            self.saque(abs(dividendoMes))


contaDoJoao = ContaCorrente(3423, 345, "João Batista da Paixão", "094393205-98")
contaDoJoao.deposita(1000)

contaDaDani = ContaPoupanca(2353,345, "Daniela Alburque de Souza", "823938532-98")
contaDaDani.deposita(1000)

contaDoJulio = ContaInvestimento(3525, 345, "Julio Batista da Paixão", "094635837-98","e")
contaDoJulio.deposita(1000)

contas = [contaDaDani, contaDoJoao, contaDoJulio]

def passaMes():
    for conta in contas:
        conta.rotinaMensal()

def printContas():
    for conta in contas:
        print(conta)

def simularAno():
    def depositoMes(valor):
        conta.deposita(valor)
    saldoIniciais = {}
    for conta in contas:
        contStr = str(conta.numConta)
        saldoIniciais[contStr] = conta.saldo
    for i in range(1,13):
        print("Mês ",i)
        passaMes()
        printContas()
        for conta in contas:
            depositoMes(100)
        #time.sleep(1)
    for conta in contas:
        contStr = str(conta.numConta)
        alteracao = conta.saldo - saldoIniciais[contStr] 
        print("A conta do(a) cliente {} sofreu uma alteração de {}.\nDepositos: 12 X {}\nResultado final: {}".format(conta.nome, round(alteracao,2), 100, round((alteracao - 1200),2)))
simularAno()
