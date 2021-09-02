# Модуль работы с ИТКО
# pip install pyautogui

from datetime import datetime
import pyautogui as pg
import subprocess
import configparser
import time

ITKO_BIN = 'C:/1Cv77/BIN/1cv7.exe'

cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')  # чтение файла settings_common.ini в папке модуля
NAME_1 = cfg.get('NAMES', 'РТК')  # РТК
NAME_2 = cfg.get('NAMES', 'электротехмонтаж')  # электротехмонтаж
NAME_3 = cfg.get('NAMES', 'автопитер')  # автопитер
NAME_4 = cfg.get('NAMES', 'ситилинк')  # ситилинк
NAME_5 = cfg.get('NAMES', 'скартел')  # скартел
NAME_6 = cfg.get('NAMES', 'вымпелком')  # вымпелком
NAME_7 = cfg.get('NAMES', 'мегафон')  # мегафон
NAME_8 = cfg.get('NAMES', 'мэлон')  # мэлон
NAME_9 = cfg.get('NAMES', 'сапв')  # сапв

NAMES = []  # кортеж с контрагентами


# Функции
def past_dates(year=21):
    """Функция расчета конечных дат прошлого месяца в строковом исполнении
    Возвращает дату прошлого месяца: 0 и 1 даты начала/конца месяца, 2 год, 3 месяц, 4 месяц в формате '01 Jan'."""
    past_start_date_, past_finish_date_, past_month_str, past_number_month = '01.01.2021', '31.01.2021', '01', '01 Jan'
    now_month = datetime.now().month  # текущий месяц в цифровом представлении
    now_year = datetime.now().year  # текущий год в цифровом представлении

    if now_month == 1:  # отлов января и реакция на него, вычитания года и явное указания декабря
        past_month_str = str(12)  # в строковом исполнении явное указания декабря
        past_year = now_year - 1  # вычитание года в цифровом исполнении
        past_start_date_ = '01' + f'.{past_month_str}.{year}'  # 01 декабря прошлого года
        past_finish_date_ = '31' + f'.{past_month_str}.{year}'  # 31 декабря прошлого года
        past_number_month = '12 Dec'

    else:  # все остальные месяцы кроме января
        past_month = now_month - 1  # вычитание месяца
        past_year = now_year  # год тот же что и текущий
        past_number_month = datetime(past_year, past_month, 1).strftime('%m %b')  # в формате "01 Jan"

        if past_month in [4, 6, 9, 11]:  # апрель, июнь, сентябрь, ноябрь
            if len(str(past_month)) == 1:  # если месяц из 1 символа то конкатенация с '0'
                past_month_str = '0' + str(past_month)  # апрель, июнь, сентябрь
            past_start_date_ = '01' + f'.{past_month_str}.{year}'
            past_finish_date_ = '30' + f'.{past_month_str}.{year}'

        elif past_month in [1, 3, 5, 7, 8, 10]:  # январь, март, май, июль, август, октябрь
            if len(str(past_month)) == 1:  # если месяц из 1 символа то конкатенация с '0'
                past_month_str = '0' + str(past_month)  # январь, март, май, июль, август
            past_start_date_ = '01' + f'.{past_month_str}.{year}'
            past_finish_date_ = '31' + f'.{past_month_str}.{year}'

        elif past_month == 2:  # февраль
            past_month_str = '02'  # февраль в строковом представлении
            if ((past_year - 2020) % 4) == 0:  # если (год - 2020) делится без остатка то високосный
                past_finish_date_ = '29' + f'.{past_month_str}.{year}'  # февраль високосного
            else:  # а если нет то обычный
                past_finish_date_ = '28' + f'.{past_month_str}.{year}'  # февраль не високосного
            past_start_date_ = '01' + f'.02.{year}'

    return past_start_date_, past_finish_date_, past_year, past_month_str, past_number_month  # возврат функции


def welcoming(name_='ИТКО', author_='Вячеслав Митин', version_='0.1'):
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'")
    print()


def start_itko():
    starting = subprocess.Popen([
        ITKO_BIN
    ])

    time.sleep(2)
    pg.press('enter', presses=4, interval=1)
    pg.press('tab', presses=2, interval=1)
    pg.press('enter')


def call_exports():
    pg.click(1000, 150)


def configuring_exports():
    time.sleep(1)
    pg.write(past_dates()[0])
    pg.press('tab')
    time.sleep(1)
    pg.write(past_dates()[1])
    pg.press('tab', presses=2, interval=1)


def clearing_file_find():
    pg.click(415, 75)  # переход в поле поиска
    time.sleep(1)
    pg.press('backspace', presses=20)


def searching_exporting():
    pg.press('pageup')
    pg.hotkey('alt', 'shift')
    time.sleep(1)
    pg.write(name1, interval=0.75)
    pg.hotkey('shift', 'F3')
    pg.press('enter')
    pg.press('tab')
    pg.press('enter')
    time.sleep(1)
    pg.hotkey('ctrl', 'F4')
    time.sleep(1)
    pg.hotkey('ctrl', 's')
    time.sleep(1)
    pg.write(name1)
    pg.press('tab')
    pg.press('down', presses=2)
    pg.press('tab')
    pg.press('enter', presses=2, interval=1)
    time.sleep(1)
    pg.hotkey('ctrl', 'F4')
    time.sleep(1)


def cycling_exports():



welcoming()
start_itko()
call_exports()
configuring_exports()
clearing_file_find()
searching_exporting()
