# Модуль запуска ИТКО
import sys
import pyautogui as pg
import subprocess
import time
from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.select_menu import selecting_menu
from MyModules.checking_start_itko import authorization_itko, check_itko
from MyModules.check_windows import check_window


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

        if args[0] == 'config':  # если идет загрузка базы
            pass

        if args[0] == 'import':  # если идет загрузка базы
            print_log("Открытие окна для загрузки базы", line_before=True)
            selecting_menu(3, 5, 0.1)
            pg.press('tab')
            pg.press('enter')
            eng_layout()
            typing_unicode_str(PATH_ITKO)  # ввод пути к каталогу с бекапами
            pg.press('enter')
            time.sleep(1)
            pg.press('tab', presses=4)
            time.sleep(0.5)
            pg.press('down')
            time.sleep(0.5)
            pg.press('up')
            time.sleep(0.5)
            pg.press('enter')
            time.sleep(1)
            import pyperclip
            import keyboard
            keyboard.press('shift')
            time.sleep(0.5)
            keyboard.press_and_release("down")
            keyboard.release('shift')
            rus_layout()
            pg.hotkey('ctrl', 'c')
            string_base_name = pyperclip.paste()
            time.sleep(0.5)
            string_base_name = string_base_name[53:]
            time.sleep(1)
            pg.press('enter')
            time.sleep(1)
            from MyModules.send_notification_telegram import notification_send_telegram
            if check_window("Конфигуратор", 60):  # проверка, что окно "Конфигуратор" появилось
                pg.press('space')  # согласия на загрузку базы
            else:
                error = f"Не появилось окно распаковки базы '{string_base_name}'"
                notification_send_telegram(error)
                sys.exit(error)
            if check_window("Конфигуратор", 900):  # проверка, что окно "Конфигуратор" появилось
                success_message = f"База '{string_base_name}' загружена"
                print_log(success_message)
                notification_send_telegram(success_message)
                time.sleep(1)
                pg.press('enter')
                from MyModules.quit_itko import quit_1c
                quit_1c(None, None)
            else:
                error = f"Не появилось окно успешного завершения базы '{string_base_name}'"
                notification_send_telegram(error)
                sys.exit(error)

        elif args[0] == 'export':  # если идет выгрузка базы
            from MyModules.past_dates import past_dates
            from MyModules.ntp_time import ntp_time_get
            print_log("Открытие окна для выгрузки базы", line_before=True)
            selecting_menu(3, 4, 0.1)
            string_base_name = ''
            eng_layout()
            typing_unicode_str(PATH_ITKO)
            string_base_name += PATH_ITKO
            typing_unicode_str(past_dates()[7])
            string_base_name += past_dates()[7]
            rus_layout()
            now_date_time = ntp_time_get()
            typing_unicode_str(" после ВОУ ")
            string_base_name += " после ВОУ "
            eng_layout()
            typing_unicode_str(f"({now_date_time})")
            string_base_name += f"({now_date_time})"
            typing_unicode_str(".zip")
            string_base_name += ".zip"
            string_base_name = string_base_name[53:]
            time.sleep(1)

            # import pyperclip
            # import keyboard
            # keyboard.press('shift')
            # time.sleep(0.5)
            # keyboard.press_and_release("down")
            # keyboard.release('shift')
            # eng_layout()
            # pg.hotkey('ctrl', 'c')
            # string_base_name = pyperclip.paste()
            # time.sleep(0.5)
            # string_base_name = string_base_name[53:]
            time.sleep(1)
            pg.press('tab', presses=2, interval=0.2)
            pg.press('enter')  # запуск выгрузки базы
            from MyModules.send_notification_telegram import notification_send_telegram
            if check_window("Конфигуратор", 900):  # проверка, что окно "Конфигуратор" появилось
                success_message = f"База '{string_base_name}' выгружена"
                print_log(success_message)
                notification_send_telegram(success_message)
                time.sleep(1)
                pg.press('enter')
                from MyModules.quit_itko import quit_1c
                quit_1c(None, None)
            else:
                error_message = f"База '{string_base_name}' не выгружена!"
                notification_send_telegram(error_message)
                sys.exit(error_message)


if __name__ == '__main__':
    start_itko()
