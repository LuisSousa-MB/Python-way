import random
import time

def Jogar():

    print("***********************************")
    print("Bem vindo ao jogo de adivinhação!\n")
    print("***********************************")

    jogador1 = input("Informe o nome do primeiro jogador: ")
    jogador2 = input("Informe o nome do segundo jogador: ")
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    jogador_atual = ""
    pontos_rodada = 100


    """ Conditions """
    vez = False
    print("é ", vez == True)
    vez_jogador1 = False
    vez_jogador2 = False
    fim = False
    secret_number = random.randint(1,61)
    str_number = 0
    pontos_vencer = 200


    while not fim:
        print("\n")
        vez = not vez
        vez_jogador1 = vez == True
        vez_jogador2 = vez == False
       # print("\nValendo {} pontos!\n".format(pontos_rodada))
        if vez_jogador1:
            print(jogador1," é a sua vez!\n")
            jogador_atual = jogador1

        elif vez_jogador2:
            print(jogador2," é a sua vez!\n")
            jogador_atual = jogador2

        time.sleep(1)
        str_number = input("\nDigite o seu chute: ")
        number = int(str_number)
        if (number < 1 or number > 60):
            print("Você deve escolher um número entre 1 e 60!")
            vez = not vez
            continue
        print("\n\nVocê chutou o número ",number,".")
        for i in range(1,4):
            print("...",i)
            time.sleep(1)
        acertou = number == secret_number
        if acertou:
            print("\n")
            print("***********************************")
            print(jogador_atual,"você acertou!\nParabéns!!!")
            print("***********************************")
            if jogador_atual == jogador1:
                pontos_jogador1 = pontos_jogador1 + pontos_rodada
            else:
                pontos_jogador2 = pontos_jogador2 + pontos_rodada
            secret_number = random.randint(1,60)
            pontos_rodada = 100
        else:
            print("____________________________________")
            print("\n\nQue pena...\nVocê errou.\n\n")
            pontos_rodada = pontos_rodada - abs(secret_number - number)
            maior = number < secret_number
            menor = number > secret_number
            if maior:
                print("O número é maior que ",number,"\n")
            elif menor:
                print("O número é menor que ",number,"\n")

            time.sleep(2)
        jogador1_venceu = pontos_jogador1 >= pontos_vencer
        jogador2_venceu = pontos_jogador2 >= pontos_vencer  
        if jogador1_venceu:
            print("*****  ",jogador1," Venceu!  *****\n******  Parabéns  ******\n\n")
            fim = True
            print("____________________________________")
            print("O placar final foi:\n",jogador1," ",pontos_jogador1," X ",pontos_jogador2," ",jogador2)
            break

        if jogador2_venceu:
            print("*****  ",jogador2," Venceu!  *****\n        Parabéns\n\n")
            fim = True
            print("____________________________________")

            print("O placar final foi:\n",jogador1," ",pontos_jogador1," X ",pontos_jogador2," ",jogador2)
            break

        print("O placar atual é:\n\n*** ",jogador1," ",pontos_jogador1," X ",pontos_jogador2," ",jogador2," ***")


if (__name__ == "__main__"):
    Jogar()

