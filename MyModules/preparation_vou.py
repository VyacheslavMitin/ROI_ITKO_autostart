# Модуль расчета ВОУ

import time
from MyModules.print_log import print_log


def preparation_vou():
    """Функция запуска расчета ВОУ"""
    print_log("Запуск расчета ВОУ", line_before=True)
    from MyModules.select_menu import selecting_menu
    selecting_menu(1, 5)  # запуск журнала воу
    from MyModules.interval_journals import interval_january
    interval_january()
    selecting_menu(2, 6)  # запуск авто формирования
    time.sleep(5)
