# Модуль закрытия кассового дня

import time
import pyautogui as pg
from MyModules.select_menu import selecting_menu
from MyModules.print_log import print_log


def closing_day():
    """Функция закрытия кассового дня"""
    print_log("Закрытие кассового дня...", line_before=True)
    selecting_menu(1, 13)  # запуск закрытия дня

    pg.press('tab', presses=3, interval=0.2)
    pg.press('space')
    time.sleep(3)
    print_log("Кассовый день закрыт", line_before=True)
