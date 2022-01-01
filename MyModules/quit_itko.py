import configparser
import pyautogui as pg
import os

cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')
ITKO_DIR = cfg.get('PATHS', 'dir_itko')


def quit_1c(name_='07 ITKO'):
    """Функция выхода из 1С и запуска проводника"""
    pg.hotkey('alt', 'F4')  # выход из кассы пересчета

    if name_ in pg.getAllTitles():
        list__ = []
        for i in pg.getAllTitles():
            if i == name_:
                list__.append(i)
        for item in enumerate(list__):
            pg.getWindowsWithTitle(item[1])[item[0]].close()

    os.system(f'explorer.exe {os.path.normpath(ITKO_DIR)}')  # запуск
