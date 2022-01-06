# Модуль проверки монитора, сейчас не используется

# Импорты
import pyautogui as pg
import sys
from MyModules.print_log import print_log


COORDINATES_THUNDERBOLT_DISPLAY = {  # словарь координат для Thunderbolt Display
    'точки по дням': (1000, 125),
    'очистка поискового поля': (400, 65),
    'экспорт 014': (45, 125),
    'экспорт вскк': (265, 125),
    'экспорт воу': (885, 95),
    'журнал воу': (785, 95),
    'авто воу': (650, 95),
    'обработка дбф': (1025, 95),
    'закрыть уведомление': (10, 1195),
    'экспорт 202': (1115, 95),
    'документы за день': (735, 125),
    'распред. ведомости': (1255, 95),
    'открыть клиенты': (95, 95),
}

COORDINATES_MACBOOK_DISPLAY = {  # словарь координат для MacBook Pro 15" Retina Display, не настроен
    'точки по дням': (1000, 125),
    'очистка поискового поля': (400, 65),
    'экспорт 014': (45, 125),
    'экспорт вскк': (265, 125),
    'экспорт воу': (885, 95),
    'журнал воу': (785, 95),
    'авто воу': (650, 95),
    'обработка дбф': (1025, 95),
    'закрыть уведомление': (10, 1195),
    'экспорт 202': (1115, 95),
    'документы за день': (735, 125),
    'распред. ведомости': (1255, 95),
    'открыть клиенты': (95, 95),
}


# Функции
def checking_monitor(silent=False):
    """Функция проверки монитора"""
    from pygetwindow import Size
    size_thunderbolt = Size(width=2560, height=1440)
    size_macbook = Size(width=1440, height=900)
    current_size = pg.size()

    if current_size == size_thunderbolt:
        if not silent:
            print_log('Определен монитор Thunderbolt')
        return COORDINATES_THUNDERBOLT_DISPLAY
    elif current_size == size_macbook:
        if not silent:
            print_log('Определен монитор MacBook Pro')
        return COORDINATES_MACBOOK_DISPLAY
    else:
        sys.exit('ERROR: не тот монитор')


if __name__ == '__main__':
    checking_monitor(silent=False)
