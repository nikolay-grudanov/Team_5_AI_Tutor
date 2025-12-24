---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.76
tokens: 6316
characters: 1171
timestamp: 2025-12-24T04:00:07.775168
finish_reason: stop
---

Листинг 10.4. Файл /etc/bind/named.conf.options

options {
    directory "/var/cache/bind";

    // Здесь описываются forward-серверы

    // forwarders {
    //     0.0.0.0;
    // };

    dnssec-validation auto;

    auth-nxdomain no;      # conform to RFC1035
    listen-on-v6 { any; };
};

Все, что нужно - это добавить IP-адрес DNS-сервера провайдера в блок forwarders. Именно они будут выполнять всю грязную работу по разрешению доменных имен, а наш сервер будет только кэшировать результаты запроса.

Перед блоком forwarders можно указать параметр forward, который может принимать значение only или first. В первом случае наш сервер вообще не будет предпринимать попыток обработать запрос самостоятельно. Во втором случае сервер предпримет попытку обработать запрос самостоятельно, если не получит ответ от серверов, описанных в блоке forwarders. Второе значение более предпочтительно:

forward first;
forwarders {
    8.8.8.8;
    8.8.8.4;
};

Вот и все. Перезапустите сервер:

# service bind9 restart

Просмотрите файл журнала:

# tail /var/log/daemon.log

Вы должны увидеть сообщение, что сервер запущен вроде этого:

Jun 29 09:41:42 debian named[6921]: running