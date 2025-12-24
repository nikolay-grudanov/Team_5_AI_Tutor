---
source_image: page_323.png
page_number: 323
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.22
tokens: 7424
characters: 516
timestamp: 2025-12-24T04:27:42.423668
finish_reason: stop
---

![Приложение для настройки DNS](https://i.imgur.com/3Q5z5QG.png)

Рис. 11.2. Приложение для настройки сервиса DNS

Листинг 11.1. Пример содержимого файла /etc/named.conf

options {
    directory "/var/named/";
};

zone "." {
    type hint;
    file "named.ca";
};

zone "sitename.com" {
    type master;
    file "sitename.zone";
};

zone "10.12.190.in-addr.arpa" {
    type master;
    file "10.12.190.in-addr.arpa.zone";
};

В данном примере файл разбит на четыре раздела, каждый из которых имеет следующий формат: