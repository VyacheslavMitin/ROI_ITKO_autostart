# Модуль работы с экспортом 014

import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import past_dates
from MyModules.select_menu import selecting_menu


def export_014():
    """Функция экспорта файла 014"""
    print_log("Экспорт 014", line_before=True)
    selecting_menu(1, 9)
    pg.write(past_dates()[0])
    pg.press('tab')
    pg.write(past_dates()[1])
    pg.press('tab', presses=2)
    eng_layout()
    typing(PATH_014)
    rus_layout()
    from MyModules.past_dates import period_for_emails
    typing(f'Выгрузка 014 ({period_for_emails()})')
    eng_layout()
    typing(f'.xml')
    time.sleep(1)
    pg.press('tab')
    pg.press('enter')
    time.sleep(30)
