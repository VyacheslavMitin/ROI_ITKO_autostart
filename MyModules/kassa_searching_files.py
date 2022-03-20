# Модуль поиски файлов (для кассы)

# Импорты
import time
import datetime
import glob
from MyModules.config_read import *
from MyModules.print_log import print_log

# Константы
TODAY_DATE = datetime.date.today().strftime('%d.%m.%Y')
TODAY_YEAR = datetime.date.today().strftime("%Y")
TODAY_MONTH = datetime.date.today().strftime("%m")
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


# Функции
def search_files(
        path,  # путь до корневого каталога с файлами по банкам
        bank,  # название банка
        printable=True):  # печатать информацию
    """Функция подготовки списка файлов на отправку"""

    path_vbrr = f'{path}/ВБРР/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MONTH)}/'
    path_vtb = f'{path}/ВТБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MONTH)}/'
    path_rnko = f'{path}/РНКО/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MONTH)}/'
    path_gpb = f'{path}/ГПБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MONTH)}/'

    path_bank = ''
    if bank == "ВБРР":
        path_bank = path_vbrr
    elif bank == "ВТБ":
        path_bank = path_vtb
    elif bank == "РНКО":
        path_bank = path_rnko
    elif bank == "ГПБ":
        path_bank = path_gpb

    path_bank = os.path.abspath(path_bank) + '\\'

    files = []
    # Получение в лист всех файлов в каталоге
    list_of_files = filter(os.path.isfile,
                           glob.glob(path_bank + '*'))

    # Сортировка листа с файлами по дате
    list_of_files = sorted(list_of_files,
                           key=os.path.getmtime)

    for file in list_of_files:  # Итерация по листу с файлами и получение дат файлов
        try:
            timestamp_str = time.strftime('%d.%m.%Y',
                                          time.gmtime(os.path.getmtime(file)))
            if timestamp_str == TODAY_DATE:  # проверка по текущей дате
                files.append(file)

        except FileNotFoundError:  # если нет каталога или файла
            pass

    if printable:  # вывод списка в print если нужно
        if files:
            print(f"На отправку: Банк '{bank}', файл '{files[0]}'")
        else:
            print_log(f"Нет файлов на отправку по Банку '{bank}'")

    return files


if __name__ == '__main__':
    a = (search_files(path=KASSA_PATH_REESTRY,
                      bank="РНКО",
                      printable=True)
         )

    print(a)
