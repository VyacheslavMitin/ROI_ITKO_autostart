# Модуль работы с ИТКО (выгрузка отчетов "сформировать")

# ИМПОРТЫ
import glob
import sys
import time
import pyautogui as pg
# Мои модули
from MyModules.config_read import *
from MyModules.starting_itko import start_itko
from MyModules.menu_gui import pyautogui_menu
from MyModules.sending_files import sending_outlook
from MyModules.making_dirs import making_dirs, kassa_making_dirs, kassa_making_dirs_banks
from MyModules.cleaning_dir import cleaning_dir
from MyModules.past_dates import past_dates
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.quit_itko import quit_1c, kassa_quit_1c


# ФУНКЦИИ
def welcoming(name_='Автоматизация ИТКО', author_='Вячеслав Митин', version_='38'):
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
    elif select == '200':
        start_itko('Бухгалтерские итоги', point='adm', no_windows=True)
    elif select == '222':
        start_itko('Удаление объектов', point='adm', no_windows=True)

    elif select == '3':
        change_datetime()
        start_itko(point='buh')
        from MyModules.preparation_vou import preparation_vou
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
    elif select == '55':
        start_itko(point='buh')
        from MyModules.kassa_exports_014 import kassa_export_014
        kassa_export_014()
        kassa_quit_1c(kassa_making_dirs(KASSA_PATH_014))

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
    elif select == '777':
        start_itko(point='buh')
        from MyModules.exports_invoice_details import exports_invoice_details
        cleaning_dir(PATH_CLIENTS)
        exports_invoice_details()
        quit_1c(*dict_with_paths.get('clients_dir'))
        time.sleep(0.5)

    elif select == '8':
        start_itko(point='buh')
        cleaning_dir(PATH_202)
        from MyModules.exports_202 import export_202
        export_202(change_mount=False)
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

    elif select == '30':
        start_itko(point='buh')
        from MyModules.kassa_exports_xml_xls_reestr import export_xml_xls_reestr
        export_xml_xls_reestr()
        quit_1c(None, None)
        time.sleep(0.5)

    elif select == '100':
        change_datetime()

    elif select is None:
        pg.alert("Выход из меню!", title='Выход')
        sys.exit("Выход!")

    success_window_alert()
