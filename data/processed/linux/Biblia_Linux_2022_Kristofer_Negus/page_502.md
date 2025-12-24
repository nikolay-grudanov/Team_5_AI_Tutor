---
source_image: page_502.png
page_number: 502
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.67
tokens: 7453
characters: 1892
timestamp: 2025-12-24T04:59:28.573953
finish_reason: stop
---

State or Province Name (full name) [Some-State]:Washington
Locality Name (eg, city) []:Bellingham
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Example Company, LTD.
Organizational Unit Name (eg, section) []:Network Operations
Common Name (eg, YOUR name) []:secure.example.org
Email Address []:dom@example.org

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:

3. Перейдите на сайт выбранного центра подписи сертификатов и запросите подпись для сертификата. Сайт CA, скорее всего, попросит вас скопировать содержимое своего CSR (в данном примере файл server.csr) и вставить в форму.

4. Когда CA отправит вам сертификат (возможно, по электронной почте), сохраните его в каталоге /etc/pki/tls/certs/, используя имя своего сайта, например, example.org.crt.

5. Измените значение SSLCertificateFile в файле /etc/httpd/conf.d/ssl.conf и укажите новый CRT-файл. Если у вас несколько хостов SSL, можете создать отдельную запись (возможно, в отдельном файле .conf), которая выглядит следующим образом:

Listen 192.168.0.56:443
<VirtualHost *:443>
    ServerName secure.example.org
    ServerAlias web.example.org
    DocumentRoot /home/username/public_html/
    DirectoryIndex index.php index.html index.htm
    SSLEngine On
    SSLCertificateKeyFile /etc/pki/tls/private/server.key
    SSLCertificateFile /etc/pki/tls/certs/example.org.crt
</VirtualHost>

IP-адрес, показанный в директиве Listen, следует заменить общедоступным IP-адресом, представляющим обслуживаемый вами SSL-хост. Помните, что каждый SSL-хост должен иметь собственный IP-адрес.

Диагностика веб-сервера

В любой достаточно сложной среде всегда возникают проблемы. В следующих пунктах приведены советы по выявлению и устранению наиболее распространенных ошибок, с которыми вы можете столкнуться в ходе работы с веб-сервером.