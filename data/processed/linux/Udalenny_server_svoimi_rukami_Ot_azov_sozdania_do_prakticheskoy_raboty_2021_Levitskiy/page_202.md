---
source_image: page_202.png
page_number: 202
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.88
tokens: 6344
characters: 1181
timestamp: 2025-12-24T04:00:39.590681
finish_reason: stop
---

Итак, установим необходимые пакеты (на примере Debian/Ubuntu):

sudo apt-get install samba krb5-user winbind

Первый пакет (samba) позволяет стать членом домена и предоставлять/использовать ресурсы. Второй пакет необходим для работы протокола Kerberos, который используется для аутентификации в Windows. Без третьего пакета нельзя использовать учетную запись пользователя из AD.

Далее мы будем использовать следующие параметры для настройки:

• Имя домена - MY.COMPANY
• Имя контроллера ActiveDirectory - dc.my.company
• IP-адрес контроллера домена - 192.168.1.2
• Имя Linux-сервера - linux

12.3. Подготовительная настройка

Первым делом на компьютере linux нужно настроить DNS и синхронизацию времени. Откройте файл /etc/resolv.conf и добавьте в него следующие строки:

domain my.company
search my.company
nameserver 192.168.1.2

Нужно запретить редактировать этот файл, чтобы его не изменил NetworkManager:

sudo chattr +i /etc/resolv.conf

Также нужно отредактировать /etc/hosts:

127.0.0.1 localhost
127.0.1.1 linux.my.company    linux

Также убедитесь, что файл /etc/hostname содержит правильное имя узла (linux). На этом настройка DNS закончена, а после нее нужно настроить