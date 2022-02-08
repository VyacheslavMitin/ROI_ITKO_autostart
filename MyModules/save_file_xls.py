# Модуль сохранения файлов
# from MyModules.save_file_xls import saving_xls

import pyautogui as pg
import time
from MyModules.print_log import print_log


def saving_xls(name=None):
    """Функция сохранения файла в MS Excel"""

    if name is None:
        print_log("Сохранение файла в MS Excel")
    else:
        print_log(f"Сохранение файла '{name}' в MS Excel")

    time.sleep(0.5)

    pg.press('tab')
    pg.press('down', presses=2)  # выбор формата файла
    pg.press('enter', presses=2)  # сохранение файла

    time.sleep(0.5)
