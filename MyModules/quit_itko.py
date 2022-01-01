import pyautogui as pg
from MyModules.config_read import *

dct = {
    'root_dir': ('07 ITKO\\', PATH_ITKO),
    '014_dir': (cfg.get('PATHS', 'dir_014'), PATH_014),
    'vskk_dir': (cfg.get('PATHS', 'dir_vskk'), PATH_VSKK),
    'vou_dir': (cfg.get('PATHS', 'dir_vou'), PATH_VOU),
    'exports_dir': (cfg.get('PATHS', 'dir_exports'), PATH_EXPORTS),
}


def quit_1c(name_, path_):
    """Функция выхода из 1С и запуска проводника"""
    # pg.hotkey('alt', 'F4')  # выход из кассы пересчета
    name_ = name_[:-1]
    if name_ in pg.getAllTitles():  # поиск открытой папки
        list__ = []
        for i in pg.getAllTitles():
            if i == name_:
                list__.append(i)
        for item in enumerate(list__):
            pg.getWindowsWithTitle(item[1])[item[0]].close()

    os.system(f'explorer.exe {os.path.normpath(path_)}')  # запуск проводника
