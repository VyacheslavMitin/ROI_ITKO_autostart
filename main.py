# Модуль работы с ИТКО (выгрузка отчетов "сформировать")

# ИМПОРТЫ
import glob
import sys
import subprocess
import time
import pyautogui as pg
from datetime import datetime
# Мои модули
from MyModules.config_read import *
from MyModules.starting_itko import start_itko
from MyModules.menu_gui import pyautogui_menu
from MyModules.sending_files import sending_outlook
from MyModules.making_dirs import making_dirs
from MyModules.past_dates import past_dates
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout


# КОНСТАНТЫ
NOW_DATE = datetime.now().strftime('%d.%m.%y')  # Текущая дата в формате 01.01.22


# ФУНКЦИИ
def welcoming(name_='Автоматизация ИТКО', author_='Вячеслав Митин', version_='22'):
    """Функция приветствия"""
    print(f"МОДУЛЬ РАБОТЫ '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


def success_window_alert():
    """Функция отбивки об успехе"""
    time.sleep(1)
    pg.alert("Автоматизация завершена", title="Завершено")
    print_log("Автоматизация завершена", line_before=True)
    sys.exit(0)


def change_datetime():
    """Функция смены системной даты и времени"""
    print_log("Изменение даты/времени", line_before=True)
    from os import system
    system(CHANGE_TIME)


def interval_january(long_=False):
    """Функция определения интервалов: если январь и нужен доступ к документам прошлого года"""
    def clear_dates():
        pg.press('right', presses=20, interval=0.0)
        pg.press('backspace', presses=20, interval=0.0)

    if past_dates()[3] == '12':
        time_sec = 0
        pg.press('alt')
        pg.press('right', presses=1, interval=time_sec)
        pg.press('down', presses=12, interval=time_sec)
        if long_:
            pg.press('down', presses=4, interval=time_sec)
        pg.press('enter')
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
    from MyModules.select_menu import selecting_menu
    selecting_menu(1, 5)  # запуск журнала воу
    interval_january()
    selecting_menu(2, 6)  # запуск автоформирования


def cleaning_dir(path0_: str):
    """Функция удаления файлов в каталоге экспортов"""
    print_log("Очистка каталога экспорта")

    for files in glob.glob(path0_ + f'*.*'):
        os.remove(files)
    time.sleep(0.5)


def quit_1c(name_, path1_):
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

    os.system(f'explorer.exe {os.path.normpath(path1_)}')  # запуск проводника


if __name__ == '__main__':
    welcoming()
    making_dirs()

    select = pyautogui_menu()
    if select == '0':
        start_itko('import', point='adm', mode='CONFIG')
    elif select == '00':
        start_itko('export', point='adm', mode='CONFIG')

    elif select == '1':
        start_itko(point='buh', no_windows=False)
    elif select == '10':
        start_itko(point='buh', no_windows=True)

    elif select == '2':
        start_itko(point='adm', no_windows=False)
    elif select == '20':
        start_itko(point='adm', no_windows=True)

    elif select == '3':
        change_datetime()
        start_itko(point='buh')
        preparation_vou()

    elif select == '4':
        start_itko(point='buh')
        cleaning_dir(PATH_VOU)
        from MyModules.exports_vou import export_vou
        export_vou()
        quit_1c(*dict_with_paths.get('vou_dir'))
        time.sleep(0.5)
        sending_outlook(mode_='vou', displayed=True)

    elif select == '5':
        start_itko(point='buh')
        cleaning_dir(PATH_014)
        from MyModules.exports_014 import export_014
        export_014()
        quit_1c(*dict_with_paths.get('014_dir'))

    elif select == '6':
        start_itko(point='buh')
        cleaning_dir(PATH_VSKK)
        from MyModules.exports_vskk import export_vskk
        export_vskk()
        quit_1c(*dict_with_paths.get('vskk_dir'))

    elif select == '7':
        from MyModules.exporting_xls import *
        cleaning_dir(PATH_SFORMIROVAT)
        start_itko(point='buh')
        cycling_exports()
        quit_1c(*dict_with_paths.get('exports_dir'))
        time.sleep(0.5)
        sending_outlook(mode_='sformirovat', displayed=True)
    elif select == '70':
        from MyModules.exporting_xls import *
        cleaning_dir(PATH_SFORMIROVAT)
        start_itko(point='buh')
        exports_rzd()
        quit_1c(*dict_with_paths.get('exports_dir'))
        time.sleep(0.5)
        sending_outlook(mode_='sformirovat', displayed=True)

    elif select == '8':
        start_itko(point='buh')
        cleaning_dir(PATH_202)
        from MyModules.exports_202 import export_202
        export_202()
        quit_1c(*dict_with_paths.get('202_dir'))
        time.sleep(0.5)
        sending_outlook(mode_='202', displayed=True)

    elif select == '9':
        start_itko(point='buh')
        cleaning_dir(PATH_PP)
        from MyModules.exports_pp import export_pp
        export_pp()
        quit_1c(*dict_with_paths.get('pp_dir'))
        time.sleep(0.5)
        sending_outlook(mode_='pp', displayed=True)

    elif select == '10':
        change_datetime()

    elif select is None:
        pg.alert("Выход из меню!", title='Выход')
        sys.exit("Выход!")

    success_window_alert()
