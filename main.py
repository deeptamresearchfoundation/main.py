from os import write
import pyautogui
import time
from inflect import engine
time.sleep(2)
for x in range(375001, 375999):
    n=x
    p = engine()
    num = p.number_to_words(n)
    if(x % 2 == 0):
        ret = "true"
    else:
        ret = "false"
    pyautogui.write("else if")
    pyautogui.write("(number === ")
    pyautogui.write(str(x))
    pyautogui.write(" || number === \"")
    pyautogui.write(str(x))
    pyautogui.write("\" || number === ")
    time.sleep(0.004)
    pyautogui.write("\"" + num.replace(",", "").lower() + "\" || number === \"" + num.replace(",", "").title() +"\" || number === \"" + num.replace(",", "").upper() + "\") return " + ret + ";\n    ")
    time.sleep(0.1)
