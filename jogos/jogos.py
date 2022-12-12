import adivinhacao
import forca


def Selecionar_jogo():
    opcao = int(input("Bem vindo!\n\nQual o jogo você deseja jogar?\n1 - Adivinhação do número\n2 - Forca\n\nDigite: "))
    while opcao != 1 and opcao != 2:
        opcao = int( input("Opção inválida...\nTente novamente.\n\nQual o jogo você deseja jogar?\n1 - Adivinhação do número\n2 - Forca\n\nDigite: "))
    jogo_adivinhacao = opcao == 1
    jogo_forca = opcao == 2  
    if(jogo_adivinhacao):
        adivinhacao.Jogar()
    elif(jogo_forca):
        forca.Jogar()


if (__name__ == "__main__"):
    Selecionar_jogo()
