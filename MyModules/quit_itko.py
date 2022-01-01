import pyautogui as pg
from MyModules.config_read import *


def quit_1c(name_='07 ITKO', path_=ITKO_DIR):
    """Функция выхода из 1С и запуска проводника"""
    pg.hotkey('alt', 'F4')  # выход из кассы пересчета

    if name_ in pg.getAllTitles():  # поиск открытой папки
        list__ = []
        for i in pg.getAllTitles():
            if i == name_:
                list__.append(i)
        for item in enumerate(list__):
            pg.getWindowsWithTitle(item[1])[item[0]].close()

    os.system(f'explorer.exe {os.path.normpath(path_)}')  # запуск проводника
