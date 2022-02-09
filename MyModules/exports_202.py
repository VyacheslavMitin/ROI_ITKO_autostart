# Модуль с экспортами 014, ВСКК, ВОУ

import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import period_for_emails
from MyModules.select_menu import selecting_menu


def export_202():
    """Функция экспорта файлов 202 формы"""
    print_log("Экспорт 202 формы", line_before=True)
    selecting_menu(1, 11)  # запуск обработки выгрузки 202
    # pg.press('tab', presses=1, interval=0.2)
    # pg.press('space')
    # pg.press('tab', presses=2, interval=0.2)
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
    banks = ('ВТБ', 'Р-ИНКАС', 'ГПБ', 'ВБРР')
    for bank in banks:
        pg.hotkey('ctrl', 's')
        time.sleep(0.5)
        eng_layout()
        typing(PATH_202)
        rus_layout()
        typing(f'202 {bank} ({period_for_emails()})')
        pg.press('tab')
        pg.press('down', presses=2)  # выбор формата файла
        pg.press('enter', presses=2)  # сохранение файла
        time.sleep(0.5)
        pg.hotkey('ctrl', 'F4')  # закрытие окна формы
