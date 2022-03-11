# Модуль экспорта реестров в XML и XLS

import datetime
import time
import pyperclip
import pyautogui as pg
from MyModules.config_read import *
from MyModules.select_menu import selecting_menu
from MyModules.print_log import print_log
from MyModules.close_day import closing_day
from MyModules.save_file_xls import saving_xls
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.making_dirs import kassa_making_dirs

TODAY_YEAR = datetime.date.today().strftime("%Y")
TODAY_DATE = datetime.date.today().strftime("%d %m %Y")
TODAY_MOUNT = datetime.date.today().strftime("%m")
SAMPLE_NAME = "Реестр"

DICT_MOUNTS = {
    '01': "Январь",
    '02': "Февраль",
    '03': "Март",
    '04': "Апрель",
    '05': "Май",
    '06': "Июнь",
    '07': "Июль",
    '08': "Август",
    '09': "Сентябрь",
    '10': "Октябрь",
    '11': "Ноябрь",
    '12': "Декабрь"
}


def export_xml_xls_reestr():
    """Функция экспорта реестров XML и XLS"""
    # closing_day()  # вызов функции закрытия кассвоого дня

    current_date = ''
    current_bank = ''
    bank = ''
    wait_xml_form = 2
    wait_print_form = 3  # ожидание печатной формы

    print_log("Открытие журнала распред. ведомостей", line_before=True)
    selecting_menu(1, 3)  # Запуск журнала распред. ведомостей
    pg.press('end')  # переход к последней строке в журнале

    pg.press('left', presses=5)  # выбор крайнего левого столбца с датами

    eng_layout()
    pg.hotkey('ctrl', 'c')  # копирование в буфер обмена даты последней записи для сравнения в дальнейшем
    current_date = pyperclip.paste()  # запись в переменную даты последней записи в журнале

    i = 0
    for i in range(5):
        pg.press('left', presses=5)  # выбор крайнего левого столбца с датами

        eng_layout()
        pg.hotkey('ctrl', 'c')  # копирование в буфер обмена даты последней записи для сравнения в дальнейшем

        if pyperclip.paste() == current_date:  # сравнение по дате
            pg.press('right', presses=2, interval=0.1)  # выбор крайнего левого столбца с датами
            rus_layout()
            pg.hotkey('ctrl', 'c')  # копирование в буфер обмена текущего банка
            current_bank = pyperclip.paste()  # запись в переменную текущего банка

            if current_bank == 'Филиал  ВТБ (ПАО) в г. Нижнем Новгороде':  # переименование файлов
                bank = "ВТБ"
                wait_xml_form = 2
                wait_print_form = 2
            elif current_bank == 'Р-ИНКАС':
                bank = "РНКО"
                wait_xml_form = 7
                wait_print_form = 12
            elif current_bank == 'Газпромбанк':
                bank = "ГПБ"
                wait_xml_form = 2
                wait_print_form = 4
            elif current_bank == 'ВБРР Самарский филиал':
                bank = "ВБРР"
                wait_xml_form = 2
                wait_print_form = 2

            pg.press('enter')  # вход в последнюю запись

            print_log(f"Выгрузка файла XML Банка '{bank}'", line_before=True)
            pg.press('tab', presses=17, interval=0.1)  # выгрузка реестра в XML
            pg.press('space')
            time.sleep(wait_xml_form)
            pg.press('space')
            # TODO сделать копирование файлов XML в папку

            kassa_making_dirs(path=KASSA_PATH_REESTRY, bank=bank)  # создание каталогов для экспорта

            print_log("Выгрузка файла XLS", line_before=True)
            pg.press('tab', presses=1, interval=0.1)  # выгрузка реестра в XLS
            pg.press('space')
            pg.press('down')
            pg.press('enter')  # открытие печатной формы
            time.sleep(wait_print_form)  # ожидание печатной формы
            pg.hotkey('ctrl', 's')
            time.sleep(0.5)
            eng_layout()
            typing(KASSA_PATH_REESTRY)
            rus_layout()
            typing(bank)
            eng_layout()
            typing(f"\\{TODAY_YEAR}\\{DICT_MOUNTS.get(TODAY_MOUNT)}\\{SAMPLE_NAME} {TODAY_DATE}")  # генерируется
            # строка вида C:\Users\sonic\Desktop\Реестры\ВБРР\2022\Март\Реестр 11 03 2022
            saving_xls(f"Реестр по Банку '{bank}'")
            pg.press('esc')  # закрытие окна ведомости
            i += 1
            time.sleep(0.5)
            pg.press('up')  # выбор строки выше
            pg.press('left', presses=5)  # выбор крайнего левого столбца с датами

        else:  # если дата не совпадает
            break

        # TODO сделать высылку файлов
    # input()
