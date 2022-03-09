# Модуль экспорта файлов Сформировать

import time
import pyautogui as pg
from MyModules.config_read import *
from MyModules.finding import working_find
from MyModules.past_dates import past_dates, period_for_emails
from MyModules.print_log import print_log
from MyModules.switch_layout import eng_layout, rus_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.select_menu import selecting_menu
from MyModules.save_file_xls import saving_xls

# Константы
NAMES_LIST = NAMES_STR.split(',')  # список для всех элементов
NAMES_LIST_double = NAMES_STR_double.split(',')  # список для элементов которые нужно дважды искать


def call_sformirovat():
    """Функция запуска и настройки отчета Точки по дням"""
    selecting_menu(1, 1)  # запуск обработки по дням
    time.sleep(0.5)
    pg.write(past_dates()[0])
    pg.press('tab')
    time.sleep(0.5)
    pg.write(past_dates()[1])
    pg.press('tab', presses=2)


def exporting(name):
    """Функция работы с экспортом"""
    if name in NAMES_LIST_double:
        time.sleep(0.5)
        pg.hotkey('shift', 'F3')
    pg.press('enter')  # выбор клиента
    time.sleep(0.5)
    pg.press('tab')
    pg.press('enter')  # формирование форм
    time.sleep(1)
    pg.hotkey('ctrl', 'F4')
    pg.hotkey('ctrl', 's')
    eng_layout()
    typing(PATH_SFORMIROVAT)
    rus_layout()
    if name == 'Сеть автомат':
        typing('САПВ' + f' ({period_for_emails()})')  # имя файла для сохранения
    else:
        typing(name + f' ({period_for_emails()})')  # имя файла для сохранения
    saving_xls(name + f' ({period_for_emails()})')
    pg.hotkey('ctrl', 'F4')


def cycling_exports():
    """Функция основного цикла для перебора по списку"""
    print_log("Начало выгрузки файлов 'Сформировать.xls'", line_before=True)

    i = 0
    for item in NAMES_LIST:
        call_sformirovat()
        working_find(item)
        exporting(item)
        i += 1
    print_log(f'Всего {i} файлов выгружено')


def exports_rzd():
    """Функция основного цикла для перебора по списку"""
    print_log("Начало выгрузки файлов 'Сформировать.xls'", line_before=True)

    name_ = "РЖД"

    call_sformirovat()
    working_find(name_)
    exporting(name_)
