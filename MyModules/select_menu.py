import pyautogui as pg
# Мои модули
# from MyModules.select_menu import selecting_menu


def selecting_menu(point_):
    """Функция выбора строки меню в 'Робот'.
    0 - ТочкиПоДням
    1 - Журнал ВОУ
    2 - Распредел. ведомости
    3 - Клиенты
    4 - Авто ВОУ
    5 - Выгрузка ВОУ
    6 - Выгрузка 014
    7 - Преобразовать TXT в DBF
    8 - Выгрузка ВСКК
    9 - Выгрузка 202"""

    pg.press('alt', presses=2)
    pg.press('down', presses=point_)
    pg.press('enter')
