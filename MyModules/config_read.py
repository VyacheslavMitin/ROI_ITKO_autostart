# Модуль чтения конфига с настройками
# from MyModules.config_read import *

import configparser
import os

# КОНСТАНТЫ
name_curdir = os.path.basename(os.path.abspath(os.path.curdir))

if name_curdir == 'MyModules':
    path_ = os.path.abspath(os.path.join(os.path.curdir, '..')) + '\\'
else:
    path_ = os.path.abspath(os.path.join(os.path.curdir)) + '\\'

INI_FILE = 'config.ini'
PATH_TO_INI = path_ + INI_FILE

cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read(PATH_TO_INI)

ITKO_BIN = cfg.get('PATHS', 'itko_bin')
OUTLOOK_BIN = cfg.get('PATHS', 'outlook_bin')
CHANGE_TIME = cfg.get('PATHS', 'change_time')
# Блок для работы с путями к папкам
PATH_ITKO = cfg.get('PATHS', 'dir_itko')

PATH_SFORMIROVAT = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_sformirovat'))
PATH_014 = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_014'))
PATH_VSKK = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_vskk'))
PATH_VOU = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_vou'))
PATH_202 = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_202'))
PATH_PP = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_pp'))

dict_with_paths = {  # словарь с именами папок и путям к ним
    'root_dir': ('07 ITKO\\', PATH_ITKO),
    '014_dir': (cfg.get('PATHS', 'dir_014'), PATH_014),
    'vskk_dir': (cfg.get('PATHS', 'dir_vskk'), PATH_VSKK),
    'vou_dir': (cfg.get('PATHS', 'dir_vou'), PATH_VOU),
    '202_dir': (cfg.get('PATHS', 'dir_202'), PATH_202),
    'pp_dir': (cfg.get('PATHS', 'dir_pp'), PATH_PP),
    'exports_dir': (cfg.get('PATHS', 'dir_sformirovat'), PATH_SFORMIROVAT),
}

# Блок для работы с именами клиентов
NAMES_STR = cfg.get('NAMES', 'points')
NAMES_STR_double = cfg.get('NAMES', 'points_double')
# Блок для работы с письмами
RECIPIENTS_SFORMIROVAT = cfg.get('NAMES', 'recipients_sform')
RECIPIENTS_202 = cfg.get('NAMES', 'recipients_202')
RECIPIENTS_VOU = cfg.get('NAMES', 'recipients_vou')
RECIPIENTS_TEST = cfg.get('NAMES', 'recipients_test')
RECIPIENTS_COPY = cfg.get('NAMES', 'recipients_copy')
# Блок для определения монитора
# from MyModules.checking_monitor import checking_monitor
# COORDINATES_FOR_DISPLAY = checking_monitor(silent=True)
# Блок для определения расширений файлов для поиска
EXTENSIONS = cfg.get('PATHS', 'extensions')


if __name__ == '__main__':
    print(PATH_TO_INI)
    print(ITKO_BIN)
    print(OUTLOOK_BIN)
    print(CHANGE_TIME)
    print(PATH_ITKO)
    print(NAMES_STR)
    print(NAMES_STR_double)
    print(RECIPIENTS_SFORMIROVAT)
    print(RECIPIENTS_202)
    print(RECIPIENTS_VOU)
    print(EXTENSIONS)
