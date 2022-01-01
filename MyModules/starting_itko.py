import pyautogui as pg
import subprocess
import time
from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.select_menu import selecting_menu


def start_itko(*args, point='buh', mode='ENTERPRISE', no_windows=True):
    """Функция запуска 1С 7 ИТКО"""
    print_log(f"Запуск ИТКО в режиме {mode}")

    subprocess.Popen([
        ITKO_BIN,
        mode
    ])

    time.sleep(1)
    pg.press('tab', presses=2)
    pg.press('home')  # выбор первой базы в списке баз
    pg.press('enter')
    pg.hotkey('shift', 'tab')
    pg.press('home')  # выбор администратора для точки отсчета

    if point == 'buh':  # выбор бухгалтера
        print_log("Выбор Бухгалтера для входа")
        pg.press('down', presses=7)
    elif point == 'adm':  # оставить администратора
        print_log("Выбор Администратора для входа")

    pg.press('enter', presses=4, interval=0.3)
    pg.press('tab', presses=2, interval=0.3)
    pg.press('enter')
    time.sleep(0.5)

    if mode == 'ENTERPRISE':
        pg.click(COORDINATES_FOR_DISPLAY.get('закрыть уведомление'))  # закрыть всплывающее уведомление внизу

    if point == 'buh' and mode == 'ENTERPRISE':  # оставить администратора
        if not no_windows:
            print_log("Открытие окон")
            tuple_ = (COORDINATES_FOR_DISPLAY.get('документы за день'),
                      COORDINATES_FOR_DISPLAY.get('распред. ведомости'),
                      COORDINATES_FOR_DISPLAY.get('открыть клиенты'))
            for item in tuple_:
                if item == COORDINATES_FOR_DISPLAY.get('распред. ведомости'):
                    pg.click(item)
                    from main import interval_january
                    interval_january(long_=True)
                pg.click(item)

    if point == 'adm' and mode == 'ENTERPRISE':  # оставить администратора
        if not no_windows:
            from main import interval_january
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
            pg.press('right', presses=2, interval=0.1)
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
