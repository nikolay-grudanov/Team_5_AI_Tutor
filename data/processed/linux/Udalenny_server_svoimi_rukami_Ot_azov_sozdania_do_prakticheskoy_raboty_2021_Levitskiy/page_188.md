---
source_image: page_188.png
page_number: 188
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.90
tokens: 6350
characters: 1244
timestamp: 2025-12-24T04:00:21.958371
finish_reason: stop
---

Комментарии из remote.conf, которые также будут сгенерированы утилитой, можно не копировать. Вот что нужно скопировать (ключ у вас будет другим):

key "rndc-key" {
    algorithm hmac-md5;
    secret «sJZkjPskmF9KPKQBwaUtfQ==»;
};
controls {
default-key "rndc-key";
default-server 127.0.0.1;
default-port 953;
};

Также в файл named.conf.options нужно добавить блок allow-query (внутри блока options):

allow-query {
192.168.1.0/24;
localhost;
}

Здесь мы разрешаем обращаться к нашему DNS-серверу только пользователям внутренней локальной сети и узлу localhost.

Также можно обновить файл корневых серверов (это рекомендуется делать периодически):

# wget ftp://ftp.internic.net/domain/named.root
# cp named.root /etc/bind/db.root

Вот теперь действительно все и можно перезапустить сервер:

# service bind9 restart

10.5. Настройка вторичного DNS-сервера

В крупных сетях или там, где важна отказоустойчивость, например, в сетях провайдера, важно настроить вторичный DNS-сервер, который будет обслуживать запросы клиентов в случае отказа первичного сервера.

Вторичный сервер настраивается, как и первичный, вот только тип зоны задается как подчиненная (slave), а в блоке masters указываются первичные DNS-серверы (в нашем случае только один):