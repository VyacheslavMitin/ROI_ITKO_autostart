# Модуль расчета ВОУ
import sys
import time
import pyautogui as pg
import pyperclip
from MyModules.print_log import print_log
from MyModules.past_dates import period_for_emails
from MyModules.send_notification_telegram import notification_send_telegram


def preparation_vou():
    """Функция запуска расчета ВОУ"""
    print_log("Запуск расчета ВОУ", line_before=True)
    from MyModules.select_menu import selecting_menu
    selecting_menu(1, 5)  # открытие журнала воу
    from MyModules.interval_journals import interval_january
    interval_january()
    pg.press("pagedown")
    time.sleep(0.5)
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)
    before_vou_date = pyperclip.paste()

    selecting_menu(2, 6)  # запуск авто формирования
    time.sleep(360)  # 6 минут ждем воу
    # TODO сделать проверку созданной ВОУ иначе - по загрузке процессора например
    pg.press("down")

    time.sleep(0.5)
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)
    after_vou_date = pyperclip.paste()

    if before_vou_date != after_vou_date:
        pg.press("right", presses=3, interval=0.5)
        time.sleep(0.5)
        pg.hotkey('ctrl', 'c')
        time.sleep(0.5)
        after_vou_number = pyperclip.paste()
        notification_send_telegram(f"ВОУ №{after_vou_number} от {after_vou_date} "
                                   f"за период '{period_for_emails()}' сформирована")
    else:
        error = f"ВОУ за  период '{period_for_emails()}' не сформирована!"
        notification_send_telegram(error)
        sys.exit(error)
