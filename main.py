# Модуль работы с ИТКО (выгрузка отчетов "сформировать")

# ИМПОРТЫ
import os

import pyautogui
import pyautogui as pg
import time
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.print_log import print_log
from MyModules.quit_itko import quit_1c
import subprocess
import configparser

# КОНСТАНТЫ
cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')
ITKO_DIR = cfg.get('PATHS', 'dir_itko')
ITKO_BIN = cfg.get('PATHS', 'itko_bin')
PATH_014 = os.path.join(ITKO_DIR, cfg.get('PATHS', 'dir_014'))
PATH_VSKK = os.path.join(ITKO_DIR, cfg.get('PATHS', 'dir_vskk'))


# ФУНКЦИИ
def welcoming(name_='ИТКО', author_='Вячеслав Митин', version_='5'):
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


def start_itko(point='buh', mode='ENTERPRISE'):
    """Функция запуска 1С 7 ИТКО"""
    print_log(f"Запуск ИТКО в  режиме {mode}")

    subprocess.Popen([
        ITKO_BIN,
        mode
    ])

    time.sleep(1)
    pg.press('tab', presses=2)
    pg.press('home')  # выбор первой базы в списке баз
    pg.press('enter')
    pg.hotkey('shift', 'tab')
    pg.press('home')  # выбор администратора для точки отсчета
    if point == 'buh':  # выбор бухгалтера
        print_log("Выбор Бухгалтера для входа")
        pg.press('down', presses=7)
        pg.press('enter', presses=4, interval=0.5)
        pg.press('tab', presses=2, interval=0.5)

    elif point == 'adm':  # оставить администратора
        print_log("Выбор Администратора для входа")

    pg.press('enter')

    if mode == 'CONFIG':
        print_log("Открытие окна для загрузки базы", line_before=True)
        pg.press('alt')
        pg.press('right', presses=3)
        pg.press('down', presses=5)
        pg.press('enter')
        pg.press('tab')
        pg.press('enter')
        from MyModules.typing_unicode_str import typing_unicode_str
        typing_unicode_str(ITKO_DIR)
        pg.press('enter')


def success_window_alert():
    time.sleep(1)
    pg.alert("Автоматизация завершена", title="Завершено")
    print_log("Автоматизация завершена", line_before=True)


def change_datetime():
    file = 'change_datetime.lnk'
    import os
    os.system(file)


def preparation_vou():
    pg.click(750, 85)
    pg.click(650, 85)


def export_014():
    from MyModules.past_dates import past_dates
    pg.click(50, 120)
    pg.write(past_dates()[0])
    pg.press('tab')
    pg.write(past_dates()[1])
    pg.press('tab', presses=2)
    typing(PATH_014 + f'014_{past_dates()[5]}.xml')
    time.sleep(1)
    pg.press('tab')
    pg.press('enter')
    time.sleep(30)


def export_vskk():
    from MyModules.past_dates import past_dates
    pg.click(250, 120)
    pg.write(past_dates()[0])
    pg.press('tab')
    pg.write(past_dates()[1])
    pg.press('tab', presses=2)


def pyautogui_menu() -> str:
    """Функция МЕНЮ"""
    print_log("Запуск меню")

    menu_points = {
        0: 'Загрузка базы ИТКО',
        1: 'Старт ИТКО Бухгалтером',
        2: 'Старт ИТКО Администратором',
        3: "Подготовка к формированию ВОУ",
        4: "Файлы 'Сформировать.xls'",
        5: "Выгрузка '014'",
        6: "Выгрузка 'ВСКК'",
        9: "Поменять системные дату/время"
    }

    return pg.prompt(text=f"""
    Необходимо выбрать пункт меню:
    
    0: {menu_points.get(0)}
    =========================
    1: {menu_points.get(1)}
    2: {menu_points.get(2)}
    =========================
    3: {menu_points.get(3)}
    =========================
    4: {menu_points.get(4)}
    5: {menu_points.get(5)}
    6: {menu_points.get(6)}
    =========================
    9: {menu_points.get(9)}
    """, title='МЕНЮ АВТОМАТИЗАЦИИ ИТКО', default='1')


if __name__ == '__main__':
    welcoming()

    select = pyautogui_menu()
    if select == '0':
        start_itko(point='adm', mode='CONFIG')

    elif select == '1':
        start_itko()

    elif select == '2':
        start_itko(point='adm')

    elif select == '3':
        change_datetime()
        start_itko()
        preparation_vou()

    elif select == '4':
        from MyModules.exporting_xls import *
        start_itko(point='buh')
        cleaning_export_dir()
        cycling_exports()
        make_separator()
        quit_1c()

    elif select == '5':
        start_itko(point='buh')
        export_014()
        quit_1c()

    elif select == '6':
        start_itko(point='buh')
        export_vskk()

    elif select == '9':
        change_datetime()

    success_window_alert()
