# Модуль поиски файлов (для кассы)

import os
import time
import sys
import glob
from MyModules.config_read import *
from MyModules.print_log import print_log


def search_files_to_send(bank, path, printable=False, technical=False):
    """Функция подготовки списка файлов на отправку"""
    print_log(f"Сбор документов для отправки", line_after=False)

    for bank, path in KASSA_PATH_XML:
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