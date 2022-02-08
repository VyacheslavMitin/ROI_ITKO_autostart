# Модуль работы с экспортом отчета о ПП

import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import period_for_emails, past_dates
from MyModules.select_menu import selecting_menu
from MyModules.save_file_xls import saving_xls


def export_pp():
    """Функция экспорта отчета по ПП"""
    print_log("Экспорт отчета по ПП", line_before=True)
    name_short = f'Отчет о ПП Ульяновск ({period_for_emails()})'
    name_full = f'Отчет о Платежным Поручениям - РЦ "Ульяновск" за {period_for_emails()}'
    selecting_menu(1, 12)  # запуск обработки выгрузки 202

    # Формирование формы отчета
    print_log('Формирование отчета о ПП')
    time.sleep(0.5)
    pg.write(past_dates()[0])
    pg.press('tab')
    time.sleep(0.5)
    pg.write(past_dates()[1])
    pg.press('tab', presses=2)
    pg.press('space')
    time.sleep(1)

    # Запись в отчет Даты
    print_log('Запись названия в отчет ПП')
    pg.press('pgup', presses=2, interval=0.5)
    pg.press('right', presses=3, interval=0.1)
    selecting_menu(3, 9)
    pg.press('space')
    rus_layout()
    typing(name_full)
    pg.press('enter')

    # Сохранения отчета в файл
    pg.hotkey('ctrl', 's')
    eng_layout()
    typing(PATH_PP)
    rus_layout()
    typing(name_short)
    saving_xls(name_short)
