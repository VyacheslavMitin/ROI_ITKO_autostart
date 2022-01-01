# Модуль переключения раскладок
import pyautogui as pg
import time


def eng_layout():
    pg.hotkey('ctrl', '8')
    time.sleep(0.5)


def rus_layout():
    pg.hotkey('ctrl', '9')
    time.sleep(0.5)
