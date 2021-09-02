# Модуль работы с ИТКО
# pip install pyautogui

import pyautogui as pg
import subprocess
import configparser
import time

name_ = 'ИТКО'
author_ = 'Вячеслав Митин'
version_ = '0.1'

ITKO_BIN = 'C:/1Cv77/BIN/1cv7.exe'

cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')  # чтение файла settings_common.ini в папке модуля
name1 = cfg.get('NAMES', 'РТК')  # РТК


# Функции
def welcoming(name_, author_, version_):
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'")
    print()


def start_itko():
    starting = subprocess.Popen([
        ITKO_BIN
    ])

    time.sleep(2)
    pg.press('enter', presses=4, interval=1)
    pg.press('tab', presses=2, interval=1)
    pg.press('enter')


def starting_exports():
    pg.click(1000, 150)


def configuring_exports():
    pg.press('tab', presses=2, interval=0.5)
    pg.press('enter')


#welcoming()
start_itko()
starting_exports()
