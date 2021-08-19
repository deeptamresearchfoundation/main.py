import pyautogui
import time
from inflect import engine
time.sleep(2)
for x in range(375001, 395000):
    n=x
    p = engine()
    num = p.number_to_words(n)
    if(x % 2 == 0):
        ret = "true"
    else:
        ret = "false"
    pyautogui.write("else if ( number === " + str(x) + " || number === \"" + str(x) + "\"" + " || number === \"" + num.replace(",", "").lower() + "\" || number === \"" + num.replace(",", "").title() +"\" || number === \"" + num.replace(",", "").upper() + "\") return " + ret + ";\n")
    time.sleep(1)