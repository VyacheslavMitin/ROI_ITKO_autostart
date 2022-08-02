import ntplib
import time
# import datetime
from MyModules.print_log import print_log

# import os
# import time
# import ntplib
# c = ntplib. NTPClient ()
# response = c.request('pool.ntp.org')
# ts = response.tx_time
# _date = time.strftime('%d.%m.%Yг. %H-%Mч.', time.localtime(ts))
# print(_date,)


def ntp_time_get():
    c = ntplib.NTPClient()
    try:
        response = c.request('pool.ntp.org')
    except ntplib.NTPException:
        return "нет точного времени"
    else:
        # Вариант 1
        ntp_time = time.ctime(response.tx_time)
        ntp_time = ntp_time.replace(":", "-")
        # Вариант 1
        ts = response.tx_time
        # ntp_time2 = time.strftime('%d.%m.%Yг. %H-%Mч.', time.localtime(ts))
        ntp_time2 = time.strftime('%d.%m.%Y, %H-%M', time.localtime(ts))
        return ntp_time2


def ntp_time():
    i = 0
    attempts = 30
    time_ntp = ntp_time_get()
    while time_ntp == "нет точного времени":
        i += 1
        print_log(f"Точное время не получено! Продолжаю попытки получения {i} из {attempts}...")
        time_ntp = ntp_time_get()
        if time_ntp != "нет точного времени":
            print_log("Удалось получить точное время")
            return time_ntp
        if i == 30:
            break
    else:
        return time_ntp


if __name__ == '__main__':
    print("Время с интернета")

    # datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    # print(ntp_time_get())
    print(ntp_time())
