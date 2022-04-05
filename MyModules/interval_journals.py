# Модуль переключения периодов в журналах ИТКО
# from MyModules.interval_journals import interval_january

import pyautogui as pg
from MyModules.past_dates import past_dates
from MyModules.typing_unicode_str import typing_unicode_str as typing
from MyModules.config_read import NOW_DATE


def interval_january(long_=False):
    """Функция определения интервалов: если январь и нужен доступ к документам прошлого года"""
    def clear_dates():
        pg.press('right', presses=20, interval=0.0)
        pg.press('backspace', presses=20, interval=0.0)

    if past_dates()[3] == '12':
        time_sec = 0
        pg.press('alt')
        pg.press('right', presses=1, interval=time_sec)
        pg.press('down', presses=12, interval=time_sec)
        if long_:
            pg.press('down', presses=4, interval=time_sec)
        pg.press('enter')
        clear_dates()
        typing(past_dates()[0])
        pg.press('tab')
        clear_dates()
        typing(NOW_DATE)
        pg.press('tab')
        pg.press('enter')
