# Модуль экспорта реестров в XML и XLS

import datetime
import time
import pyperclip
import pyautogui as pg
from MyModules.config_read import *
from MyModules.kassa_close_day import closing_day
from MyModules.select_menu import selecting_menu
from MyModules.print_log import print_log
from MyModules.save_file_xls import saving_xls
from MyModules.switch_layout import rus_layout, eng_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.making_dirs import kassa_making_dirs
from MyModules.kassa_searching_copy_xmls import copy_xml
from MyModules.kassa_sending_files import sending_outlook

TODAY_YEAR = datetime.date.today().strftime("%Y")
TODAY_DATE = datetime.date.today().strftime("%d %m %Y")
TODAY_MOUNT = datetime.date.today().strftime("%m")
SAMPLE_NAME = "Реестр"
TUPLE_BANKS = ("ВБРР", "ВТБ", "РНКО", "ГПБ")

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


# Функции
def export_xml_xls_reestr():
    """Функция экспорта реестров XML и XLS"""
    if os.getlogin() == KASSA_LOGIN:
        # pass
        closing_day()  # вызов функции закрытия кассового дня

    current_date = ''
    current_bank = ''
    bank = ''
    wait_xml_form = 2
    wait_print_form = 3  # ожидание печатной формы

    print_log("Открытие журнала распред. ведомостей", line_before=True)
    selecting_menu(1, 3)  # Запуск журнала распред. ведомостей
    pg.press('end')  # переход к последней строке в журнале

    pg.press('left', presses=5, interval=0.3)  # выбор крайнего левого столбца с датами

    eng_layout()
    pg.hotkey('ctrl', 'c')  # копирование в буфер обмена даты последней записи для сравнения в дальнейшем
    current_date = pyperclip.paste()  # запись в переменную даты последней записи в журнале

    i = 0
    for i in range(5):
        pg.press('left', presses=5, interval=0.3)  # выбор крайнего левого столбца с датами

        eng_layout()
        pg.hotkey('ctrl', 'c')  # копирование в буфер обмена даты последней записи для сравнения в дальнейшем

        if pyperclip.paste() == current_date:  # сравнение по дате
            pg.press('right', presses=2, interval=0.3)  # выбор столбца с банком
            rus_layout()
            pg.hotkey('ctrl', 'c')  # копирование в буфер обмена имени текущего банка
            current_bank = pyperclip.paste()  # запись в переменную текущего банка

            if current_bank == 'Филиал  ВТБ (ПАО) в г. Нижнем Новгороде':  # переименование файлов
                bank = "ВТБ"
                wait_xml_form = 3
                wait_print_form = 3
            elif current_bank == 'Р-ИНКАС':
                bank = "РНКО"
                wait_xml_form = 10
                wait_print_form = 15
            elif current_bank == 'Газпромбанк':
                bank = "ГПБ"
                wait_xml_form = 6
                wait_print_form = 7
            elif current_bank == 'ВБРР Самарский филиал':
                bank = "ВБРР"
                wait_xml_form = 3
                wait_print_form = 3

            pg.press('enter')  # вход в последнюю запись

            print_log(f"Выгрузка файла XML Банка '{bank}'", line_before=True)
            pg.press('tab', presses=18, interval=0.3)  # выгрузка реестра в XML
            time.sleep(0.5)
            pg.press('space')  # нажать кнопку выгрузки
            time.sleep(wait_xml_form)
            pg.press('space')

            kassa_making_dirs(path=KASSA_PATH_REESTRY, bank=bank)  # создание каталогов для экспорта

            print_log("Выгрузка файла XLS", line_before=True)
            pg.press('tab', presses=1, interval=0.3)  # выгрузка реестра в XLS
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
            pg.press('left', presses=5, interval=0.3)  # выбор крайнего левого столбца с датами

        else:  # если дата не совпадает
            break

    copy_xml()  # копирование XML

    print_log("Отправка реестров XLS и XML получателям", line_before=True)
    for item in TUPLE_BANKS:  # отправка реестров
        sending_outlook(mode='XML_РЕЕСТРЫ',
                        path=KASSA_PATH_XML_TO,
                        bank=item,
                        displayed=True)
    # subprocess.Popen(OUTLOOK_BIN)  # запуск MS Outlook
    # КОНЕЦ ФУНКЦИИ


# if __name__ == '__main__':
#     export_xml_xls_reestr()
