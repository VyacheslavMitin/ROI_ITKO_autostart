# Модуль работы с поиском и отправкой файлов через MS Outlook

# Импорты
import glob
import subprocess
import time
import datetime
import win32com.client as win32  # импорт модуля для работы с Win32COM (MS Outlook, etc.) pip install pywin32

# Мои модули
from MyModules.print_log import print_log
from MyModules.config_read import *

# КОНСТАНТЫ
SIGNATURE = """

--
с уважением,
Начальник Ульяновского участка пересчета
Регионального Центра "Ульяновск"
Нурмухамедова Регина Маулетдиновна
Тел.: (8422) 63-47-78 
С 7:00 до 12:00 и с 13:00 до 16:00
"""


# ФУНКЦИИ
def sending_outlook(mode='work', bank=None, files=None, displayed=True) -> None:
    """Функция подготовки писем к отправке через MS Outlook.
    Режимы mode могут быть 'work' и 'test'"""
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')  # вызов MS Outlook
    new_mail = outlook.CreateItem(0)  # создание письма в MS Outlook

    new_mail.BodyFormat = 2  # формат HTML

    if mode == 'test':
        recipients = RECIPIENTS_TEST

        new_mail.Subject = f'Тестовое письмо {datetime.date.today().strftime("%d %m %Y")}'  # указание темы
        new_mail.Body = f'Тестовое письмо за {datetime.date.today().strftime("%d %m %Y")}.' \
                        + SIGNATURE  # сообщение
        new_mail.To = recipients  # обращение к списку получателей

    elif mode == 'work':
        recipients = ''
        if bank == "ВБРР":
            recipients = RECIPIENTS_VBRR
        elif bank == "ВТБ":
            recipients = RECIPIENTS_VTB
        elif bank == "РНКО":
            recipients = RECIPIENTS_RNKO
        elif bank == "ГПБ":
            recipients = RECIPIENTS_GPB

        new_mail.Subject = f'Заявка на сдачу наличных денег {bank} {datetime.date.today().strftime("%d %m %Y")}'
        new_mail.Body = SIGNATURE  # сообщение
        new_mail.To = recipients  # обращение к списку получателей
        if files:
            for file in files:
                new_mail.Attachments.Add(file)

    if displayed:  # отображать окно письма
        new_mail.Display(True)  # отображение подготовленного письма или new_mail.Send()  # немедленная отправка письма
    else:
        new_mail.Send()

    print_log(f"Письмо для отправки в '{bank}' подготовлено")

    time.sleep(0.5)
    # subprocess.Popen(OUTLOOK_BIN)  # запуск MS Outlook


if __name__ == '__main__':
    # pass
    sending_outlook(mode='test',

                    files=None,
                    displayed=True)
    # sending_outlook('sformirovat')
    # sending_outlook('202')
    # print(search_sending_files('202')[0])
    # print(search_sending_files('pp')[1])
    # sending_outlook('vou')
