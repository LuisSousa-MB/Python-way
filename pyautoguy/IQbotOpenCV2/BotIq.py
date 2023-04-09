from numpy import  *
import pyautogui
import time

import cv2
import os

def AltTab():
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

# configurar as variáveis
intervalo_tempo = 120
ativo = "EUR/USD"
limiteMaxY = 114
limiteMinY = 18
operando = True
button_buy = "img/buttons/buy.png"
button_sell= "img/buttons/sell.png"
button_nova= "img/buttons/nova.png"
pos_buy = 107
pos_sell = 24

AltTab()

time.sleep(1)

def mark_pattern(y ,x , output_image):
    image_finished = cv2.circle(output_image, (x,y),3,(0,0,255), -1 )
    return image_finished

def CheckLinha(img, x, y):
    linha = False
    for i in range(y+1, img.shape[0]):
        if img[i, x] == 255:
            linha = True
            img[i-2,x] = 0
            img[i-1,x] = 0
            img[i, x] = 0 
    if not linha:
        medias.append(y)
    #img_linha = cv2.circle(img, (x, i), 3,(111,111,122), -1 )

    cv2.imwrite("/home/lsousa/python/Projects/pyautoguy/img/linha"+ str(markPaint)+".png", img)

def PrecoMedio():
    soma = 0
    for y in medias:
        soma += y
    media = soma/(len(medias))
    print("A média em y é: ", round(media))

    return round(media)
# usar o pyautogui para clicar em elementos da interface da plataforma de negociação
# para configurar o gráfico
#pyautogui.click(x=100, y=200)  # clicar em um botão para selecionar o intervalo de tempo
#pyautogui.write(intervalo_tempo)  # digitar o intervalo de tempo
#pyautogui.click(x=300, y=400)  # clicar em um botão para selecionar o ativo
#pyautogui.write(ativo)  # digitar o ativo

while operando: 
    # capturar a imagem do gráfico
    #c pyautogui.screenshot(region=(125, 600, 1235, 730))p

    image = pyautogui.screenshot(region=(325,900, 950, 130))
    image.save("img/TESTEbot.PNG")
    
    time.sleep(1)
    # processar a imagem para extrair informações úteis
    # por exemplo, você pode usar o OpenCV para detectar padrões de gráfico comuns
    # ou calcular médias móveis
    
    imageCV2 =  cv2.imread("img/TESTEbot.PNG")
    imageCV2Cinza = cv2.cvtColor(imageCV2, cv2.COLOR_BGR2GRAY)
    ImageCV2Tratada = cv2.threshold(imageCV2Cinza, 150, 255, cv2.THRESH_BINARY)[1]
    
    #imageCV2Bordas = cv2.Canny(ImageCV2Tratada, 50, 200)
    
    i = 1
    cv2.imwrite("/home/lsousa/python/Projects/pyautoguy/img/xxxxxxxxxx.png", ImageCV2Tratada)

    # percorrer a imagem pixel a pixel
    final_x = -1  # posição final da linha no eixo x
    final_y = -1
    markPaint = 0
    menor_y = 0
    maior_y = 300
    menor_x = 0
    maior_x = 0
    medias = []

    for y in range(ImageCV2Tratada.shape[0]):
        for x in range(ImageCV2Tratada.shape[1]):
            # verificar se o pixel atual é branco
            #if ImageCV2Tratada[y,x] != 0 :
           #     print("x - {}, y - {}".format(x,y), "Pixel:", ImageCV2Tratada[y,x])
            if ImageCV2Tratada[y, x] == 255:
               #print(ImageCV2Tratada[y,x]
                CheckLinha(ImageCV2Tratada, x, y)
                
                if y > menor_y and y < limiteMaxY:
                    menor_y = y
                    menor_x = x
                if y < maior_y and menor_y > limiteMinY:
                    maior_y = y
                    maior_x = x
                if x > final_x and y >= limiteMinY and y <= limiteMaxY:
                    final_x = x  # armazenar a posição no eixo x
                    final_y = y
    # verificar a posição final da linha no eixo x
    if final_x == -1:
        print("Não foi encontrada nenhuma linha branca na imagem")
    else:
        #print("A posição final da linha no eixo x é", final_x)
        print("A Menor posição y foi", menor_y)
        print("A Maior posição y foi", maior_y)
        print("A posição final da linha no eixo y é", final_y)        
        media = PrecoMedio()

        image_finished = cv2.circle(ImageCV2Tratada, (final_x, final_y), 3,(111,111,122), -1 )

        cv2.imwrite("/home/lsousa/python/Projects/pyautoguy/img/finalposition"+ str(markPaint)+".png", image_finished)
   
    
    menorYImage = cv2.circle(ImageCV2Tratada, (menor_x, menor_y), 5,(200,0,200), -1 )
    cv2.imwrite("/home/lsousa/python/Projects/pyautoguy/img/menorY"+ str(markPaint)+".png", menorYImage)

    maiorYImage = cv2.circle(ImageCV2Tratada, (maior_x, maior_y), 5,(200,0,200), -1 )
    cv2.imwrite("/home/lsousa/python/Projects/pyautoguy/img/maiorY"+ str(markPaint)+".png", maiorYImage)

    if final_y > pos_buy and final_y < limiteMaxY:
        pyautogui.click(1881, 245)
        print("Comprar em y =", final_y)
        pyautogui.click(button_buy)
        pyautogui.moveTo(1781, 245)
        AltTab()
        time.sleep(intervalo_tempo)
        pyautogui.click(button_nova)
        time.sleep(1)
        AltTab()
    elif final_y < pos_sell and final_y > limiteMinY:
        pyautogui.click(1881, 245)
        print("Vender em y =", final_y )
        pyautogui.click(button_sell)
        pyautogui.moveTo(1781, 245)
        AltTab()
        time.sleep(intervalo_tempo)
        pyautogui.click(button_nova)
        time.sleep(1)
        AltTab()
    elif media < menor_y and final_y >= (media + 42):
        pyautogui.click(1881, 245)
        print("Comprar por media em y =", final_y)
        pyautogui.click(button_buy)
        pyautogui.moveTo(1781, 245)
        AltTab()
        time.sleep(intervalo_tempo)
        pyautogui.click(button_nova)
        time.sleep(1)
        AltTab()
    elif media > maior_y and final_y <= (media - 42):
        pyautogui.click(1881, 245)
        print("Vender por media em y =", final_y)
        pyautogui.click(button_sell)
        pyautogui.moveTo(1781, 245)
        AltTab()
        time.sleep(intervalo_tempo)
        pyautogui.click(button_nova)
        time.sleep(1)
        AltTab()
    time.sleep(3)
    #operando = not operando