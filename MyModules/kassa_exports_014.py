# Модуль работы с экспортом 014
import datetime
import os.path

import pyautogui as pg
import time

from MyModules.config_read import KASSA_PATH_014
from MyModules.print_log import print_log
from MyModules.switch_layout_keyboard import eng_layout, rus_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.cur_dates import current_dates
from MyModules.select_menu import selecting_menu
from MyModules.making_dirs import kassa_making_dirs, DICT_MOUNTS, TODAY_MOUNTH

today = datetime.datetime.today().strftime('%d.%m.%y')
file_name_input = f"014 {today}.xml"
file_name_output = f"014_{today}.xml"
not_correct = 'Podrazd="73005"'
correct = 'Podrazd="63053"'


def kassa_export_014():
    """Функция экспорта файла 014"""
    print_log("Экспорт 014", line_before=True)

    path_ = kassa_making_dirs(KASSA_PATH_014) + "\\"

    if os.path.isfile(path_ + file_name_input):
        os.remove(path_ + file_name_input)
    if os.path.isfile(path_ + file_name_output):
        os.remove(path_ + file_name_output)

    selecting_menu(1, 9)
    pg.write(current_dates()[0])
    pg.press('tab')
    pg.write(today)
    pg.press('tab', presses=2)
    eng_layout()
    typing(KASSA_PATH_014 + datetime.datetime.today().strftime("%Y") + '\\')
    rus_layout()
    typing(DICT_MOUNTS.get(TODAY_MOUNTH))
    eng_layout()
    typing('\\' + file_name_input)
    time.sleep(1)
    pg.press('tab')
    pg.press('enter')
    time.sleep(10)

    print_log(f"Ожидание файла...")
    while True:
        time.sleep(1)
        if os.path.isfile(path_ + file_name_input):
            time.sleep(20)
            break

    print_log("Конвертация файла...")
    with open(path_ + file_name_input, 'r') as file:
        input_file = file.read()

    repl_string_xml = input_file.replace(not_correct, correct)

    with open(path_ + file_name_output, 'w') as file:
        file.write(repl_string_xml)

    if os.path.isfile(path_ + file_name_input):
        os.remove(path_ + file_name_input)
