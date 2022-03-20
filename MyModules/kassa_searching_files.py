# Модуль поиски файлов (для кассы)

# Импорты
import os
import time
import datetime
import glob
from MyModules.config_read import KASSA_PATH_XML_FROM, KASSA_PATH_XML_TO
from MyModules.print_log import print_log
from MyModules.making_dirs import kassa_making_dirs

# Константы
TODAY_DATE = datetime.date.today().strftime('%d.%m.%Y')

PATH_VBRR_FROM = f'{KASSA_PATH_XML_FROM}/ВБРР Самарский филиал/'
PATH_VTB_FROM = f'{KASSA_PATH_XML_FROM}/Филиал  ВТБ (ПАО) в г Нижнем Новгороде/'
PATH_RNKO_FROM = f'{KASSA_PATH_XML_FROM}/Р-ИНКАС/'
PATH_GPB_FROM = f'{KASSA_PATH_XML_FROM}/Газпромбанк/'

DICT_BANKS_FROM = {  # словарь с путями для банков
    "ВБРР": os.path.join(PATH_VBRR_FROM),
    "ВТБ": os.path.join(PATH_VTB_FROM),
    "РНКО": os.path.join(PATH_RNKO_FROM),
    "ГПБ": os.path.join(PATH_GPB_FROM),
}

FILES_VBRR, FILES_VTB, FILES_RNKO, FILES_GPB = [], [], [], []
DICT_FILES = {  # словарь с пустыми списками файлов
    "ВБРР": FILES_VBRR,
    "ВТБ": FILES_VTB,
    "РНКО": FILES_RNKO,
    "ГПБ": FILES_GPB,
}


# Функции
def search_files(printable=False, technical=False):
    """Функция подготовки списка файлов на отправку"""

    for bank, path in DICT_BANKS_FROM.items():
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

    if technical:  # вывод списка в print если нужно
        print("Файлы XML:")
        for key, values in DICT_FILES.items():
            if values:
                print(f"Банк '{key}', файл '{values[0]}'")


if __name__ == '__main__':
    search_files()
