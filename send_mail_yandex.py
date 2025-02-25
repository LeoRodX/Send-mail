import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Параметры для отправки письма
smtp_server = "smtp.yandex.ru"  # SMTP-сервер Yandex
smtp_port = 587  # Порт для TLS
email_from = "my_out_mail@yandex.ru"  # Ваш email на Yandex
email_to = "my_in_mail@yandex.ru"  # Email получателя
password = "my_out_mail_password"  # Пароль от почты или пароль приложения

# Создание письма
subject = "Тема письма"
body = "Текст письма"

# Создаем объект письма
msg = MIMEMultipart()
msg["From"] = email_from
msg["To"] = email_to
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))  # Добавляем текст письма

# Подключение к SMTP-серверу и отправка письма
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Включаем шифрование TLS
        server.login(email_from, password)  # Авторизация
        server.sendmail(email_from, email_to, msg.as_string())  # Отправка письма
    print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")
