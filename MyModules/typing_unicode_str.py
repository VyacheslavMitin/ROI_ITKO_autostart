# Модуль ввода и копирования/вставки текста

def typing_unicode_str(text: str) -> None:
    """Функция вставки Юникод-строк."""
    from pynput.keyboard import Controller
    Controller().type(text)


def copy_paste_text(text: str) -> None:
    """Функция вставки текста, передаваемой как аргумент функции."""
    import pyperclip
    import platform
    import pyautogui
    pyperclip.copy(text)
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")
