# Модуль проверки запуска ИТКО

import time
import sys
import pyautogui as pg
from MyModules.print_log import print_log


WINDOW_LAUNCHER = 'Запуск 1С:Предприятия'
WINDOW_AUTHORIZATION = 'Авторизация  доступа'


def check_itko() -> bool:
    """Функция проверки запуска ИТКО"""
    print_log("Проверка запуска '1С: ИТКО'...")
    # Сначала - поиск лаунчера 1С 7
    for item in range(10):
        if WINDOW_LAUNCHER in pg.getAllTitles():
            print_log("Обнаружено окно выбора баз '1С: ИТКО'")
            break
        time.sleep(1)

    if WINDOW_LAUNCHER not in pg.getAllTitles():
        sys.exit("Не обнаружено окно выбора баз '1С: ИТКО'")

    # Потом - поиск окна авторизации
    for item in range(30):
        if WINDOW_AUTHORIZATION in pg.getAllTitles():
            print_log("Обнаружено авторизации в базу '1С: ИТКО'")
            break
        time.sleep(1)

    if WINDOW_AUTHORIZATION not in pg.getAllTitles():
        sys.exit("Не обнаружено окно авторизации в базу '1С: ИТКО'")
    else:
        print_log("'1С: ИТКО' обнаружена")
        return True


if __name__ == '__main__':
    check_itko()
