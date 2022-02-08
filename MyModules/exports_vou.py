# Модуль работы с экспортом ВОУ

import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import past_dates
from MyModules.select_menu import selecting_menu
from MyModules.save_file_xls import saving_xls


def export_vou():
    """Функция экспорта файлов ВОУ"""
    print_log("Генерация XLS файла")
    selecting_menu(1, 5)  # вход в журнал воу с сохранением файла
    from main import interval_january
    interval_january()
    pg.press('end')
    pg.press('enter')
    # pg.press('tab', presses=16, interval=0.1)  # без записи даты в ВОУ
    pg.press('tab', presses=4, interval=0.1)
    eng_layout()
    typing(f'{past_dates()[1]}')
    print_log(f"Смена даты в ВОУ на {past_dates()[1]}")
    pg.press('tab', presses=12, interval=0.1)
    pg.press('space')
    pg.press('down')
    pg.press('enter')
    time.sleep(4)
    pg.hotkey('ctrl', 's')
    time.sleep(0.5)
    eng_layout()
    typing(PATH_VOU)
    rus_layout()
    from MyModules.past_dates import period_for_emails
    typing(f'Детализация выручки ОКО {period_for_emails()}')
    saving_xls(f'Детализация выручки ОКО {period_for_emails()}')
    # pg.press('tab')
    # pg.press('down', presses=2)  # выбор формата файла
    # pg.press('enter', presses=2)  # сохранение файла
    # time.sleep(0.5)
    # pg.hotkey('ctrl', 'f4')
    pg.keyDown('shift')
    pg.press('tab')
    pg.keyUp('shift')
    pg.press('space')
    time.sleep(0.5)

    print_log("Работа с ВОУ", line_before=True)
    file_name = 'ВОУ ОКО'
    print_log("Экспорт ВОУ в текстовый файл")
    selecting_menu(2, 7)  # запуск обработки выгрузки воу
    pg.press('tab', presses=9, interval=0.2)
    pg.write(past_dates()[1])
    pg.press('tab')
    pg.write(past_dates()[0])
    pg.press('tab')
    eng_layout()
    typing(PATH_VOU)
    rus_layout()
    typing(f'{file_name}')
    eng_layout()
    typing('.txt')
    pg.press('tab')
    pg.press('enter')
    time.sleep(3)

    print_log("Генерация DBF файла")
    selecting_menu(2, 8)  # запуск обработки конвертации тхт в дбф
    pg.press('f4')
    time.sleep(0.5)
    rus_layout()
    typing(f'{file_name}_')
    eng_layout()
    typing(f'{past_dates()[0]}_{past_dates()[1]}')
    eng_layout()
    typing('.txt')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'shift', 'z')  # закрыть окно сообщений
    pg.hotkey('shift', 'tab')
    typing(past_dates()[1])
    pg.press('tab', presses=2, interval=0.2)
    pg.press('enter')
    time.sleep(30)
    pg.press('tab')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(3)


