import glob
import time
import os
import configparser
import pyautogui as pg
from MyModules.past_dates import past_dates
from MyModules.print_log import print_log
from MyModules.typing_unicode_str import typing_unicode_str as typing


EXPORT_PATH = os.path.join(ITKO_DIR, EXPORT_DIR)
NAMES_STR = cfg.get('NAMES', 'points')
NAMES_STR_double = cfg.get('NAMES', 'points_double')

NAMES_LIST = NAMES_STR.split(',')  # список для всех элементов
NAMES_LIST_double = NAMES_STR_double.split(',')  # список для жлементов которые нужно дважды искать


# def make_dir() -> str:
#     """Функция создания каталога для файлов"""
#     path_ = export_dir + past_dates()[1]
#     os.makedirs(path_, exist_ok=True)
#     print(path_)
#     return path_


def cleaning_export_dir():
    """Функция удаления файлов эксель в каталоге экспорта"""
    print_log("Очистка каталога экспорта")

    for files in glob.glob(EXPORT_PATH + f'*_{past_dates()[5]}.xls'):
        os.remove(files)
    time.sleep(0.5)


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
    typing(name + f'_{past_dates()[5]}')  # имя файла для сохранения
    pg.press('tab')
    pg.press('down', presses=2)  # выбор формата файла
    pg.press('enter', presses=2)  # сохранение файла
    time.sleep(timeout)
    pg.hotkey('ctrl', 'F4')  # закрытие окна формы
    time.sleep(timeout)
    pg.hotkey('ctrl', 'F4')
cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')
ITKO_DIR = cfg.get('PATHS', 'dir_itko')
EXPORT_DIR = cfg.get('PATHS', 'dir_exports')

def make_separator(separator='---------'):
    """Функция создания сепаратора для проводника"""
    path_ = os.path.normpath(EXPORT_PATH)  # переход в папку
    os.chdir(path_)
    with open(separator + past_dates()[1] + separator, 'tw'):  # создание пустого файла как разделителя
        pass


def cycling_exports():
    """Функция основного цикла для перебора по списку"""
    print_log("Начало выгрузки файлов 'Сформировать.xls'", line_before=True)
    pg.hotkey('alt', 'shift')  # переключение языка
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

