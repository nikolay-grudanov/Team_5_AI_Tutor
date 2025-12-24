---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.11
tokens: 6261
characters: 928
timestamp: 2025-12-24T04:00:31.858440
finish_reason: stop
---

синхронизацию времени, что очень важно для нормальной работы нашего сервера в AD.

Для автоматической синхронизации времени используется демон ntpd. Установим его:

sudo apt-get install ntp

После этого нужно отредактировать файл /etc/ntp.conf и добавить в него строку:

server dc.my.company

Теперь перезапускаем сеть и ntpd:

service networking restart
service ntp restart

12.4. Настройка Kerberos

Теперь мы можем приступить к настройке нашей связки Kerberos + Samba + Winbind. Первым делом настроим Kerberos. Нужно отредактировать файл /etc/krb5.conf и привести его к виду, представленному в листинге 12.1. Строки, выделенные жирным, необходимо заполнить своими данными.

Листинг 12.1. Файл /etc/krb5.conf

[libdefaults]
default_realm = MY.COMPANY
kdc_timesync = 1
ccache_type = 4
forwardable = true
proxiable = true
v4_instance_resolve = false
v4_name_convert = {
    host = {
        rcmd = host
        ftp = ftp
    }
}