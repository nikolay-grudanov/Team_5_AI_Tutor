---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.24
tokens: 6214
characters: 835
timestamp: 2025-12-24T04:00:39.241843
finish_reason: stop
---

# Комментарий
comment = Public Directory
# путь
path = /var/samba
# не только чтение, но и запись
read only = no
# явно разрешаем запись
writable = yes
# разрешаем гостевой доступ
guest ok = yes
# разрешить просмотр содержимого каталога
browseable = yes

Сохраните файл конфигурации и введите команду testparm, которая проверит файл конфигурации Samba и сообщит, нет ли в нем ошибок:

# testparm
Load smb config files from /etc/samba/smb.conf
Loaded services file OK.
Server role: ROLE_DOMAIN_MEMBER
...

Как видите, файл в порядке, а роль сервера - член домена (ROLE_DOMAIN_MEMBER). Все, как нам и нужно. Теперь запустим Samba:

sudo service smbd start

Попробуем подключиться к нашему домену как пользователь user:

# net ads join -U user -D MY
Enter user's password:
Using short domain name - MY
Joined 'linux' to realm 'my.company'