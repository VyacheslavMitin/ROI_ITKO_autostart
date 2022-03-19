# Модуль создания каталогов для выгрузки файлов

import datetime
from MyModules.config_read import *

TODAY_YEAR = datetime.date.today().strftime("%Y")
TODAY_MOUNTH = datetime.date.today().strftime("%m")

DICT_MOUNTS = {
    '01': "Январь",
    '02': "Февраль",
    '03': "Март",
    '04': "Апрель",
    '05': "Май",
    '06': "Июнь",
    '07': "Июль",
    '08': "Август",
    '09': "Сентябрь",
    '10': "Октябрь",
    '11': "Ноябрь",
    '12': "Декабрь"
}

tuple_dirs = (PATH_014, PATH_VSKK, PATH_VOU, PATH_SFORMIROVAT, PATH_202, PATH_PP)  # кортеж для выручки


def making_dirs():
    """Функция создания каталогов для файлов экспорта"""
    if os.getlogin() == MY_LOGIN:
        for item in tuple_dirs:
            os.makedirs(os.path.normpath(item), exist_ok=True)


def kassa_making_dirs(path, bank):
    """Функция создания каталогов для документов кассы"""
    string_path = os.path.normpath(f'{path}//{bank}//{TODAY_YEAR}//{DICT_MOUNTS.get(TODAY_MOUNTH)}//')
    os.makedirs(string_path, exist_ok=True)

    return string_path


if __name__ == '__main__':
    making_dirs()
    kassa_making_dirs(path=KASSA_PATH_REESTRY, bank='ВБРР')
