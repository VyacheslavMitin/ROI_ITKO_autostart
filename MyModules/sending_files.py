import glob
import subprocess
import time
# Мои модули
from MyModules.config_read import *
from MyModules.print_log import print_log
from MyModules.past_dates import period_for_emails

# КОНСТАНТЫ
SIGNATURE = """

______________________
Ведущий специалист Регионального Центра "Ульяновск" Объединения РОСИНКАСС
Митин Вячеслав Алексеевич
8-902-004-27-98
"""


# ФУНКЦИИ
def search_sending_files(mode_):
    """Функция подготовки файлов для писем к отправке через MS Outlook.
    Режимы mode_ могут быть '202', 'sformirovat', 'vou', 'test'"""
    files_names = ''
    files = []
    path_files = None

    extensions = EXTENSIONS.split(',')

    if mode_ == 'test':
        print_log("Файлов для отправки нет - тестовый режим")

    elif mode_ == '202':
        path_files = PATH_202

    elif mode_ == 'sformirovat':
        path_files = PATH_SFORMIROVAT

    elif mode_ == 'vou':
        path_files = PATH_VOU

    for item in extensions:  # искать файлы по расширению
        files.extend(glob.glob(path_files + f'*{item}'))

    files_names_ = os.listdir(path_files)  # список имен файлов вида 1) Ашан
    for names in enumerate(files_names_):
        files_names += f'{str(names[0] + 1)})  {names[1]}\n'  # в конце разделитель, может быть хоть '; '

    if mode_ != 'test':
        return files, files_names


def sending_outlook(mode_, displayed=True) -> None:
    """Функция подготовки писем к отправке через MS Outlook.
    Режимы mode_ могут быть '202', 'sformirovat', 'vou', 'test'"""
    import win32com.client as win32  # импорт модуля для работы с Win32COM (MS Outlook, etc.)
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')  # вызов MS Outlook
    new_mail = outlook.CreateItem(0)  # создание письма в MS Outlook

    new_mail.BodyFormat = 2  # формат HTML

    if mode_ == 'test':
        new_mail.Subject = f'Тестовое письмо из ИТКО {period_for_emails()}'  # указание темы
        new_mail.Body = f"Тестовое письмо из ИТКО за {period_for_emails()}." + SIGNATURE  # сообщение
        new_mail.To = RECIPIENTS_TEST  # обращение к списку получателей

    elif mode_ == '202':
        new_mail.Subject = f'Форма 202 {period_for_emails()}'  # указание темы
        new_mail.Body = f"Форма 202 из ИТКО за {period_for_emails()}.\n\nФайлы:\n{search_sending_files(mode_)[1]}" \
                        + SIGNATURE  # сообщение
        new_mail.To = RECIPIENTS_202  # обращение к списку получателей

    elif mode_ == 'sformirovat':
        new_mail.Subject = f'Файлы "Сформировать.xls" из кассы пересчета {period_for_emails()}'  # указание темы
        new_mail.Body = f'Файлы "Сформировать.xls" из кассы пересчета за {period_for_emails()}.' \
                        f'\n\nФайлы:\n{search_sending_files(mode_)[1]}' + SIGNATURE  # сообщение
        new_mail.To = RECIPIENTS_SFORMIROVAT  # обращение к списку получателей

    elif mode_ == 'vou':
        new_mail.Subject = f'Детализация выручки ОКО {period_for_emails()}'  # указание темы
        new_mail.Body = f'Детализация выручки ОКО за {period_for_emails()}.' \
                        f'\n' + SIGNATURE  # сообщение
        new_mail.To = RECIPIENTS_VOU  # обращение к списку получателей
    new_mail.CC = RECIPIENTS_COPY  # получатели в копии

    if mode_ != 'test':  # работа с вложениями
        print_log("Поиск файлов для отправки через e-mail:", line_before=True)
        for files in (search_sending_files(mode_)[0]):  # вложения
            new_mail.Attachments.Add(files)
        tuple_not_used = ('test', 'vou')
        if mode_ not in tuple_not_used:
            print_log(f"Файлы для отправки:\n{search_sending_files(mode_)[1]}")

    if displayed:  # отображать окно письма
        new_mail.Display(True)  # отображение подготовленного письма или new_mail.Send()  # немедленная отправка письма
    else:
        new_mail.Send()

    print_log("Письмо для отправки через MS Outlook подготовлено")

    time.sleep(0.5)
    subprocess.Popen(OUTLOOK_BIN)  # запуск MS Outlook


if __name__ == '__main__':
    # sending_outlook('test')
    # sending_outlook('sformirovat')
    # sending_outlook('202')
    print(search_sending_files('202')[0])
    # print(search_sending_files('vou')[1])
    # sending_outlook('vou')
