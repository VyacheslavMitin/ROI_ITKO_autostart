# Модуль переключения раскладок
# from MyModules.switch_layout import rus_layout, eng_layout
import keyboard
import time


def eng_layout():
    keyboard.press_and_release('ctrl+8')
    time.sleep(0.5)


def rus_layout():
    keyboard.press_and_release('ctrl+9')
    time.sleep(0.5)
