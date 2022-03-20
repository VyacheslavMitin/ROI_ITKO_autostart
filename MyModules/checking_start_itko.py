# Модуль проверки запуска ИТКО

import time
import sys
import pyautogui as pg
from MyModules.print_log import print_log
from MyModules.config_read import KASSA_LOGIN

# Константы с именами окон для поиска
WINDOW_LAUNCHER = 'Запуск 1С:Предприятия'
WINDOW_AUTHORIZATION = 'Авторизация  доступа'
WINDOW_ITKO_ENTERPRISE_BUH = '1С:Предприятие - Касса пересчета РОИ ЦБ РФ:  Бухгалтер: Нурмухамедова Р.М.'
WINDOW_ITKO_ENTERPRISE_ADM = '1С:Предприятие - Касса пересчета РОИ ЦБ РФ:  Админ: Администратор'
WINDOW_ITKO_CONFIG = 'Конфигуратор - Касса пересчета РОИ ЦБ РФ'
TUPLE_WINDOWS = (WINDOW_ITKO_ENTERPRISE_BUH, WINDOW_ITKO_ENTERPRISE_ADM, WINDOW_ITKO_CONFIG)


# Функции
def authorization_itko() -> None:
    """Функция запуска ИТКО"""
    print_log("Запуск '1С: ИТКО'...")
    # Сначала - поиск лаунчера 1С 7
    for item in range(10):
        if WINDOW_LAUNCHER in pg.getAllTitles():
            print_log("Обнаружено окно выбора баз '1С: ИТКО', вход")
            break
        time.sleep(1)

    if WINDOW_LAUNCHER not in pg.getAllTitles():
        sys.exit("Не обнаружено окно выбора баз '1С: ИТКО'!")

    # Выбор первой (верхней базы в списке
    pg.press('tab', presses=2)
    pg.press('home')  # выбор первой базы в списке баз
    pg.press('enter')  # вход в базу

    print_log("Ожидание окна авторизации '1С: ИТКО'...", line_before=False)
    # Потом - поиск окна авторизации
    for item in range(60):  # ожидание 30 секунд окна авторизации
        if WINDOW_AUTHORIZATION in pg.getAllTitles():
            print_log("Обнаружено окно авторизации в базу '1С: ИТКО'")
            break
        time.sleep(0.5)

    if WINDOW_AUTHORIZATION not in pg.getAllTitles():
        sys.exit("Не обнаружено окно авторизации в базу '1С: ИТКО'")
    else:
        print_log("Авторизация '1С: ИТКО' подготовлена")

    # Работа с авторизацией
    pg.hotkey('shift', 'tab')  # переход в поле выбора пользователя
    pg.press('home')  # выбор администратора для точки отсчета


def check_itko():
    """Функция проверки запуска ИТКО"""
    print_log("Проверка запуска '1С: ИТКО'...")

    i = 0
    check = False

    while i < 20:
        for element in TUPLE_WINDOWS:
            if element in pg.getAllTitles():
                print_log("'1С: ИТКО' запущена")
                check = True
                break
            else:
                continue
        if check:
            break
        time.sleep(0.5)
        i += 1

    if not check:
        print_log("'1С: ИТКО' не запущено!")


if __name__ == '__main__':
    check_itko()
