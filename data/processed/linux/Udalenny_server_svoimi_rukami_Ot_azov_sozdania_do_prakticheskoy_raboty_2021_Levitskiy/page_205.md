---
source_image: page_205.png
page_number: 205
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.09
tokens: 6302
characters: 1127
timestamp: 2025-12-24T04:00:44.665930
finish_reason: stop
---

описывают предоставляемые ресурсы. В листинге 12.2 будут приведены секции global и public. В последней описываются общий каталог, который будет доступен всем пользователям. Дополнительную информацию о настройке Samba можно получить по адресу https://help.ubuntu.com/community/Samba. Сейчас главное интегрировать Samba в домен AD, а опи- сать дополнительные ресурсы и настроить к ним права доступа, думаю, вы сможете самостоятельно.

Листинг 12.2. Пример файла конфигурации /etc/samba/smb.conf для интеграции сервера в домен AD

[global]
# Имя рабочей группы и домена нужно указывать заглавными буквами
workgroup = MY
realm = MY.COMPANY

# Авторизация через AD
security = ADS
encrypt passwords = true

# Отключаем прокси DNS
dns proxy = no

# Ускоряем работу Samba
socket options = TCP_NODELAY

# Если не хотите, чтобы Samba стала контроллером домена, установите
# следующие параметры таким образом
domain master = no
local master = no
preferred master = no
os level = 0
domain logons = no

# Отключаем поддержку принтеров
load printers = no
show add printer wizard = no
printcap name = /dev/null
disable spoolss = yes

[public]