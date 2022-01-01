import pyautogui as pg
import subprocess
import time
from MyModules.config_read import *
from MyModules.print_log import print_log


def start_itko(point='buh', mode='ENTERPRISE', no_windows=True):
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
        pg.click(10, 680)  # закрыть всплывающее уведомление внизу

    if point == 'buh' and mode == 'ENTERPRISE':  # оставить администратора
        if not no_windows:
            print_log("Открытие окон")
            tuple_ = ((750, 115), (1250, 85), (85, 85))
            for item in tuple_:
                if item == (1250, 85):
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
        print_log("Открытие окна для загрузки базы", line_before=True)
        pg.press('alt')
        pg.press('right', presses=3, interval=0.1)
        pg.press('down', presses=5, interval=0.1)
        pg.press('enter')
        pg.press('tab')
        pg.press('enter')
        from MyModules.switch_layout import eng_layout
        eng_layout()
        from MyModules.typing_unicode_str import typing_unicode_str
        typing_unicode_str(PATH_ITKO)
        pg.press('enter')
