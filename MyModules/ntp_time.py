import ntplib
import time
import datetime

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
    response = c.request('pool.ntp.org')
    # Вариант 1
    ntp_time = time.ctime(response.tx_time)
    ntp_time = ntp_time.replace(":", "-")
    # Вариант 1
    ts = response.tx_time
    ntp_time2 = time.strftime('%d.%m.%Yг. %H-%Mч.', time.localtime(ts))
    return ntp_time2


if __name__ == '__main__':
    print("Время с интернета")
    # datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    print(ntp_time_get())
