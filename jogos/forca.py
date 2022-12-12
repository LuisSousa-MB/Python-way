import random
import time

pontos_letra= 50


def Jogar():
    pontos_jogador1 = 0
    pontos_jogador2 = 0

    vez = quem_começa()
    erros = 0
    acertou = False
    enforcou = False    
    exibe_apresetacao()
    exibe_recordes()

    modo,rodada = definir_modo_de_jogo()
    palavra,tipo = gera_palavra()
    campo_de_letras = gera_campo_de_letras(palavra)
    jogador1, jogador2 = define_jogadores(modo)

    #print("O jogador 1 é {} e o 2 {}".format(jogador1,jogador2))
    print("DICA!\n",tipo.upper(),"\n")

    while(not enforcou and rodada != 0):
        time.sleep(2)
        if modo == 1:
            vez_jogador1 = 1 == 1
            vez_jogador2 = False
        else:
            vez_jogador1 = vez == True
            vez_jogador2 = vez == False
            print("\n\nRodadas restantes:",rodada)
            time.sleep(1)
        if vez_jogador1:
            print("\n{} é a sua vez!\n".format(jogador1))
        if vez_jogador2:
            print("\n{} é a sua vez!\n".format(jogador2))
        print(campo_de_letras)
        chute = define_chute()
        if (chute in palavra):
            pontos,letras = verifica_letra(palavra, chute,campo_de_letras)
            if vez_jogador1:
                print("\nExistem {} letras '{}' na palavra.\n{} marcou {} pontos.".format(letras,chute,jogador1,pontos))
                pontos_jogador1 += pontos
                print(campo_de_letras)

                time.sleep(1)
            elif vez_jogador2:
                print("\nExistem {} letras '{}' na palavra.\n{} marcou {} pontos.".format(letras,chute,jogador2,pontos))
                pontos_jogador2 += pontos
                print(campo_de_letras)

                time.sleep(1)
        else:
            vez = not vez
            if modo == 1:
                erros += 1
                desenha_forca(erros)
            print("\nNão tem a letra '{}'...\n\n".format(chute))
        if modo != 1:
            mostrar_placar(jogador1,jogador2,pontos_jogador1,pontos_jogador2)
            time.sleep(2)
        acertou = "_" not in campo_de_letras
        enforcou = erros == 7
        if(acertou):
            if modo == 2:
                print(campo_de_letras)
                print("\n\nCorreto!\nA palavra era {}\n\n".format(palavra))
                if vez_jogador1:
                    double = pontos * 2
                    print("{} marcou {} pontos por ter concluido a palavra.".format(jogador1,double))
                    pontos_jogador1 += double
                elif vez_jogador2:
                    double = pontos * 2
                    print("{} marcou {} pontos por ter concluido a palavra.".format(jogador2,double))
                    pontos_jogador2 += double
                mostrar_placar(jogador1,jogador2,pontos_jogador1,pontos_jogador2)
                time.sleep(2)
                rodada -= 1
                if rodada == 0:
                    if pontos_jogador1 > pontos_jogador2:
                        print("\n\n{}...".format(jogador1))
                        mensagem_vencedor()
                        mostrar_placar(jogador1,jogador2,pontos_jogador1,pontos_jogador2)
                    elif pontos_jogador2 > pontos_jogador1:
                        print("\n\n{}...".format(jogador2))
                        mensagem_vencedor()
                        mostrar_placar(jogador1,jogador2,pontos_jogador1,pontos_jogador2)
                    else:
                        print("Vocês mandaram muito bem!\nO placar ficou em empate!")
                        mostrar_placar(jogador1,jogador2,pontos_jogador1,pontos_jogador2)
                        resposta = input("Desejam mais uma rodada para definir um vencedor?\nDigite (S para sim ou N para não):").upper()
                        while resposta != "S" and resposta != "N":
                            resposta = input("Resposta inválida...\nMais uma rodada?\nDigite (S para sim ou N para não):").upper()
                        if resposta == "S":
                            rodada += 1
                        else:
                            print("Ok!\nFim de jogo!!!")
                            time.sleep(1)
                            print("Vocês são demais!\n UhuuUuuu!!! \o/")

                else:
                    print("\nGerando próxima palavra...")
                    time.sleep(2)
                    palavra,tipo = gera_palavra()
                    print("DICA!\n",tipo.upper(),"\n")
                    time.sleep(2)
                    campo_de_letras = gera_campo_de_letras(palavra)
            else:
                print("\n\nCorreto!\nA palavra era {}\n\n".format(palavra))
                print("Pontos: ",pontos_jogador1)
                time.sleep(2)
                print("\nGerando próxima palavra...")
                time.sleep(2)
                palavra,tipo = gera_palavra()
                print("DICA!\n",tipo.upper(),"\n")
                time.sleep(2)
                campo_de_letras = gera_campo_de_letras(palavra)
                   
        if(enforcou):
            mensagem_perdedor(palavra,pontos_jogador1,jogador1)
            break
def definir_modo_de_jogo():
    modo = int(input("\nIniciando nova partida...\nQuantos jogadores 1 ou 2?\n\nDigite:"))
    while modo != 1 and modo != 2:
        modo = int(input("\n Opção inválida...\n1 ou 2 jogadores?\n\nDigite:"))
    if modo == 2:
        rodada = int(input("Quantas rodadas vocês querem jogar?\n\nDigite:"))
        while rodada <1 or rodada > 100:
            rodada = int(input("Digite um valor entre 1 e 100 rodadas...\n\nDigite:"))
        return modo,rodada
    else:
        rodada = 1
        return modo,rodada

def define_chute():
    chute = input("Adivinhe a letra: \n").strip().upper()
    return chute
22
def verifica_letra(palavra,chute,campo_de_letras):
    index = 0
    pontos = 0
    letras = 0
    for letra in palavra:
        if (letra == chute):
            print("\nExiste a letra {} na posição {}".format(letra,index + 1))
            campo_de_letras[index] = letra
            pontos += pontos_letra
            letras += 1
        index += 1
    return pontos, letras

def mensagem_perdedor(palavra,pontos,nome):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    time.sleep(5)
    print("\n\n\n\nVocê marcou {} pontos.".format(pontos))
    if pontos != 0:
            salvar_pontuação(nome,pontos)    
            print("\nParabéns!")
def exibe_recordes():
    toplist = {}
    with open('recordes.txt', 'r') as arquivo:
        recordes = []
        for linha in arquivo:
            recordes.append(linha.strip())
    print("Os Top 5 melhores pontuadores do modo um jogador, são:\n")
    for recorde in recordes:
        index = recorde.find(":")
        nome = (recorde[:index-1])
        pontos = int(recorde[index+1:])
        if nome in toplist:
            if toplist[nome] < pontos:
                toplist[nome] = pontos
        else:
            toplist[nome]= pontos
    toplist = sorted(toplist.items(), key =     lambda kv:(kv[1], kv[0]), reverse=True)  
    i = 1
    for e in toplist:
        if i <= 5:
            print("{}º - {} pontos".format(i,e))
            i += 1
    time.sleep(4)
def salvar_pontuação(nome,pontos):
    with open('recordes.txt', 'a') as arquivo:
            # <Seu código aqui>
            dados = nome + " : " +str(pontos)
            print(dados, file=arquivo)

def mensagem_vencedor():
    print("__________________________________________________")
    print("        Parabéns!\n   *** Você venceu!!! ***")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("__________________________________________________\n\n")
   

def exibe_apresetacao():
    print("***********************************")
    print("Bem vindo ao jogo da forca!!\n")
    print("***********************************")

def gera_palavra():
    tipo = random.randrange(1,3)
    if tipo == 1:
        arquivo = open("frutas.txt","r")
        tipo = "fruta"
    elif tipo == 2:
        arquivo = open("animais.txt","r")
        tipo = "animal"
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    sorteada = random.randrange(0,len(palavras))
    palavra = (palavras[sorteada]).upper()

    return palavra,tipo

def gera_campo_de_letras(palavra):
    return ["_" for char in palavra]

def mostrar_placar(j1,j2,j1_pontos, j2_pontos):
    print("Placar\n")
    print("\n{} {} X {} {}".format(j1,j1_pontos,j2_pontos,j2))


def define_jogadores(modo):
    if modo != 1:
        jogador1 = input("Informe o nome do primeiro jogador: ")
        jogador2 = input("Informe o nome do segundo jogador: ")
        return jogador1,jogador2
    else:
        jogador1 = input("Informe o nome do jogador: ")
        jogador2 = "Ghost"
        return jogador1,jogador2

def quem_começa():
    sorte = random.randrange(1,3)
    if sorte == 1:
        vez = True
    else:
        vez = False
    return vez

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
if (__name__ == "__main__"):
    Jogar()
