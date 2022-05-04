# Модуль запуска ИТКО

import pyautogui as pg
import subprocess
import time
from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.select_menu import selecting_menu
from MyModules.checking_start_itko import authorization_itko, check_itko


def start_itko(*args, point='buh', mode='ENTERPRISE', no_windows=True):
    """Функция запуска 1С 7 ИТКО"""
    print_log(f"Запуск 1С: ИТКО в режиме {mode}")

    if os.getlogin() == KASSA_LOGIN:  # проверка сети если касса
        from MyModules.kassa_checking_network import network_work
        network_work()
        itko_bin = KASSA_ITKO_BIN
    else:
        itko_bin = ITKO_BIN

    subprocess.Popen([  # запуск процесса ИТКО
        itko_bin,
        mode
    ])

    time.sleep(1)
    if not args:
        authorization_itko(monopoly=False)
    elif args[0] == "Удаление объектов" or args[0] == "Бухгалтерские итоги":
        authorization_itko(monopoly=True)
    else:  # работа с конфигуратором, аргументы импорт и экспорт
        authorization_itko(monopoly=False)

    if point == 'buh':  # выбор бухгалтера
        print_log("Выбор 'Бухгалтер' для входа")
        pg.press('down', presses=7, interval=0.1)
    elif point == 'adm':  # оставить администратора
        print_log("Выбор 'Администратор' для входа")

    timeout = 0
    interval = 0.3
    if os.getlogin() == KASSA_LOGIN:
        timeout = 2
        interval = 2
    elif os.getlogin() == MY_LOGIN:
        timeout = 0
        interval = 0.3

    time.sleep(timeout)
    pg.press('enter', presses=4, interval=interval)
    time.sleep(timeout)
    pg.press('tab', presses=2, interval=interval)
    pg.press('enter')
    time.sleep(timeout)
    check_itko()

    if mode == 'ENTERPRISE':
        pg.hotkey('ctrl', 'shift', 'z')  # закрыть окно сообщений

    if point == 'buh' and mode == 'ENTERPRISE':
        if not no_windows:
            print_log("Открытие окон")
            from datetime import datetime
            from MyModules.interval_journals import interval_january
            if 1 <= int(datetime.now().strftime('%d')) <= 10:  # если первые 10 дней месяца
                from MyModules.exporting_xls import call_sformirovat
                call_sformirovat()  # документы за день
                from MyModules.open_vou import open_last_vou
                open_last_vou(2)  # журнал ВОУ
            else:  # если НЕ первые 10 дней месяца
                selecting_menu(1, 2)  # документы за день
                pg.press('F4')
                pg.press('end')
                pg.press('enter')
                pg.press('tab', presses=1, interval=0.0)
                for i in range(4):
                    pg.press('tab')
                    pg.press('space')
                pg.press('tab', presses=1, interval=0.0)
                for i in range(4):
                    pg.press('tab')
                    pg.press('space')
                selecting_menu(2, 3)  # распределительные ведомости
                interval_january(long_=True)
                selecting_menu(2, 4)  # клиенты

    if point == 'adm' and mode == 'ENTERPRISE':  # оставить администратора
        if not no_windows:
            from datetime import datetime
            from MyModules.interval_journals import interval_january
            if 1 <= int(datetime.now().strftime('%d')) <= 10:
                print_log("Открытие журнала ВОУ")
                from MyModules.open_vou import open_last_vou
                open_last_vou(4)  # журнал ВОУ
            print_log("Открытие журнала документов")
            time.sleep(0.5)
            if 1 <= int(datetime.now().strftime('%d')) <= 10:
                selecting_menu(2, 1)
            else:
                selecting_menu(4, 1)
            pg.press('enter', presses=1, interval=0.5)

    if point == 'adm' and mode == 'ENTERPRISE' and args:
        if args[0] == 'Удаление объектов':
            print_log("Открытие меню для удаления помеченных объектов")
            time.sleep(0.5)
            selecting_menu(1, 14)
            time.sleep(1)
            pg.press('space')
        elif args[0] == 'Бухгалтерские итоги':
            print_log("Открытие меню управления бухгалтерскими итогами")
            time.sleep(0.5)
            selecting_menu(1, 18)

    if mode == 'CONFIG':
        from MyModules.switch_layout import eng_layout, rus_layout
        from MyModules.typing_unicode_str import typing_unicode_str
        if args[0] == 'import':
            print_log("Открытие окна для загрузки базы", line_before=True)
            selecting_menu(3, 5, 0.1)
            pg.press('tab')
            pg.press('enter')
            eng_layout()
            typing_unicode_str(PATH_ITKO)
            pg.press('enter')
        elif args[0] == 'export':
            from MyModules.past_dates import past_dates
            print_log("Открытие окна для выгрузки базы", line_before=True)
            selecting_menu(3, 4, 0.1)
            eng_layout()
            typing_unicode_str(PATH_ITKO)
            typing_unicode_str(past_dates()[7])
            rus_layout()
            typing_unicode_str(" после ВОУ")
            eng_layout()
            typing_unicode_str(".zip")
            pg.press('tab', presses=2, interval=0.2)
            pg.press('enter')


if __name__ == '__main__':
    start_itko()
