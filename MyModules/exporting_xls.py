import time
import os
import configparser
import pyautogui as pg
from MyModules.past_dates import past_dates
from MyModules.print_log import print_log
from MyModules.switch_layout import eng_layout, rus_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing

cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')
ITKO_DIR = cfg.get('PATHS', 'dir_itko')
EXPORT_DIR = cfg.get('PATHS', 'dir_exports')
EXPORT_PATH = os.path.join(ITKO_DIR, EXPORT_DIR)
NAMES_STR = cfg.get('NAMES', 'points')
NAMES_STR_double = cfg.get('NAMES', 'points_double')

NAMES_LIST = NAMES_STR.split(',')  # список для всех элементов
NAMES_LIST_double = NAMES_STR_double.split(',')  # список для жлементов которые нужно дважды искать


def call_exports():
    """Функция запуска отчета Точки по дням"""
    pg.click(1000, 120)  # координаты под вин7 150% (1000, 150)


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
    pg.press('backspace', presses=30)


def searching_exporting(name):
    """Функция поиска контрагента через поле поиска и сохранения нужной печатной формы"""
    pg.press('pageup')
    timeout = 1  # таймаут ожидания
    time.sleep(timeout)
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
    text = EXPORT_PATH + name + f'_{past_dates()[5]}'
    print(text)
    # input('')
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
    rus_layout()
    # pg.hotkey('alt', 'shift')  # переключение языка
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
