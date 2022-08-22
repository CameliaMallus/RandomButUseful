import pyautogui as pag
import pyperclip as ppc
import time
pag.click(240,50)
pag.click(1750,74)
def autowrite(file):
    time.sleep(1.5)
    pag.PAUSE=0.0
    for x in file:
        ppc.copy(x)
        time.sleep(0.00001)
        pag.hotkey('ctrl','v')
        time.sleep(0.00001)
file=open("file.txt", "r")
autowrite(file.read())
file.close()