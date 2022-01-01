# Модуль экспорта файлов Сформировать

import time
import pyautogui as pg
from MyModules.past_dates import past_dates
from MyModules.print_log import print_log
from MyModules.switch_layout import eng_layout, rus_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.config_read import *

# Константы
NAMES_LIST = NAMES_STR.split(',')  # список для всех элементов
NAMES_LIST_double = NAMES_STR_double.split(',')  # список для жлементов которые нужно дважды искать


def call_exports():
    """Функция запуска отчета Точки по дням"""
    pg.click(1000, 120)  # координаты под Win7 125% (1000, 150)


def configuring_exports():
    """Функция запуска настройки дат в Точках по дням"""
    time.sleep(0.5)
    pg.write(past_dates()[0])
    pg.press('tab')
    time.sleep(0.5)
    pg.write(past_dates()[1])
    pg.press('tab', presses=2)


def clearing_file_find():
    """Функция очистки поискового поля"""
    pg.click(350, 60)  # переход в поле поиска; координаты под вин7 150% (415, 75)
    time.sleep(0.5)
    pg.press('backspace', presses=50)


def searching_exporting(name):
    """Функция поиска контрагента через поле поиска и сохранения нужной печатной формы"""
    pg.press('pageup')
    timeout = 1  # таймаут ожидания
    time.sleep(timeout)
    rus_layout()
    typing(name)  # имя в поисковое окно
    if name in NAMES_LIST_double:
        pg.hotkey('shift', 'F3')
    pg.hotkey('shift', 'F3')  # поиск
    pg.press('enter')  # выбор клиента
    pg.press('tab')
    pg.press('enter')  # формирование форм
    time.sleep(timeout)
    pg.hotkey('ctrl', 'F4')
    time.sleep(timeout)
    pg.hotkey('ctrl', 's')
    time.sleep(timeout)
    eng_layout()
    typing(PATH_EXPORTS)
    rus_layout()
    typing(name + f'_{past_dates()[5]}')  # имя файла для сохранения
    pg.press('tab')
    pg.press('down', presses=2)  # выбор формата файла
    pg.press('enter', presses=2)  # сохранение файла
    time.sleep(timeout)
    pg.hotkey('ctrl', 'F4')  # закрытие окна формы
    time.sleep(timeout)
    pg.hotkey('ctrl', 'F4')


def cycling_exports():
    """Функция основного цикла для перебора по списку"""
    print_log("Начало выгрузки файлов 'Сформировать.xls'", line_before=True)

    length_ = 0
    length = len(NAMES_LIST)

    for i in NAMES_LIST:
        call_exports()
        configuring_exports()
        clearing_file_find()
        searching_exporting(i)
        print_log(f"Выгружено '{i}'")
        if length_ >= length:
            break
