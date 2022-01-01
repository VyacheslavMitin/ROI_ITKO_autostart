# Модуль работы с ИТКО (выгрузка отчетов "сформировать")

# ИМПОРТЫ
import glob
from datetime import datetime
import subprocess
import pyautogui as pg
import time
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.print_log import print_log
from MyModules.quit_itko import quit_1c
from MyModules.config_read import *

# КОНСТАНТЫ
NOW_DATE = datetime.now().strftime('%d.%m.%y')  # Текущая дата в фоммате 01.01.22


# ФУНКЦИИ
def welcoming(name_='ИТКО', author_='Вячеслав Митин', version_='5'):
    print(f"МОДУЛЬ РАБОТЫ С '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


def start_itko(point='buh', mode='ENTERPRISE', no_windows=True):
    """Функция запуска 1С 7 ИТКО"""
    print_log(f"Запуск ИТКО в  режиме {mode}")

    subprocess.Popen([
        ITKO_BIN,
        mode
    ])

    time.sleep(1)
    pg.press('tab', presses=2)
    pg.press('home')  # выбор первой базы в списке баз
    pg.press('enter')
    pg.hotkey('shift', 'tab')
    pg.press('home')  # выбор администратора для точки отсчета

    if point == 'buh':  # выбор бухгалтера
        print_log("Выбор Бухгалтера для входа")
        pg.press('down', presses=7)
    elif point == 'adm':  # оставить администратора
        print_log("Выбор Администратора для входа")

    pg.press('enter', presses=4, interval=0.5)
    pg.press('tab', presses=2, interval=0.5)
    pg.press('enter')

    if point == 'buh' and mode == 'ENTERPRISE':  # оставить администратора
        time.sleep(0.5)
        pg.click(10, 680)
        if not no_windows:
            print_log("Открытие окон")
            tuple_ = ((750, 115), (85, 85))
            for i in tuple_:
                pg.click(i)

    if point == 'adm' and mode == 'ENTERPRISE':  # оставить администратора
        print_log("Открытие журнала ВОУ")
        time.sleep(0.5)
        pg.press('alt')
        pg.press('right', presses=4, interval=0.1)
        pg.press('down', presses=5, interval=0.1)
        pg.press('enter')
        print_log("Открытие журнала документов")
        time.sleep(0.5)
        pg.press('alt')
        pg.press('right', presses=2, interval=0.1)
        pg.press('down', presses=1, interval=0.1)
        pg.press('enter', presses=2, interval=0.5)

    if mode == 'CONFIG':
        print_log("Открытие окна для загрузки базы", line_before=True)
        pg.press('alt')
        pg.press('right', presses=3, interval=0.1)
        pg.press('down', presses=5, interval=0.1)
        pg.press('enter')
        pg.press('tab')
        pg.press('enter')
        from MyModules.typing_unicode_str import typing_unicode_str
        typing_unicode_str(ITKO_DIR)
        pg.press('enter')


def success_window_alert():
    time.sleep(1)
    pg.alert("Автоматизация завершена", title="Завершено")
    print_log("Автоматизация завершена", line_before=True)


def change_datetime():
    print_log("Изменение даты/времени", line_before=True)
    file = 'change_datetime.lnk'
    import os
    os.system(file)


def preparation_vou():
    print_log("Запуск расчета ВОУ", line_before=True)
    pg.click(750, 85)
    pg.click(650, 85)


def export_014():
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
    typing(PATH_VSKK + f'VSKK OKO ALL {past_dates()[3]} {past_dates()[2]}.txt')
    pg.press('tab')
    pg.press('enter')
    time.sleep(5)
    pg.press('enter')


def export_vou():
    print_log("Работа с ВОУ", line_before=True)
    import pyperclip
    from MyModules.past_dates import past_dates

    print_log("Экспорт ВОУ в текстовый файл")
    pg.click(885, 85)  # экспорт файла
    pg.press('tab', presses=9, interval=0.2)
    pg.write(past_dates()[1])
    pg.press('tab')
    pg.write(past_dates()[0])
    pg.press('tab')
    typing(PATH_VOU + f'VOU_OKO.txt')
    pg.press('tab')
    pg.press('enter')
    time.sleep(3)

    print_log("Генерация XLS файла")
    pg.click(785, 85)  # вызов журнала с ведомостями
    if past_dates()[3] == '12':
        pg.press('alt')
        pg.press('right', presses=1, interval=0.1)
        pg.press('down', presses=12, interval=0.1)
        pg.press('enter')

        def clear_dates():
            pg.press('right', presses=10, interval=0.1)
            pg.press('backspace', presses=10, interval=0.1)

        clear_dates()
        typing(past_dates()[0])
        pg.press('tab')
        clear_dates()
        typing(past_dates()[1])
        pg.press('tab')
        pg.press('enter')
        # input('')
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
    typing(PATH_VOU + f'VOU_OKO_{pyperclip.paste()}')
    pg.press('tab')
    pg.press('down', presses=2)  # выбор формата файла
    pg.press('enter', presses=2)  # сохранение файла
    time.sleep(0.5)

    print_log("Генерация DBF файла")
    pg.click(1025, 85)  # открытие обработки для превращения в ДБФ
    pg.press('f4')
    time.sleep(0.5)
    typing(f'VOU_OKO_{past_dates()[0]}_{past_dates()[1]}.txt')
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


def cleaning_dir(path_: str):
    """Функция удаления файлов в каталоге экспортов"""
    print_log("Очистка каталога экспорта")

    for files in glob.glob(path_ + f'*.*'):
        os.remove(files)
    time.sleep(0.5)


def pyautogui_menu() -> str:
    """Функция МЕНЮ"""
    print_log("Запуск меню")

    menu_points = {
        0: 'Загрузка базы ИТКО',
        1: 'Старт ИТКО Бухгалтером',
        2: 'Старт ИТКО Администратором',
        3: "Подготовка к формированию ВОУ",
        4: "Файлы 'Сформировать.xls'",
        5: "Выгрузка '014'",
        6: "Выгрузка 'ВСКК'",
        7: "Выгрузка 'ВОУ'",
        9: "Поменять системные дату/время"
    }

    return pg.prompt(text=f"""
    Необходимо выбрать пункт меню:
    
    0: {menu_points.get(0)}
    =========================
    1: {menu_points.get(1)}
    2: {menu_points.get(2)}
    =========================
    3: {menu_points.get(3)}
    =========================
    4: {menu_points.get(4)}
    5: {menu_points.get(5)}
    6: {menu_points.get(6)}
    7: {menu_points.get(7)}
    =========================
    9: {menu_points.get(9)}
    """, title='МЕНЮ АВТОМАТИЗАЦИИ ИТКО', default='4')


if __name__ == '__main__':
    welcoming()

    select = pyautogui_menu()
    if select == '0':
        start_itko(point='adm', mode='CONFIG')

    elif select == '1':
        start_itko(point='buh', no_windows=False)

    elif select == '2':
        start_itko(point='adm')

    elif select == '3':
        change_datetime()
        start_itko()
        preparation_vou()

    elif select == '4':
        from MyModules.exporting_xls import *
        start_itko(point='buh')
        cleaning_dir(EXPORT_PATH)
        cycling_exports()
        quit_1c()

    elif select == '5':
        start_itko(point='buh')
        export_014()
        quit_1c()

    elif select == '6':
        start_itko(point='buh')
        export_vskk()
        quit_1c()

    elif select == '7':
        start_itko(point='buh')
        export_vou()
        quit_1c()

    elif select == '9':
        change_datetime()

    success_window_alert()
