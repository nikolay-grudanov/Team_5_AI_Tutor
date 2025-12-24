---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.34
tokens: 6368
characters: 1389
timestamp: 2025-12-24T03:59:45.091117
finish_reason: stop
---

# Максимальное число клиентов на один узел. Позже мы
# поговорим об этой
# директиве подробнее
#MaxClientsPerHost none
# Максимальное число соединений для одного пользователя
#MaxClientsPerUser 1 "Only one connection at a time."

# -----------------------------
# Аутентификация
# -----------------------------

### PAM-аутентификация
# Включите PAM-аутентификацию, если она вам нужна (если хотите
# контролировать вход систему по FTP через PAM)
AuthPAM off

# измененный AuthPAMConfig-файл
AuthPAMConfig proftpd
### PAM-аутентификация

# Задает альтернативный файл паролей. Если нужно, чтобы информация об учетных записях бралась из /etc/passwd,
# укажите его здесь, а еще лучше - закомментируйте следующие две опции
AuthUserFile /etc/proftpd/auth/passwd
# Задает альтернативный файл групп
AuthGroupFile /etc/group

### порядок модулей аутентификации.
# сначала аутентификация будет производиться средствами самой ОС, а потом - через файл, заданный в AuthFile
AuthOrder mod_auth_unix.c mod_auth_file.c
# AuthOrder mod_auth_file.c
# Если нужна аутентификация PAM, то порядок должен быть такой:
# AuthOrder mod_auth_pam.c* mod_auth_unix.c

# -----------------------------
# После входа пользователя (логина)
# -----------------------------
# Задает файл, который будет отображен после входа на сервер
DisplayLogin welcome.msg
# Задает файл, который будет отображаться при изменении каталога