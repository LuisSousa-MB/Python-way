import pyautogui

while True:
    # Obtém a posição atual do mouse
    x, y = pyautogui.position()

    # Exibe a posição do mouse
    print(f'A posição atual do mouse é ({x}, {y})')
