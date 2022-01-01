import pyautogui as pg
from MyModules.print_log import print_log


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
        7: "Выгрузка 'ВОУ'",
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
    7: {menu_points.get(7)}
    =========================
    9: {menu_points.get(9)}
    """, title='МЕНЮ АВТОМАТИЗАЦИИ ИТКО', default='4')
