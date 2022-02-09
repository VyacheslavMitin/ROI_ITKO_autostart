# Модуль с экспортами 014, ВСКК, ВОУ

import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import past_dates
from MyModules.select_menu import selecting_menu


def export_vskk():
    """Функция экспорта файла ВСКК"""
    print_log("Экспорт ВСКК", line_before=True)
    selecting_menu(1, 10)
    pg.press('tab', presses=8, interval=0.2)
    pg.press('esc', interval=0.2)
    pg.press('tab')
    pg.write(past_dates()[0])
    pg.press('tab')
    pg.write(past_dates()[1])
    pg.press('tab', presses=2, interval=0.2)
    eng_layout()
    typing(PATH_VSKK)
    rus_layout()
    typing(f'ВСКК ОКО ALL {past_dates()[3]} {past_dates()[6]}')
    pg.press('tab')
    pg.press('enter')
    time.sleep(5)
    pg.press('enter')
