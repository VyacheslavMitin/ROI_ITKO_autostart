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

    subprocess.Popen([
        itko_bin,
        mode
    ])

    time.sleep(1)
    authorization_itko()

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
            from main import interval_january
            if 1 <= int(datetime.now().strftime('%d')) <= 10:  # если первые 10 дней месяца
                from MyModules.exporting_xls import call_sformirovat
                call_sformirovat()  # документы за день
                selecting_menu(2, 5)  # журнал воу
                interval_january(long_=False)
                pg.press('end')
                pg.press('enter')
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
                selecting_menu(2, 3)  # распред. ведомости
                interval_january(long_=True)
                selecting_menu(2, 4)  # клиенты

    if point == 'adm' and mode == 'ENTERPRISE':  # оставить администратора
        if not no_windows:
            from datetime import datetime
            from main import interval_january
            if 1 <= int(datetime.now().strftime('%d')) <= 10:
                print_log("Открытие журнала ВОУ")
                time.sleep(0.5)
                pg.press('alt')
                pg.press('right', presses=4, interval=0.1)
                pg.press('down', presses=5, interval=0.1)
                pg.press('enter')
                interval_january()
            print_log("Открытие журнала документов")
            time.sleep(0.5)
            pg.press('alt')
            if 1 <= int(datetime.now().strftime('%d')) <= 10:
                pg.press('right', presses=2, interval=0.1)
            else:
                pg.press('right', presses=4, interval=0.1)
            pg.press('down', presses=1, interval=0.1)
            pg.press('enter', presses=2, interval=0.5)

    if mode == 'CONFIG':
        from MyModules.switch_layout import eng_layout, rus_layout
        from MyModules.typing_unicode_str import typing_unicode_str
        pg.press('alt')
        pg.press('right', presses=3, interval=0.1)
        if args[0] == 'import':
            print_log("Открытие окна для загрузки базы", line_before=True)
            pg.press('down', presses=5, interval=0.1)
            pg.press('enter')
            pg.press('tab')
            pg.press('enter')
            eng_layout()
            typing_unicode_str(PATH_ITKO)
            pg.press('enter')
        elif args[0] == 'export':
            from MyModules.past_dates import past_dates
            print_log("Открытие окна для выгрузки базы", line_before=True)
            pg.press('down', presses=4, interval=0.1)
            pg.press('enter')
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
