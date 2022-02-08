# Модуль создания каталогов для выгрузки файлов

from MyModules.config_read import *

tuple_dirs = (PATH_014, PATH_VSKK, PATH_VOU, PATH_SFORMIROVAT, PATH_202, PATH_PP)


def making_dirs():
    """Функция создания каталогов для файлов экспорта"""
    for item in tuple_dirs:
        os.makedirs(os.path.normpath(item), exist_ok=True)


if __name__ == '__main__':
    making_dirs()
