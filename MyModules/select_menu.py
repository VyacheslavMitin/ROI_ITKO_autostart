# Модуль работы с меню "робот" в ИТКО

import time

import pyautogui as pg
# Мои модули
# from MyModules.select_menu import selecting_menu


def selecting_menu(mode_, point_):
    """Функция выбора строки меню в 'Робот'.
    1 - ТочкиПоДням
    2 - Документы кассового дня
    3 - Распредел. ведомости
    4 - Клиенты
    5 - Журнал ВОУ
    6 - Автоформирование ВОУ
    7 - Выгрузка ВОУ
    8 - Преобразовать TXT в DBF
    9 - Выгрузка 014
    10 - Выгрузка ВСКК
    11 - Выгрузка 202"""

    timeout = 0.0  # без таймаута

    time.sleep(timeout)
    pg.press('alt')
    time.sleep(timeout)
    pg.press('right', presses=mode_, interval=timeout)
    time.sleep(timeout)
    pg.press('down', presses=point_, interval=timeout)
    time.sleep(timeout)
    pg.press('enter')
    time.sleep(timeout)
