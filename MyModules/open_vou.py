# Модуль открытия ВОУ
# from MyModules.open_vou import open_last_vou

import time
import pyautogui as pg
from MyModules.select_menu import selecting_menu
from MyModules.interval_journals import interval_january


def open_last_vou(column_menu=2):
    """Функция открытия журнала последней ВОУ"""
    selecting_menu(column_menu, 5)  # журнал воу
    interval_january(long_=False)
    pg.press('end')
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(0.1)
