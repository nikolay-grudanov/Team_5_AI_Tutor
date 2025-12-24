---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.99
tokens: 6317
characters: 1079
timestamp: 2025-12-24T04:00:06.978699
finish_reason: stop
---

Общие параметры теперь вынесены в файл /etc/bind/named.conf.options. Локальные зоны описываются в named.conf.local, а зоны по умолчанию - в named.conf.default-zones. Нас в данный момент интересует файл named.conf.default-zones, в котором описаны зоны по умолчанию. Проследите, чтобы в этом файле были описаны зоны, представленные в листинге 10.3.

Листинг 10.3. Файл /etc/bind/named.conf.default-zones

// корневая зона, содержит корневые серверы имен
zone "." {
    type hint;
    file "/etc/bind/db.root";
};

// Зона localhost
zone "localhost" {
    type master;
    file "/etc/bind/db.local";
};

zone "127.in-addr.arpa" {
    type master;
    file "/etc/bind/db.127";
};

zone "0.in-addr.arpa" {
    type master;
    file "/etc/bind/db.0";
};

zone "255.in-addr.arpa" {
    type master;
    file "/etc/bind/db.255";
};

Как видите, в этом конфигурационном файле описывается зона корневых серверов и локальная зона localhost, которая отвечает за преобразование имени localhost в IP-адрес 127.0.0.1 и обратно.

Теперь рассмотрим файл /etc/bind/named.conf.options (лист. 10.4).