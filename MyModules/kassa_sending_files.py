# Модуль отправки файлов по кассе

import time
import datetime
import win32com.client as win32  # импорт модуля для работы с Win32COM (MS Outlook, etc.) pip install pywin32
from MyModules.config_read import *
from MyModules.kassa_searching_files import search_files
from MyModules.print_log import print_log

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

TODAY_DATE = datetime.date.today().strftime("%d %m %Y")


# ФУНКЦИИ
def func_dict_mail(mode: str, path: str, bank: str) -> dict:
    """Функция возвращения словаря с нужными данными"""
    recipients: str = 'список получателей'
    if bank == "ВБРР":
        recipients = KASSA_RECIPIENTS_VBRR
    elif bank == "ВТБ":
        recipients = KASSA_RECIPIENTS_VTB
    elif bank == "РНКО" or bank == "ГПБ":
        recipients = KASSA_RECIPIENTS_SAMARA

    files_xml_reestr = []
    if mode == 'XML_РЕЕСТРЫ':
        files_xml_reestr = [search_files(path=KASSA_PATH_REESTRY, bank=bank, printable=False)[0],
                            search_files(path=KASSA_PATH_XML_TO, bank=bank, printable=False)[0]]
        # print(files_xml_reestr)

    dict_mail = {
        'XML_РЕЕСТРЫ': {
            'subject': f'РЦ Ульяновск реестр {bank} {TODAY_DATE}',
            'recipients': recipients,
            'files': files_xml_reestr,
        }
    }

    return dict_mail


def sending_outlook(mode='XML_РЕЕСТРЫ', path=KASSA_PATH_REESTRY, bank='РНКО', displayed=True) -> None:
    """Функция подготовки писем к отправке через MS Outlook.
    Режимы mode могут быть 'XML_РЕЕСТРЫ' и 'test'"""

    if mode == 'test':
        outlook = win32.gencache.EnsureDispatch('Outlook.Application')  # вызов MS Outlook
        new_mail = outlook.CreateItem(0)  # создание письма в MS Outlook

        new_mail.BodyFormat = 2  # формат HTML

        recipients = RECIPIENTS_TEST

        new_mail.Subject = f'Тестовое письмо {datetime.date.today().strftime("%d %m %Y")}'  # указание темы
        new_mail.Body = f'Тестовое письмо за {datetime.date.today().strftime("%d %m %Y")}.' \
                        + SIGNATURE  # сообщение
        new_mail.To = recipients  # обращение к списку получателей
        new_mail.Display(True)

    else:
        try:
            files = func_dict_mail(mode, path, bank).get(mode).get('recipients')
        except IndexError:
            print_log(f"Файла по Банку '{bank}' нет")
        else:
            outlook = win32.gencache.EnsureDispatch('Outlook.Application')  # вызов MS Outlook
            new_mail = outlook.CreateItem(0)  # создание письма в MS Outlook

            new_mail.BodyFormat = 2  # формат HTML
            new_mail.Subject = func_dict_mail(mode, path, bank).get(mode).get('subject')
            new_mail.Body = SIGNATURE  # сообщение, только подпись
            new_mail.To = func_dict_mail(mode, path, bank).get(mode).get('recipients')
            files = func_dict_mail(mode, path, bank).get(mode).get('files')

            if isinstance(files, list):
                for item in files:
                    new_mail.Attachments.Add(item)
            else:
                new_mail.Attachments.Add(files)
            if displayed:  # отображать окно письма
                new_mail.Display(True)  # отображение подготовленного письма или new_mail.Send()  # немедленная отправка письма
            else:
                new_mail.Send()
            print_log(f"Письмо для отправки в '{bank}' подготовлено")

    time.sleep(0.5)
    # subprocess.Popen(OUTLOOK_BIN)  # запуск MS Outlook


if __name__ == '__main__':
    # print(func_dict_mail('XML_РЕЕСТРЫ', KASSA_PATH_REESTRY, "РНКО").get('XML_РЕЕСТРЫ').get('subject'))
    # print(func_dict_mail('XML_РЕЕСТРЫ', KASSA_PATH_REESTRY, "РНКО").get('XML_РЕЕСТРЫ').get('recipients'))
    # print(func_dict_mail('XML_РЕЕСТРЫ', KASSA_PATH_REESTRY, "РНКО").get('XML_РЕЕСТРЫ').get('files'))
    sending_outlook(mode='test',
                    path=KASSA_PATH_XML_TO,
                    bank="ГПБ",
                    )
