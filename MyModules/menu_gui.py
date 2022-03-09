# Модуль работы с меню

import pyautogui as pg
from datetime import datetime
from MyModules.print_log import print_log


def pyautogui_menu() -> str:
    """Функция МЕНЮ"""
    print_log("Запуск меню")

    menu_points = {
        0: 'Загрузка/Выгрузка базы ИТКО',
        1: 'Старт/Быстрый старт Бухгалтером',
        2: 'Старт/Быстрый старт ИТКО Администратором',
        3: "Формирование ВОУ",
        4: "Выгрузка 'ВОУ'",
        5: "Выгрузка '014'",
        6: "Выгрузка 'ВСКК'",
        7: "Файлы 'Сформировать.xls'/'РЖД.xls'",
        8: "Выгрузка '202 форма'",
        9: "Выгрузка 'Отчет по ПП'",
        30: "Выписки по клиентам",
        100: "Поменять системные дату/время"
    }
    separator = '=' * 40
    return pg.prompt(text=f"""
    МОДУЛЬ АВТОМАТИЗАЦИИ ИТКО
                                  время {datetime.now().strftime('%d.%m.%y %H:%M')}
    
    Необходимо выбрать пункт меню:

    0/00: {menu_points.get(0)}
    {separator}
    1/10: {menu_points.get(1)}
    2/20: {menu_points.get(2)}
    {separator}
    3: {menu_points.get(3)}
    {separator}
    4: {menu_points.get(4)}
    5: {menu_points.get(5)}
    6: {menu_points.get(6)}
    7/70: {menu_points.get(7)}
    8: {menu_points.get(8)}
    9: {menu_points.get(9)}
    {separator}
    30: {menu_points.get(30)}
    {separator}
    100: {menu_points.get(100)}
    """,
                     title='МЕНЮ АВТОМАТИЗАЦИИ ИТКО',
                     default='1')
