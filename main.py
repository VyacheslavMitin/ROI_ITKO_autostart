# Модуль работы с ИТКО (выгрузка отчетов "сформировать")
# pip install pyautogui
# Win7 разрешение 2560 х 1440, 125% маштаб
# Win10 разрешение 2560 х 1440, 100% маштаб

# ИМПОРТЫ
import os
import pyautogui as pg
import subprocess
import configparser
import time
import glob
from MyModules.past_dates import past_dates
from MyModules.typing_unicode_str import typing_unicode_str as typing


# КОНСТАНТЫ
cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')
EXPORT_DIR = cfg.get('PATHS', 'dir')
ITKO_BIN = cfg.get('PATHS', 'itko')
NAME_0 = cfg.get('NAMES', 'ашан')
NAME_1 = cfg.get('NAMES', 'РТК')
NAME_2 = cfg.get('NAMES', 'электротехмонтаж')
NAME_3 = cfg.get('NAMES', 'автопитер')
NAME_4 = cfg.get('NAMES', 'ситилинк')
NAME_5 = cfg.get('NAMES', 'скартел')
NAME_6 = cfg.get('NAMES', 'вымпелком')
NAME_7 = cfg.get('NAMES', 'мегафон')
NAME_8 = cfg.get('NAMES', 'мэлон')
NAME_9 = cfg.get('NAMES', 'сапв')
NAME_10 = cfg.get('NAMES', 'вкусвилл')

NAMES = (  # кортеж с контрагентами
    NAME_0,
    NAME_1,
    NAME_2,
    NAME_3,
    NAME_4,
    NAME_5,
    NAME_6,
    NAME_7,
    NAME_8,
    NAME_9,
    NAME_10
)


# ФУНКЦИИ
def welcoming(name_='ИТКО', author_='Вячеслав Митин', version_='5'):
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


# def make_dir() -> str:
#     """Функция создания каталога для файлов"""
#     path_ = export_dir + past_dates()[1]
#     os.makedirs(path_, exist_ok=True)
#     print(path_)
#     return path_


def cleaning_export_dir():
    """Функция удаления файлов эксель в каталоге экспорта"""
    for files in glob.glob(EXPORT_DIR + f'*_{past_dates()[5]}.xls'):
        os.remove(files)
    time.sleep(0.5)


def start_itko_bookkeeper():
    """Функция запуска 1С 7 ИТКО"""
    subprocess.Popen([
        ITKO_BIN
    ])

    time.sleep(2)
    pg.press('enter', presses=4, interval=0.5)
    pg.press('tab', presses=2, interval=0.5)
    pg.press('enter')


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
    pg.write(name)  # имя в поисковое окно
    if name == NAME_0 or name == NAME_1 or name == NAME_2:  # дополнительный поиск 'Ашан', 'РТК' и 'электротехмонтаж'
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
    pg.write(name.lower() + f'_{past_dates()[5]}')  # имя файла для сохранения
    pg.press('tab')
    pg.press('down', presses=2)  # выбор формата файла
    pg.press('enter', presses=2)  # сохранение файла
    time.sleep(timeout)
    pg.hotkey('ctrl', 'F4')  # закрытие окна формы
    time.sleep(timeout)
    pg.hotkey('ctrl', 'F4')


def make_separator(separator='---------'):
    """Функция создания сепаратора для проводника"""
    path_ = os.path.normpath(EXPORT_DIR)  # переход в папку
    os.chdir(path_)
    with open(separator + past_dates()[1] + separator, 'tw'):  # создание пустого файла как разделителя
        pass


def cycling_exports():
    """Функция основного цикла для перебора по списку"""
    pg.hotkey('alt', 'shift')  # переключение языка
    lenght_ = 0
    lenght = len(NAMES)

    for i in NAMES:
        call_exports()
        configuring_exports()
        clearing_file_find()
        searching_exporting(i)
        print(f"Выгружено '{i}'")
        if lenght_ >= lenght:
            break


def quit_1c(name_='+Сформировать'):
    """Функция выхода из 1С и запуска проводника"""
    pg.hotkey('alt', 'F4')  # выход из кассы пересчета

    if name_ in pg.getAllTitles():
        list__ = []
        for i in pg.getAllTitles():
            if i == name_:
                list__.append(i)
        for item in enumerate(list__):
            pg.getWindowsWithTitle(item[1])[item[0]].close()

    os.system(f'explorer.exe {os.path.normpath(EXPORT_DIR)}')  # запуск

    print('\nВыход!')
    time.sleep(1)
    pg.alert("Работа по выгрузке окончена!", title="Файлы выгружены")


def pyautogui_menu() -> str:
    """Функция МЕНЮ"""
    menu_points = {
        0: 'Загрузка базы ИТКО',
        1: 'Старт ИТКО',
        2: "Файлы 'Сформировать.xls'",
        3: "Подготовка к формированию ВОУ",
    }

    return pg.prompt(text=f"""
    Необходимо выбрать пункт меню:
    
    0: {menu_points.get(0)}
    1: {menu_points.get(1)}
    2: {menu_points.get(2)}
    3: {menu_points.get(3)}
    """, title='МЕНЮ АВТОМАТИЗАЦИИ ИТКО', default='1')


if __name__ == '__main__':
    welcoming()
    select = pyautogui_menu()
    if select == '0':
        pass
    elif select == '1':
        start_itko_bookkeeper()
    elif select == '2':
        start_itko_bookkeeper()
        cleaning_export_dir()
        cycling_exports()
        make_separator()
        quit_1c()
    elif select == '3':
        pass
