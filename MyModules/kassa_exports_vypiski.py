# Модуль экспорта файлов выписок

# Импорты
import time
import pyautogui as pg
from MyModules.config_read import *
from MyModules.finding import working_find
from MyModules.past_dates import past_dates, period_for_emails
from MyModules.print_log import print_log
from MyModules.switch_layout import eng_layout, rus_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.select_menu import selecting_menu
from MyModules.save_file_xls import saving_xls


# Функции
def export_vypiski():
    """Функция экспорта выписок по клиентам"""
    print_log("Экспорт выписок из реестра", line_before=True)
    selecting_menu(1, 13)  # запуск обработки

    pg.press('tab', presses=2)
    pg.press('esc')  # закрытие окна
    pg.press('tab', presses=5)

    pg.press('end')  # выбор первой базы в списке баз
    pg.press('enter')

    pg.press('tab', presses=5)
    pg.press('space')

    working_find("магнит")
    pg.press('enter')
    pg.press('esc')  # закрытие окна

    pg.press('tab', presses=3)
    # TODO доделать
    input()
