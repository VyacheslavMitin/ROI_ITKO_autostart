# Модуль высылки уведомлений в Телеграмм, pip install telegram-send, telegram_send --configure
# from MyModules.send_notification_telegram import notification_send_telegram

# Импорты
import telegram_send
from MyModules.print_log import print_log


# Функции
def notification_send_telegram(text):
    print_log("Отправлено уведомление в Телеграм")
    telegram_send.send(messages=['*КАССА ПЕРЕСЧЕТА*\n' + text],
                       parse_mode='Markdown')


def notification_send_telegram_images(image, caption):
    print_log("Отправлено уведомление с изображением в Телеграм")
    with open(image, 'rb') as img:
        telegram_send.send(images=[img],
                           captions=[caption])


# Тест функции
if __name__ == '__main__':
    print("Тест функции отправки уведомлений")
    notification_send_telegram('*test*')
