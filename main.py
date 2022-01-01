# Модуль работы с ИТКО (выгрузка отчетов "сформировать")

# ИМПОРТЫ
import glob
import sys
import pyautogui as pg
from datetime import datetime
import subprocess
import time
# Мои модули
from MyModules.config_read import *
from MyModules.starting_itko import start_itko
from MyModules.menu_gui import pyautogui_menu
from MyModules.sending_files import sending_outlook
from MyModules.past_dates import past_dates
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout


# КОНСТАНТЫ
NOW_DATE = datetime.now().strftime('%d.%m.%y')  # Текущая дата в фоммате 01.01.22


# ФУНКЦИИ
def welcoming(name_='ИТКО', author_='Вячеслав Митин', version_='5'):
    """Функция приветсвия"""
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


def success_window_alert():
    """Функция отбивки об успехе"""
    time.sleep(1)
    pg.alert("Автоматизация завершена", title="Завершено")
    print_log("Автоматизация завершена", line_before=True)
    sys.exit(0)


def change_datetime():
    """Функция смены сестемной даты и времени"""
    print_log("Изменение даты/времени", line_before=True)
    file = 'change_datetime.lnk'
    import os
    os.system(file)


def interval_january(long_=False):
    """Функция определения интервалов если январь и нужен доступ к документам прошлого года"""
    from MyModules.past_dates import past_dates
    if past_dates()[3] == '12':
        pg.press('alt')
        pg.press('right', presses=1, interval=0.1)
        pg.press('down', presses=12, interval=0.1)
        if long_:
            pg.press('down', presses=4, interval=0.1)
        pg.press('enter')

    def clear_dates():
        pg.press('right', presses=10, interval=0.1)
        pg.press('backspace', presses=10, interval=0.1)

    clear_dates()
    typing(past_dates()[0])
    pg.press('tab')
    clear_dates()
    typing(NOW_DATE)
    pg.press('tab')
    pg.press('enter')


def preparation_vou():
    """Функция запуска расчета ВОУ"""
    print_log("Запуск расчета ВОУ", line_before=True)
    pg.click(750, 85)
    interval_january()
    pg.click(650, 85)


def cleaning_dir(path_: str):
    """Функция удаления файлов в каталоге экспортов"""
    print_log("Очистка каталога экспорта")

    for files in glob.glob(path_ + f'*.*'):
        os.remove(files)
    time.sleep(0.5)


def quit_1c(name_, path_):
    """Функция выхода из 1С и запуска проводника"""
    pg.hotkey('alt', 'f4')
    name_ = name_[:-1]
    if name_ in pg.getAllTitles():  # поиск открытой папки
        list__ = []
        for i in pg.getAllTitles():
            if i == name_:
                list__.append(i)
        for item in enumerate(list__):
            pg.getWindowsWithTitle(item[1])[item[0]].close()

    os.system(f'explorer.exe {os.path.normpath(path_)}')  # запуск проводника


if __name__ == '__main__':
    welcoming()

    select = pyautogui_menu()
    if select == '0':
        start_itko(point='adm', mode='CONFIG')

    elif select == '1':
        start_itko(point='buh', no_windows=False)
    elif select == '10':
        start_itko(point='buh', no_windows=True)

    elif select == '2':
        start_itko(point='adm')

    elif select == '3':
        change_datetime()
        start_itko(point='buh')
        preparation_vou()

    elif select == '4':
        from MyModules.exporting_xls import *
        start_itko(point='buh')
        cleaning_dir(PATH_SFORMIROVAT)
        cycling_exports()
        quit_1c(*dict_with_paths.get('exports_dir'))
        sending_outlook(mode_='sformirovat', displayed=True)

    elif select == '5':
        start_itko(point='buh')
        from MyModules.exports_014_vskk_vou import export_014
        cleaning_dir(PATH_014)
        export_014()
        quit_1c(*dict_with_paths.get('014_dir'))

    elif select == '6':
        start_itko(point='buh')
        from MyModules.exports_014_vskk_vou import export_vskk
        cleaning_dir(PATH_VSKK)
        export_vskk()
        quit_1c(*dict_with_paths.get('vskk_dir'))

    elif select == '7':
        start_itko(point='buh')
        from MyModules.exports_014_vskk_vou import export_vou
        cleaning_dir(PATH_VOU)
        export_vou()
        quit_1c(*dict_with_paths.get('vou_dir'))

    elif select == '8':
        start_itko(point='buh')
        from MyModules.exports_202 import export_202
        cleaning_dir(PATH_202)
        export_202()
        quit_1c(*dict_with_paths.get('202_dir'))
        sending_outlook(mode_='202', displayed=True)

    elif select == '9':
        change_datetime()

    success_window_alert()
