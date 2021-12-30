import pynput


def typing_unicode_str(text: str) -> None:
    """Функция вставки Юникод-строк."""
    from pynput.keyboard import Controller
    Controller().type(text)
