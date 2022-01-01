# Модуль работы с ИТКО (выгрузка отчетов "сформировать")

# ИМПОРТЫ
import glob
import sys
from datetime import datetime
import subprocess
import pyautogui as pg
import time
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.print_log import print_log
from MyModules.quit_itko import quit_1c
from MyModules.menu_gui import pyautogui_menu
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.config_read import *

# КОНСТАНТЫ
NOW_DATE = datetime.now().strftime('%d.%m.%y')  # Текущая дата в фоммате 01.01.22


# ФУНКЦИИ
def welcoming(name_='ИТКО', author_='Вячеслав Митин', version_='5'):
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


def start_itko(point='buh', mode='ENTERPRISE', no_windows=True):
    """Функция запуска 1С 7 ИТКО"""
    print_log(f"Запуск ИТКО в  режиме {mode}")

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

    pg.press('enter', presses=4, interval=0.5)
    pg.press('tab', presses=2, interval=0.5)
    pg.press('enter')

    if point == 'buh' and mode == 'ENTERPRISE':  # оставить администратора
        time.sleep(0.5)
        pg.click(10, 680)
        if not no_windows:
            print_log("Открытие окон")
            tuple_ = ((750, 115), (85, 85))
            for i in tuple_:
                pg.click(i)

    if point == 'adm' and mode == 'ENTERPRISE':  # оставить администратора
        print_log("Открытие журнала ВОУ")
        time.sleep(0.5)
        pg.press('alt')
        pg.press('right', presses=4, interval=0.1)
        pg.press('down', presses=5, interval=0.1)
        pg.press('enter')
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
        from MyModules.typing_unicode_str import typing_unicode_str
        typing_unicode_str(PATH_ITKO)
        pg.press('enter')


def success_window_alert():
    time.sleep(1)
    pg.alert("Автоматизация завершена", title="Завершено")
    print_log("Автоматизация завершена", line_before=True)
    sys.exit(0)


def change_datetime():
    print_log("Изменение даты/времени", line_before=True)
    file = 'change_datetime.lnk'
    import os
    os.system(file)


def preparation_vou():
    print_log("Запуск расчета ВОУ", line_before=True)
    pg.click(750, 85)
    pg.click(650, 85)


def cleaning_dir(path_: str):
    """Функция удаления файлов в каталоге экспортов"""
    print_log("Очистка каталога экспорта")

    for files in glob.glob(path_ + f'*.*'):
        os.remove(files)
    time.sleep(0.5)


if __name__ == '__main__':
    welcoming()

    select = pyautogui_menu()
    if select == '0':
        start_itko(point='adm', mode='CONFIG')

    elif select == '1':
        start_itko(point='buh', no_windows=False)

    elif select == '2':
        start_itko(point='adm')

    elif select == '3':
        change_datetime()
        start_itko()
        preparation_vou()

    elif select == '4':
        from MyModules.exporting_xls import *
        start_itko(point='buh')
        cleaning_dir(PATH_EXPORTS)
        cycling_exports()
        quit_1c()

    elif select == '5':
        start_itko(point='buh')
        from MyModules.exports_014_vskk_vou import export_014
        export_014()
        quit_1c()

    elif select == '6':
        start_itko(point='buh')
        from MyModules.exports_014_vskk_vou import export_vskk
        export_vskk()
        quit_1c()

    elif select == '7':
        start_itko(point='buh')
        from MyModules.exports_014_vskk_vou import export_vou
        export_vou()
        quit_1c()

    elif select == '9':
        change_datetime()

    success_window_alert()
