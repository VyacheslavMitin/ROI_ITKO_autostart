# Модуль работы с экспортом детализаций для красное и белое

import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import period_for_emails
from MyModules.save_file_xls import saving_xls
from MyModules.open_vou import open_last_vou
from MyModules.finding import working_find


TUPLE_KRASNOE_BELOE = ("Альфа Пенза", "Альфа-М", "Лабиринт-Волга")


def exports_krasnoe_beloe():
    """Функция экспорта документов для 'Красное и белое'"""
    open_last_vou(1)  # журнал ВОУ

    print_log("Выгрузка детализаций по кассе клиента 'Красное и Белое'")
    for item in TUPLE_KRASNOE_BELOE:
        working_find(item)
        pg.press('tab', presses=8, interval=0.1)
        pg.press('space')
        time.sleep(0.1)
        pg.press('down', presses=2, interval=0.1)
        time.sleep(0.1)
        pg.press('enter')
        time.sleep(4)
        pg.hotkey('ctrl', 's')
        time.sleep(0.5)
        eng_layout()
        typing(PATH_CLIENTS)
        rus_layout()
        typing(f'Детализация пересчета {item} {period_for_emails()}')
        saving_xls(f'Детализация пересчета {item} {period_for_emails()}')

