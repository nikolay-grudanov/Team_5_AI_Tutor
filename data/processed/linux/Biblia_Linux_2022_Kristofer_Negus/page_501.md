---
source_image: page_501.png
page_number: 501
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.13
tokens: 7571
characters: 2185
timestamp: 2025-12-24T04:59:33.601268
finish_reason: stop
---

3. Если не планируете подписывать сертификат или хотите протестировать настройки, создайте самоподписанный сертификат и сохраните его в файле server.crt в каталоге /etc/pki/tls/certs:

# cd /etc/pki/tls/certs
# openssl req -new -x509 -nodes -sha1 -days 365 \
    -key /etc/pki/tls/private/server.key \
    -out server.crt
Country Name (2 letter code) [AU]: US
State or Province Name (full name) [Some-State]: NJ
Locality Name (eg, city) [Default City]: Princeton
Organization Name (eg, company) [Default Company Ltd Ltd]:TEST USE ONLY
Organizational Unit Name (eg, section) []:TEST USE ONLY
Common Name (eg, YOUR name) []:secure.example.org
Email Address []:dom@example.org

4. Отредактируйте файл /etc/httpd/conf.d/ssl.conf, чтобы изменить местоположение ключа и сертификата на только что созданные, например:

SSLCertificateFile /etc/pki/tls/certs/server.crt
SSLCertificateKeyFile /etc/pki/tls/private/server.key

5. Перезапустите или перезагрузите службу httpd.

6. Снова откройте https://localhost в локальном браузере и повторите процедуру проверки, приняв новый сертификат.

Для внутреннего использования или тестирования подойдет и самоподписанный сертификат. Однако для общедоступных сайтов следует применять сертификат, проверенный центром сертификации (СА). Далее описано, как это сделать.

Создание запроса на получение сертификата

Если вы планируете получить сертификат, подписаный центром сертификации (включая тот, который запускаете сами), используйте свой закрытый ключ для создания запроса на получение сертификата (CSR).

1. Создайте каталог, в котором будет храниться CSR:

# mkdir /etc/pki/tls/ssl.csr
# cd /etc/pki/tls/ssl.csr/

2. С помощью команды openssl сгенерируйте CSR. В результате в текущем каталоге будет создан CSR-файл с именем server.csr. При вводе этой информации строка Common Name должна совпадать с именем, которое клиенты будут использовать для доступа к вашему серверу. Обязательно уточните остальные детали, чтобы проверить их сторонним СА. Кроме того, если вы задали кодовую фразу для своего ключа, необходимо ввести ее, чтобы применить ключ:

# openssl req -new -key ../private/server.key -out server.csr

Country Name (2 letter code) [AU]:US