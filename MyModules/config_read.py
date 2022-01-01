# Модуль чтения конфига
# from MyModules.config_read import *

import configparser
import os

# КОНСТАНТЫ
cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')
ITKO_DIR = cfg.get('PATHS', 'dir_itko')
ITKO_BIN = cfg.get('PATHS', 'itko_bin')
EXPORT_DIR = cfg.get('PATHS', 'dir_exports')

PATH_014 = os.path.join(ITKO_DIR, cfg.get('PATHS', 'dir_014'))
PATH_VSKK = os.path.join(ITKO_DIR, cfg.get('PATHS', 'dir_vskk'))
PATH_VOU = os.path.join(ITKO_DIR, cfg.get('PATHS', 'dir_vou'))
PATH_EXPORTS = os.path.join(ITKO_DIR, cfg.get('PATHS', 'dir_exports'))

NAMES_STR = cfg.get('NAMES', 'points')
NAMES_STR_double = cfg.get('NAMES', 'points_double')