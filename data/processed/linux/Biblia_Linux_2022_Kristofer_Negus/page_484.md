---
source_image: page_484.png
page_number: 484
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.54
tokens: 7514
characters: 1846
timestamp: 2025-12-24T04:58:59.180609
finish_reason: stop
---

Установка веб-сервера Apache

Несмотря на то что для установки веб-сервера Apache нужен только пакет httpd, в начале изучения Apache следует установить руководство (httpd-manual). Если вы хотите создать защищенный (SSL) сайт и, возможно, использовать для него статистику, можно просто установить всю группу пакетов, содержащуюся в дистрибутиве Fedora 30:

# yum groupinstall "Web Server"

При наличии интернет-соединения с репозиторием Fedora (или репозиторием RHEL, если вы используете систему RHEL) все обязательные и стандартные пакеты из этой группы будут установлены. В таком случае у вас будет все программное обеспечение, необходимое для выполнения примеров и упражнений, описанных в этой главе.

Запуск веб-сервера Apache

Чтобы запустить веб-сервер Apache, нужно задать запуск службы при каждой перезагрузке. В Red Hat Enterprise Linux (до RHEL 6) и более старых дистрибутивах Fedora от имени суперпользователя можно ввести следующее:

# chkconfig httpd on
# service httpd start
Starting httpd: [ OK ]

В системах Fedora 30 и RHEL 8 включение и запуск пакета httpd осуществляются с помощью команды systemctl:

# systemctl enable httpd.service
# systemctl start httpd.service
# systemctl status httpd.service
• httpd.service – The Apache HTTP Server
Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled;
    vendor preset: disabled)
Drop-In: /usr/lib/systemd/system/httpd.service.d
    └─ php-fpm.conf
Active: active (running) since Mon 2019-09-02 16:16:56 EDT;
    21min ago
Docs: man:httpd.service(8)
Main PID: 11773 (/usr/sbin/httpd)
Status: "Total requests: 14; Idle/Busy workers 100/0;Requests/sec: 0.0111; Bytes served/s>
Tasks: 214 (limit: 2294)
Memory: 24.6M
CGroup: /system.slice/httpd.service
    └─ 11773 /usr/sbin/httpd -DFOREGROUND
    └─ 11774 /usr/sbin/httpd -DFOREGROUND
    └─ 11775 /usr/sbin/httpd -DFOREGROUND