# Модуль чтения конфига с настройками
# from MyModules.config_read import *

import configparser
import os
import datetime

# КОНСТАНТЫ
NOW_DATE = datetime.datetime.now().strftime('%d.%m.%y')  # Текущая дата в формате 01.01.22
name_curdir = os.path.basename(os.path.abspath(os.path.curdir))  # путь к текущей директории

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

# Пути для выручки
PATH_SFORMIROVAT = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_sformirovat'))
PATH_014 = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_014'))
PATH_VSKK = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_vskk'))
PATH_VOU = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_vou'))
PATH_202 = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_202'))
PATH_PP = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_pp'))
PATH_CLIENTS = os.path.join(PATH_ITKO, cfg.get('PATHS', 'dir_clients'))

# Пути для кассовой рутины
KASSA_ITKO_BIN = cfg.get('KASSA', 'kassa_itko_bin')
KASSA_PATH_REESTRY = cfg.get('KASSA', 'path_reestry')
KASSA_PATH_VYPISKI = cfg.get('KASSA', 'path_vypiski')
KASSA_PATH_XML_FROM = cfg.get('KASSA', 'path_xml_from')
KASSA_PATH_XML_TO = cfg.get('KASSA', 'path_xml_to')
# Получатели писем кассы
KASSA_RECIPIENTS_SAMARA = cfg.get('KASSA', 'xml_reestr_samara')
KASSA_RECIPIENTS_VBRR = cfg.get('KASSA', 'xml_reestr_vbrr')
KASSA_RECIPIENTS_VTB = cfg.get('KASSA', 'xml_reestr_vtb')


dict_with_paths = {  # словарь с именами папок и путям к ним
    'root_dir': ('07 ITKO\\', PATH_ITKO),
    '014_dir': (cfg.get('PATHS', 'dir_014'), PATH_014),
    'vskk_dir': (cfg.get('PATHS', 'dir_vskk'), PATH_VSKK),
    'vou_dir': (cfg.get('PATHS', 'dir_vou'), PATH_VOU),
    '202_dir': (cfg.get('PATHS', 'dir_202'), PATH_202),
    'pp_dir': (cfg.get('PATHS', 'dir_pp'), PATH_PP),
    'clients_dir': (cfg.get('PATHS', 'dir_clients'), PATH_CLIENTS),
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

# Имена пользователей в системах
MY_LOGIN = cfg.get('NAMES', 'my_login')
KASSA_LOGIN = cfg.get('NAMES', 'regina_login')

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
    print(MY_LOGIN)
    print(KASSA_LOGIN)
    print(KASSA_PATH_REESTRY)
    print(KASSA_PATH_VYPISKI)
    print(KASSA_PATH_XML_FROM)
    print(KASSA_PATH_XML_TO)
    print(KASSA_RECIPIENTS_SAMARA)
    print(KASSA_RECIPIENTS_VBRR)
    print(KASSA_RECIPIENTS_VTB)
