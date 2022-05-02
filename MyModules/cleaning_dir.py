# Модуль для очистки каталогов
import time
import glob
import os
from MyModules.print_log import print_log


def cleaning_dir(path0_: str):
    """Функция удаления файлов в каталоге экспортов"""
    print_log("Очистка каталога экспорта")

    for files in glob.glob(path0_ + f'*.*'):
        os.remove(files)
    time.sleep(0.5)
