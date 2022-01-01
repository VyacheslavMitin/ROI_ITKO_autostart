# Модуль для определения текущих дат
# from MyModules.past_dates import past_dates
from datetime import datetime


def past_dates() -> tuple:
    """Функция расчета конечных дат прошлого месяца в строковом исполнении
    Возвращает дату прошлого месяца: 0 и 1 даты начала/конца месяца, 2 год, 3 месяц, 4 месяц в формате '01 Jan'."""
    past_start_date_, past_finish_date_, past_month_str, past_number_month = '01.01.2021', '31.01.2021', '01', '01 Jan'
    now_month = datetime.now().month  # текущий месяц в цифровом представлении
    now_year = datetime.now().year  # текущий год в цифровом представлении

    if now_month == 1:  # отлов января и реакция на него, вычитания года и явное указания декабря
        past_month_str = str(12)  # в строковом исполнении явное указания декабря
        past_year = now_year - 1  # вычитание года в цифровом
        past_year = str(past_year)[2:]
        past_start_date_ = '01' + f'.{past_month_str}.{past_year}'  # 01 декабря прошлого года
        past_finish_date_ = '31' + f'.{past_month_str}.{past_year}'  # 31 декабря прошлого года
        past_number_month = '12 Dec'

    else:  # все остальные месяцы кроме января
        past_month = now_month - 1  # вычитание месяца
        past_year_ = now_year  # год тот же что и текущий
        past_year = str(past_year_)[2:]
        now_year = str(now_year)[2:]
        past_number_month = datetime(past_year_, past_month, 1).strftime('%m %b')  # в формате "01 Jan"

        if past_month in [4, 6, 9, 11]:  # апрель, июнь, сентябрь, ноябрь
            if len(str(past_month)) == 1:  # если месяц из 1 символа то конкатенация с '0'
                past_month_str = '0' + str(past_month)  # апрель, июнь, сентябрь
            else:
                past_month_str = str(past_month)
            past_start_date_ = '01' + f'.{past_month_str}.{now_year}'
            past_finish_date_ = '30' + f'.{past_month_str}.{now_year}'

        elif past_month in [1, 3, 5, 7, 8, 10]:  # январь, март, май, июль, август, октябрь
            if len(str(past_month)) == 1:  # если месяц из 1 символа то конкатенация с '0'
                past_month_str = '0' + str(past_month)  # январь, март, май, июль, август
            else:
                past_month_str = str(past_month)
            past_start_date_ = '01' + f'.{past_month_str}.{now_year}'
            past_finish_date_ = '31' + f'.{past_month_str}.{now_year}'

        elif past_month == 2:  # февраль
            past_month_str = '02'  # февраль в строковом представлении
            if ((past_year_ - 2020) % 4) == 0:  # если (год - 2020) делится без остатка то високосный
                past_finish_date_ = '29' + f'.{past_month_str}.{now_year}'  # февраль високосного
            else:  # а если нет то обычный
                past_finish_date_ = '28' + f'.{past_month_str}.{now_year}'  # февраль не високосного
            past_start_date_ = '01' + f'.02.{now_year}'

    (dd_, mm_, yyyy_) = past_finish_date_.split('.')  # создание строки без разделителя
    past_finish_date_no_dots = ''.join((dd_, mm_, yyyy_))

    return past_start_date_, past_finish_date_, past_year, past_month_str, past_number_month, past_finish_date_no_dots
