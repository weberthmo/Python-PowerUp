
import pyautogui
import time
import pandas

link = "https://www.mercadolivre.com.br/"

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=609, y=114)
pyautogui.write("nicho madeira")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
print(tabela)