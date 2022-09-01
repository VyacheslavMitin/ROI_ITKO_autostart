# Модуль работы с меню

import os
import pyautogui as pg
from datetime import datetime
from MyModules.config_read import MY_LOGIN, KASSA_LOGIN
from MyModules.print_log import print_log

if os.getlogin() == MY_LOGIN:  # дефолтный выбор
    default_menu = '1'
elif os.getlogin() == KASSA_LOGIN:
    default_menu = '30'


def pyautogui_menu() -> str:
    """Функция МЕНЮ"""
    print_log("Запуск Меню", line_after=True)

    menu_points = {
        0: 'Загрузка/Выгрузка базы ИТКО/Конфигуратор',
        1: 'Старт/Быстрый старт Бухгалтером',
        2: 'Старт/Быстрый старт ИТКО Администратором',
        200: 'Бухгалтерские итоги',
        222: 'Удаление помеченных объектов',
        3: "Формирование ВОУ",
        4: "Выгрузка 'ВОУ'",
        5: "Выгрузка '014'",
        55: "Выгрузка '014 для Самары",
        6: "Выгрузка 'ВСКК'",
        7: "Файлы 'Сформировать.xls'/'РЖД.xls'",
        777: "Выгрузка для клиентов",
        8: "Выгрузка '202 форма'",
        9: "Выгрузка 'Отчет по ПП'",
        100: "Поменять системные дату/время",
        30: "Отправка XML", 31: "Выписки Мегафон-РТК-Вымпелком", 32: "Выгрузка АДМ",
    }
    separator = '=' * 47
    return pg.prompt(text=f"""
    МОДУЛЬ АВТОМАТИЗАЦИИ ИТКО
                                  время {datetime.now().strftime('%d.%m.%y %H:%M')}
    
    Необходимо выбрать пункт меню:

    0/00/000: {menu_points.get(0)}
    {separator}
    1/10: {menu_points.get(1)}
    {separator}
    2/20: {menu_points.get(2)}
    200: {menu_points.get(200)}
    222: {menu_points.get(222)}
    {separator}
    3: {menu_points.get(3)}
    {separator}
    4: {menu_points.get(4)}
    5: {menu_points.get(5)}
    55: {menu_points.get(55)}
    6: {menu_points.get(6)}
    7/70: {menu_points.get(7)}
    777: {menu_points.get(777)}
    8: {menu_points.get(8)}
    9: {menu_points.get(9)}
    {separator}
    30: {menu_points.get(30)}
    {separator}
    100: {menu_points.get(100)}
    """,
                     title='МЕНЮ АВТОМАТИЗАЦИИ ИТКО',
                     default=default_menu)
