# Модуль для поиска координат и цветов на экране

import pyautogui
import time


while True:
    time.sleep(0.2)
    a = pyautogui.position()
    # b = pyautogui.pixel(*pyautogui.position())
    print(a)
