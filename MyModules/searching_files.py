# Модуль поиски файлов (для кассы)

import os
import time
import sys
import datetime
import glob
from MyModules.config_read import *
from MyModules.print_log import print_log

TODAY_DATE = datetime.date.today().strftime('%d.%m.%Y')
TODAY_YEAR = datetime.date.today().strftime("%Y")
TODAY_MOUNTH = datetime.date.today().strftime("%m")

PATH_VBRR = f'{PATH_BANKS}/ВБРР/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_VTB = f'{PATH_BANKS}/ВТБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_RNKO = f'{PATH_BANKS}/РНКО/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
# проверка вложенной папки в ГПБ
PATH_GPB = f'{PATH_BANKS}/ГПБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/{datetime.date.today().strftime("%d %m %Y")}/'
if os.path.isdir(f'{PATH_GPB}/{datetime.date.today().strftime("%d %m %Y")}/'):
    PATH_GPB = f'{PATH_GPB}/{datetime.date.today().strftime("%d %m %Y")}/'

DICT_BANKS = {  # словарь с путями для банков
    "ВБРР": os.path.join(PATH_VBRR),
    "ВТБ": os.path.join(PATH_VTB),
    "РНКО": os.path.join(PATH_RNKO),
    "ГПБ": os.path.join(PATH_GPB),
}

FILES_VBRR, FILES_VTB, FILES_RNKO, FILES_GPB = [], [], [], []
DICT_FILES = {  # словарь с пустыми списками файлов
    "ВБРР": FILES_VBRR,
    "ВТБ": FILES_VTB,
    "РНКО": FILES_RNKO,
    "ГПБ": FILES_GPB,
}


def search_files(path, bank, printable=False, technical=False):
    """Функция подготовки списка файлов на отправку"""
    print_log(f"Сбор документов для отправки", line_after=False)

    for path, bank in KASSA_PATH_XML:
        # Получение в лист всех файлов в каталоге
        list_of_files = filter(os.path.isfile,
                               glob.glob(path + '*'))

        # Сортировка листа с файлами по дате
        list_of_files = sorted(list_of_files,
                               key=os.path.getmtime)

        for file in list_of_files:  # Итерация по листу с файлами и получение дат файлов
            try:
                timestamp_str = time.strftime('%d.%m.%Y',
                                              time.gmtime(os.path.getmtime(file)))
                if timestamp_str == TODAY_DATE:  # проверка по текущей дате
                    if printable:
                        # print(timestamp_str, ' -->', file)
                        print(file)
                    if bank == "ВБРР":
                        FILES_VBRR.append(os.path.normpath(file))
                    elif bank == "ВТБ":
                        FILES_VTB.append(os.path.normpath(file))
                    elif bank == "РНКО":
                        FILES_RNKO.append(os.path.normpath(file))
                    elif bank == "ГПБ":
                        FILES_GPB.append(os.path.normpath(file))
            except FileNotFoundError:  # если нет каталога или файла
                pass

    if technical:  # вывод списка в принте если нужно
        print("\nСловарь:")
        for key, values in DICT_FILES.items():
            if values:
                print(f"Банк '{key}', файлы {values}")