# Модуль расчета ВОУ
import datetime
import sys
import time
import pyautogui as pg
import pyperclip
from MyModules.config_read import PATH_SCREENSHOTS
from MyModules.print_log import print_log
from MyModules.past_dates import period_for_emails
from MyModules.send_notification_telegram import notification_send_telegram, notification_send_telegram_images
from MyModules.ntp_time import ntp_time_get


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
    time.sleep(420)  # 7 минут ждем ВОУ
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
        time.sleep(0.5)
        screenshots_path = PATH_SCREENSHOTS + f"Скрин журнала ВОУ за период '{period_for_emails()}' " \
                                              f"от '{ntp_time_get()}'.png"
        pg.screenshot(screenshots_path)
        notification_send_telegram(f"ВОУ №{after_vou_number} от {after_vou_date} "  # текстовое уведомление
                                   f"за период '{period_for_emails()}' сформирована в '{ntp_time_get()}'")
        notification_send_telegram_images(screenshots_path, screenshots_path[66:])  # скриншот
    else:
        error = f"ВОУ за период '{period_for_emails()}' не сформирована!"
        notification_send_telegram(error)
        sys.exit(error)
