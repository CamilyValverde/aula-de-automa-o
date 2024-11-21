import pyautogui
import time

time.sleep(3)
print(pyautogui.position())

print(pyautogui.click(x=724, y=455.size))

pyautogui.write("pinterest")
pyautogui.press("enter")

pyautogui.moveTo(x=329, y=355, duration=1)
pyautogui.click(x=329, y=355)

pyautogui.moveTo(x=1752, y=176, duration=1)
pyautogui.click(x=1752, y=176)

pyautogui.write("valverdecamily@gmail.com")
pyautogui.click(x=886, y=536)
pyautogui.write("magalhaes")
pyautogui.press("enter")

pyautogui.moveTo(x=684, y=182, duration=2)
pyautogui.click(x=684, y=182, duration= 11)
pyautogui.write("outfits aestheric")
pyautogui.press("enter")