# Модуль для поиска координат и цветов на экране

import pyautogui as pg
import time


while True:
    time.sleep(0.2)
    coordinates = pg.position()
    # rgb = pg.pixel(*pg.position())
    print(coordinates)
