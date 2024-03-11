import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Параметры почтового сервера
smtp_server = 'smtp.mail.ru'
smtp_port = 587  # Порт SMTP сервера (обычно 587 для TLS или 465 для SSL)
smtp_username = 'ssavev@mail.ru'  # Ваш адрес электронной почты
smtp_password = '4PerLDKKs66snnb5hfzS'  # Ваш пароль

# Создание объекта для отправки сообщения
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = 'anddand2003@mail.ru'  # Адрес получателя
msg['Subject'] = 'ppsip'

# Текст сообщения
message = 'politech'
msg.attach(MIMEText(message, 'plain'))

# Инициализация соединения с SMTP сервером
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Использование TLS для безопасной передачи
    server.login(smtp_username, smtp_password)  # Аутентификация на SMTP сервере
    server.sendmail(smtp_username, 'anddand2003@mail.ru', msg.as_string())  # Отправка сообщения
