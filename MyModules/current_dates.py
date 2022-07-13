# Модуль для определения текущих дат
# from MyModules.past_dates import past_dates
from datetime import datetime


def current_dates():
    """Функция расчета конечных дат текущего месяца в строковом исполнении.
    Возвращает текущую дату: 0 и 1 даты начала/конца месяца, 2 год, 3 месяц, 4 месяц в формате '01 Jan'."""
    now_month = datetime.now().month  # текущий месяц в цифровом представлении
    now_year = datetime.now().year  # текущий год в цифровом представлении
    now_month_year_str = datetime.now().strftime('.%m.%y')  # '.месяц.год' в строковом представлении
    number_month = datetime.now().strftime('%m %b')

    start_date_ = '01' + now_month_year_str  # начальная дата в строковом представлении

    if now_month == 2:  # пляски вокруг февраля и високосного года
        if ((now_year - 2020) % 4) == 0:  # если год - 2020 делится без остатка - то високосный
            finish_date_ = '29' + now_month_year_str
        else:  # а если нет то обычный
            finish_date_ = '28' + now_month_year_str

    elif now_month in [4, 6, 9, 11]:  # если апрель, июнь, сентябрь, ноябрь - то 30 число
        finish_date_ = '30' + now_month_year_str

    else:  # все остальные месяцы 31 число
        finish_date_ = '31' + now_month_year_str

    return start_date_, finish_date_, now_year, now_month, number_month  # возврат  функции


if __name__ == '__main__':
    print(current_dates())
