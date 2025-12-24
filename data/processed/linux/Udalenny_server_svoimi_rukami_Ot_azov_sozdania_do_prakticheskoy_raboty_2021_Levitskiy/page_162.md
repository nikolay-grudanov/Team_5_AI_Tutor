---
source_image: page_162.png
page_number: 162
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.41
tokens: 6312
characters: 1170
timestamp: 2025-12-24T03:59:40.145238
finish_reason: stop
---

# Вход на сервер

# Поскольку DeferWelcome равно on, то приветствие будет отображено после аутентификации, а не до нее (off)
ServerIdent on "FTP server ready"
DeferWelcome on
# Директива DisplayConnect задает текстовый файл, который будет отображен сразу после подключения пользователя, но до его входа
#DisplayConnect /etc/proftpd/msg
# Директива DisplayLogin указывает текстовый файл, который будет показан
# когда пользователь зайдет на сервер
#DisplayLogin /etc/proftpd/msg

<IfModule mod_ident.c>
    # Отключаем Ident-запросы (RFC1413)
    IdentLookups off
</IfModule>

# Если директива UseFtpUsers включена (on), то ProFTPD при подключении пользователя будет искать его имя в файле /etc/ftpusers.
# Если его там нет, тогда сервер откажет в подключении
UseFtpUsers off
# Подключение на основании /etc/shell. При включенной директиве будет требоваться «правильная» оболочка. Если к серверу будут подключаться не только Linux/Unix-клиенты, эту директиву нужно выключить (off)
RequireValidShell off

# Максимальное число времени в секундах, которые разрешается клиенту потратить на аутентификацию
TimeoutLogin 60

# Максимальное число попыток входа
MaxLoginAttempts 3