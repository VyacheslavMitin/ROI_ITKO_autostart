# Модуль работы с ИТКО (выгрузка отчетов "сформировать")

# ИМПОРТЫ
import pyautogui as pg
import time
from MyModules.print_log import print_log
import subprocess
import configparser

# КОНСТАНТЫ
cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')
ITKO_BIN = cfg.get('PATHS', 'itko_bin')


# ФУНКЦИИ
def welcoming(name_='ИТКО', author_='Вячеслав Митин', version_='5'):
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


def start_itko(point='buh'):
    """Функция запуска 1С 7 ИТКО"""
    print_log("Запуск ИТКО")

    subprocess.Popen([
        ITKO_BIN
    ])

    time.sleep(1)
    pg.press('tab', presses=2)
    pg.press('home')  # выбор первой базы в списке баз
    pg.press('enter')
    pg.press('home')  # выбор администратора для точки отсчета

    if point == 'buh':  # выбор бухгалтера
        print_log("Выбор Бухгалтера для входа")
        pg.press('down', presses=7)
    elif point == 'adm':  # оставить администратора
        print_log("Выбор Администратора для входа")

    pg.press('enter', presses=4, interval=0.5)
    pg.press('tab', presses=2, interval=0.5)
    pg.press('enter')


def success_window_alert():
    time.sleep(1)
    pg.alert("Автоматизация завершена", title="Завершено")
    print_log("Автоматизация завершена", line_before=True)


def pyautogui_menu() -> str:
    """Функция МЕНЮ"""
    print_log("Запуск меню")

    menu_points = {
        0: 'Загрузка базы ИТКО',
        1: 'Старт ИТКО Бухгалтером',
        2: "Файлы 'Сформировать.xls'",
        3: "Подготовка к формированию ВОУ",
        4: 'Старт ИТКО Администратором',
    }

    return pg.prompt(text=f"""
    Необходимо выбрать пункт меню:
    
    0: {menu_points.get(0)}
    1: {menu_points.get(1)}
    2: {menu_points.get(2)}
    3: {menu_points.get(3)}
    4: {menu_points.get(4)}

    """, title='МЕНЮ АВТОМАТИЗАЦИИ ИТКО', default='1')


if __name__ == '__main__':
    welcoming()

    select = pyautogui_menu()
    if select == '0':
        pass

    elif select == '1':
        start_itko()

    elif select == '2':
        from MyModules.exporting_xls import *
        start_itko(point='buh')
        cleaning_export_dir()
        cycling_exports()
        make_separator()
        quit_1c()

    elif select == '3':
        pass

    elif select == '4':
        start_itko(point='adm')

    success_window_alert()
