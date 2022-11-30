#=====================================================#

# Bot to write clipboard text

# The intention of the code is seem the max with a human
# made to circumvent sites where it is not possible to use the 'ctrl + V' function


# How to use?
# 1 - Copy the text
# 2 - Paste the text on archive 'text.txt'
# 3 - Execute the code, click on the input in question and wait 10 seconds for start the writing

#=====================================================#

import os
import pyautogui
from time import sleep

# Reading the txt
rd_txt = open('text.txt', 'r', encoding="utf8")

sleep(10)

# Writing line per line
for line in rd_txt:
    pyautogui.typewrite(line, interval=0.1)

