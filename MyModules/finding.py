# Модуль работы с поиском по клиентам

import pyautogui as pg
from MyModules.switch_layout import eng_layout, rus_layout
from MyModules.typing_unicode_str import typing_unicode_str as typing


def working_find(name):
    """Функция работы с поиском"""
    pg.press('home')
    pg.hotkey('ctrl', 'F3')
    pg.press('delete', presses=50)
    rus_layout()
    typing(name)  # имя в поисковое окно
    pg.press('enter')  # поиск
