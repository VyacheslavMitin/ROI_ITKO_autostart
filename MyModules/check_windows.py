# Модуль проверки открытых окон


# Импорты
import pyautogui as pg
import time
import sys
from MyModules.print_log import print_log


# Функции
def check_window(window='', seconds=10):
    check = None
    print_log(f"Поиск окна {window}...")
    for item in range(seconds):  # ожидание 30 секунд окна авторизации
        if window in pg.getAllTitles():
            print_log(f"Обнаружено окно '{window}', все хорошо")
            check = True
            break
        else:
            if (item % 10) == 0.0:  # выводить каждые 10 секунд
                print_log(f"Окно '{window}' не обнаружено!")
        time.sleep(1)
    if check:
        return True


def check_not_window(window='', seconds=10):
    check = None
    print_log(f"Поиск окна {window}...")
    for item in range(seconds):  # ожидание 30 секунд окна авторизации
        if window not in pg.getAllTitles():
            print_log(f"Окно '{window}' не обнаружено, все хорошо")
            check = True
            break
        else:
            if (item % 10) == 0.0:  # выводить каждые 10 секунд
                print_log(f"Окно '{window}' обнаружено!")
        time.sleep(1)
    if check:
        return True


if __name__ == '__main__':
    print("Проверка функции поиска окон")
    print("Присутствие окна")
    check_window(window='Загрузка данных')
    print("Отсутствие окна")
    check_not_window(window='Загрузка данных')
