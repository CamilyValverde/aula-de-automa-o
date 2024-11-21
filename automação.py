#automação com pyautogui
import pyautogui
import time

#para não perder o controle da automação
pyautogui.FAILSAFE = True

#pausa geral de 0.3 segundos (300 milisegundos)
pyautogui.PAUSE =  0.3

#espera um tempo para rodar
time.sleep(5)

#pegar posição do mouse
#print(pyautogui.position())


#pegar o tamanho da tela/resolução
#print(pyautogui.size())


#clicar com mouse
#pyautogui.click(x=321, y=361)


#clicar com botão direito do mouse
#pyautogui.click(x=321 , y=361, button="right")


#dois clicks no mouse
#pyautogui.click(x=321, y=361, clicks="2")


#mover o mouse
#pyautogui.moveTo(x=663, y=223, duration=2)

#pyautogui.click(x=1252, y=313)

#pyautogui.scroll(-1350)

#pyautogui.click(923, y=990)



#funções do teclado
pyautogui.press("win")

#para escrever
pyautogui.write("Clima")
pyautogui.press("enter")

#para pressionar duas teclas
pyautogui.hotkey("ctrl" , "v")
