import pyautogui as pag
import pyperclip as ppc
import time
import random
# pag.click(100,100) # (optional) Click on tab or anything else you want, how many times you want
# pag.click(200,200) # Click where text will be
def autowrite(file):
    time.sleep(1)
    pag.PAUSE=0.0
    for x in file:
        ppc.copy(x)
        time.sleep(random.randint(25,75)/3000) # Increase or decrease according to your setup and the time you want it to last
        pag.hotkey('ctrl','v')
        time.sleep(random.randint(25,75)/3000) # same
        if random.random()<0.2:
            time.sleep(0.06)
file=open("filetowrite.txt", "r")
autowrite(file.read())
file.close()