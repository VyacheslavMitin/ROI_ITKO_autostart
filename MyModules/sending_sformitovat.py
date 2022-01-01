def send_vou_outlook(subdivision) -> None:
    """Функция подготовки писем к отправке через MS Outlook."""
    import win32com.client as win32  # импорт модуля для работы с Win32COM, pip install pywin32
    to_email = RECIPIENTS  # получатели из настроек
    vou_full_path = glob.glob(ROI_common.return_path_dirs(report=f'Участок({subdivision})')[0]
                              + 'Детализация выручки*')
    os.chdir(ROI_common.return_path_dirs(report=f'Участок({subdivision})')[0])  # переход в папку с файлом
    vou_file = glob.glob('Детализация выручки*')  # только имя файла в переменную
    attach_file = vou_full_path[0]  # путь к файлу
    file_name = vou_file[0]  # имя детализации
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')  # вызов MS Outlook
    new_mail = outlook.CreateItem(0)  # создание письма в MS Outlook
    new_mail.Subject = file_name  # указание темы с именем детализации ВОУ
    new_mail.To = to_email  # обращение к списку получателей
    new_mail.BodyFormat = 2  # формат HTML
    new_mail.Body = f"Высылаю      '{file_name}'.       Данные в ВСКК так же загружены." + "\n\n"  # сообщение
    new_mail.Attachments.Add(Source=str(attach_file))  # присоединение вложения
    print_log("Письмо для отправки через MS Outlook подготовлено", line_after=False)
    new_mail.Display(True)  # отображение подготовленного письма для дополнения его данными
    # new_mail.Send()  # немедленная отправка письма
