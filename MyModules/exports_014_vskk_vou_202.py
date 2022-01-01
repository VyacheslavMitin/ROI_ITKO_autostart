# Модуль с экспортами 014, ВСКК, ВОУ
import pyautogui as pg
import time

from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.past_dates import past_dates
from MyModules.select_menu import selecting_menu


def export_014():
    """Функция экспорта файла 014"""
    print_log("Экспорт 014", line_before=True)
    selecting_menu(1, 9)
    pg.write(past_dates()[0])
    pg.press('tab')
    pg.write(past_dates()[1])
    pg.press('tab', presses=2)
    typing(PATH_014 + f'014_{past_dates()[5]}.xml')
    time.sleep(1)
    pg.press('tab')
    pg.press('enter')
    time.sleep(30)


def export_vskk():
    """Функция экспорта файла ВСКК"""
    print_log("Экспорт ВСКК", line_before=True)
    selecting_menu(1, 10)
    pg.press('tab', presses=8, interval=0.2)
    pg.press('esc', interval=0.2)
    pg.press('tab')
    pg.write(past_dates()[0])
    pg.press('tab')
    pg.write(past_dates()[1])
    pg.press('tab', presses=2, interval=0.2)
    eng_layout()
    typing(PATH_VSKK)
    rus_layout()
    typing(f'ВСКК ОКО ALL {past_dates()[3]} {past_dates()[6]}')
    pg.press('tab')
    pg.press('enter')
    time.sleep(5)
    pg.press('enter')


def export_vou():
    """Функция экспорта файлов ВОУ"""
    print_log("Работа с ВОУ", line_before=True)
    file_name = 'ВОУ ОКО'
    print_log("Экспорт ВОУ в текстовый файл")
    selecting_menu(1, 7)  # запуск обработки выгрузки воу
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

    print_log("Генерация XLS файла")
    selecting_menu(2, 5)  # вход в журнал воу с сохранением файла
    from main import interval_january
    interval_january()
    pg.press('end')
    pg.press('enter')
    pg.press('tab', presses=16, interval=0.1)
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
    pg.press('tab')
    pg.press('down', presses=2)  # выбор формата файла
    pg.press('enter', presses=2)  # сохранение файла
    time.sleep(0.5)

    print_log("Генерация DBF файла")
    selecting_menu(4, 8)  # запуск обработки конвертации тхт в дбф
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


def export_202():
    """Функция экспорта файлов 202 формы"""
    print_log("Экспорт 202 формы", line_before=True)
    selecting_menu(1, 11)  # запуск обработки выгрузки 202
    pg.press('tab', presses=1, interval=0.2)
    pg.press('space')
    pg.press('tab', presses=2, interval=0.2)
    for item in range(3):
        pg.press('space')
        pg.press('tab')
    eng_layout()
    typing(PATH_202)
    pg.press('tab')
    pg.press('enter')
    print_log("Выгрузка файлов отчета")
    time.sleep(40)
    pg.press('tab', presses=2, interval=0.2)
    pg.press('enter')
    time.sleep(5)
    print_log("Выгрузка форм по банкам в XLS")
    banks = ('ВТБ', 'Р-ИНКАС', 'ГПБ', 'ВБРР')
    for bank in banks:
        pg.hotkey('ctrl', 's')
        time.sleep(0.5)
        eng_layout()
        typing(PATH_202)
        rus_layout()
        typing(f'202_{bank}')
        pg.press('tab')
        pg.press('down', presses=2)  # выбор формата файла
        pg.press('enter', presses=2)  # сохранение файла
        time.sleep(0.5)
        pg.hotkey('ctrl', 'F4')  # закрытие окна формы
