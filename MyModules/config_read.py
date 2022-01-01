# Модуль чтения конфига
# from MyModules.config_read import *

import configparser
import os

# КОНСТАНТЫ
cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read('config.ini')

ITKO_BIN = cfg.get('PATHS', 'itko_bin')

PATH_ITKO = cfg.get('PATHS', 'dir_itko')

PATH_EXPORTS = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_exports'))
PATH_014 = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_014'))
PATH_VSKK = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_vskk'))
PATH_VOU = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_vou'))
PATH_202 = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_202'))


NAMES_STR = cfg.get('NAMES', 'points')
NAMES_STR_double = cfg.get('NAMES', 'points_double')

RECIPIENTS_SFORMIROVAT = cfg.get('NAMES', 'recipients_sform')
RECIPIENTS_202 = cfg.get('NAMES', 'recipients_sform')
