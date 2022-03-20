# Модуль проверки сети (для кассы)

import os
import sys
from MyModules.config_read import *
from MyModules.print_log import print_log


def network_work():
    """Функция работы с сетью"""
    print_log("Проверка включенной кассовой сети", line_after=True)

    if not os.path.isdir(KASSA_PATH_XML_FROM):
        print("\nНеобходимо включить кассовую сеть если это не произошло и перезапустить программу!\n".upper())
        input()
        sys.exit("Кассовая сеть не включена!")
    else:
        print_log("Кассовая сеть включена, продолжаем работу")

    # os.system(f"explorer.exe {KASSA_PATH_XML_FROM}")


if __name__ == '__main__':
    network_work()
