# Модуль с экспортами 014, ВСКК, ВОУ
import pyautogui as pg
import time
from MyModules.print_log import print_log
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.config_read import *


def export_014():
    """Функция экспорта файла 014"""
    print_log("Экспорт 014", line_before=True)
    from MyModules.past_dates import past_dates
    pg.click(50, 120)
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
    from MyModules.past_dates import past_dates
    pg.click(250, 120)
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
    typing(f'ВСКК ОКО ALL {past_dates()[3]} {past_dates()[2]}')
    pg.press('tab')
    pg.press('enter')
    time.sleep(5)
    pg.press('enter')


def export_vou():
    """Функция экспорта файлов ВОУ"""
    print_log("Работа с ВОУ", line_before=True)
    import pyperclip
    from MyModules.past_dates import past_dates
    file_name = 'ВОУ ОКО'
    print_log("Экспорт ВОУ в текстовый файл")
    pg.click(885, 85)  # экспорт файла
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
    pg.click(785, 85)  # вызов журнала с ведомостями
    from main import interval_january
    interval_january()
    pg.press('end')
    pg.press('enter')
    pg.press('tab', presses=4, interval=0.2)
    pg.hotkey('ctrl', 'c')
    pg.press('tab', presses=12, interval=0.2)
    pg.press('space')
    pg.press('down')
    pg.press('enter')
    time.sleep(4)
    pg.hotkey('ctrl', 's')
    time.sleep(0.5)
    eng_layout()
    typing(PATH_VOU)
    rus_layout()
    typing(f'{file_name}')
    eng_layout()
    typing(f'_{pyperclip.paste()}')
    pg.press('tab')
    pg.press('down', presses=2)  # выбор формата файла
    pg.press('enter', presses=2)  # сохранение файла
    time.sleep(0.5)

    print_log("Генерация DBF файла")
    pg.click(1025, 85)  # открытие обработки для превращения в ДБФ
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
    pg.click(10, 680)
    pg.hotkey('shift', 'tab')
    typing(past_dates()[1])
    pg.press('tab', presses=2, interval=0.2)
    pg.press('enter')
    time.sleep(30)
    pg.press('tab')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(3)
