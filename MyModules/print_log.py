# Модуль вывода в консоль записи текущих действий

import time


def print_log(text: str, line_before: bool = False, line_after: bool = False, bell: bool = False) -> None:
    """Функция формирования читабельной записи текущего действия.
    Аргументы line_before (bool), line_after (bool) для необходимости новых линий ДО и ПОСЛЕ вывода.
    Аргумент bell (bool) для звукового сигнала"""

    def time_log():
        """Функция формирования читабельной записи текущего времени (без даты)."""
        log_time = time.strftime("%H:%M:%S")  # формат '10:10:10'
        return log_time

    if line_before:  # линия ДО вывода сообщения
        print()  # пустая строка

    print(f" {time_log()} | {text}")  # формат ' 13:05:02 | Текст'

    if line_after:  # линия ПОСЛЕ вывода сообщения
        print()  # пустая строка

    if bell:
        print("\a")
