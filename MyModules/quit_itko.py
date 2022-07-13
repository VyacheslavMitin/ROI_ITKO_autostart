import pyautogui as pg
import os
from MyModules.making_dirs import kassa_making_dirs


def quit_1c(name_, path1_):
    """Функция выхода из 1С и запуска проводника"""
    pg.hotkey('alt', 'f4')

    if name_:  # поиск дубликатов открытых папок
        name_ = name_[:-1]
        if name_ in pg.getAllTitles():  # поиск открытой папки
            list__ = []
            for i in pg.getAllTitles():
                if i == name_:
                    list__.append(i)
            for item in enumerate(list__):
                pg.getWindowsWithTitle(item[1])[item[0]].close()

    if path1_:
        os.system(f'explorer.exe {os.path.normpath(path1_)}')  # запуск проводника


def kassa_quit_1c(path):
    pg.hotkey('alt', 'f4')
    os.system(f'explorer.exe {os.path.normpath(path)}')  # запуск проводника
