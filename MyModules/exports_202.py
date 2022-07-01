# Модуль работы с экспортом 202 формы

import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import period_for_emails
from MyModules.select_menu import selecting_menu
from MyModules.save_file_xls import saving_xls


def export_202(change_mount=False):
    """Функция экспорта файлов 202 формы"""
    print_log("Экспорт 202 формы", line_before=True)
    selecting_menu(1, 11)  # запуск обработки выгрузки 202

    if change_mount:
        # смена месяца
        pg.press('tab', presses=1, interval=0.2)
        pg.press('space')
        pg.press('tab', presses=2, interval=0.2)
    elif not change_mount:
        # без смены месяца
        pg.press('tab', presses=3, interval=0.2)

    for item in range(3):
        pg.press('space')
        pg.press('tab')
    eng_layout()
    typing(PATH_202)
    pg.press('tab')
    pg.press('enter')
    print_log("Выгрузка файлов отчета")
    time.sleep(40)
    pg.press('tab', presses=2, interval=0.2)
    pg.press('enter')
    time.sleep(5)
    print_log("Выгрузка форм по банкам в XLS")
    banks = ('ВТБ', 'Р-ИНКАС', 'ГПБ')
    for bank in banks:
        pg.hotkey('ctrl', 's')
        time.sleep(0.5)
        eng_layout()
        typing(PATH_202)
        rus_layout()
        typing(f'202 {bank} ({period_for_emails()})')
        saving_xls(f'202 {bank} ({period_for_emails()})')
