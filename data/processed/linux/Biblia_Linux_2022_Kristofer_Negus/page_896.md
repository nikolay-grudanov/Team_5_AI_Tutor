---
source_image: page_896.png
page_number: 896
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.12
tokens: 7519
characters: 2065
timestamp: 2025-12-24T05:10:21.920506
finish_reason: stop
---

службы iptables, добавьте правила, как показано далее, перед последним правилом DROP или REJECT:

-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 443 -j ACCEPT

Команда setenforce 0 временно переводит SELinux в разрешительный режим. Если подключение к веб-серверу после этого завершится успешно, необходимо исправить контекст файла SELinux и/или логический тип (возможно, в данном случае только контекст файла). Должно сработать следующее:

# chcon --reference=/var/www/html /var/www/html/index.html

Если команда chmod работает, это означает, что пользователь и группа Apache не имели прав на чтение файла. Необходимо оставить эти права без изменений.

6. Чтобы применить openssl или аналогичную команду для создания собственного закрытого ключа RSA и самоподписанного SSL-сертификата, выполните следующие действия:

# yum install openssl
# cd /etc/pki/tls/private
# openssl genrsa -out server.key 1024
# chmod 600 server.key
# cd /etc/pki/tls/certs
# openssl req -new -x509 -nodes -sha1 -days 365 \
    -key /etc/pki/tls/private/server.key \
    -out server.crt
Country Name (2 letter code) [AU]: US
State or Province Name (full name) [Some-State]: NJ
Locality Name (eg, city) []: Princeton
Organization Name (eg, company) [Internet Widgits Pty Ltd]:TEST USE ONLY
Organizational Unit Name (eg, section) []:TEST USE ONLY
Common Name (eg, YOUR name) []:secure.example.org
Email Address []:dom@example.org

Теперь у вас должны быть файл ключа /etc/pki/tls/private/server.key и файл сертификата /etc/pki/tls/certs/server.crt.

7. Чтобы настроить веб-сервер Apache на использование ключа и самоподписанного сертификата для обслуживания защищенного контента (HTTPS), выполните следующие действия:
а) отредактируйте файл /etc/httpd/conf.d/ssl.conf, изменив ключ и расположение сертификата, чтобы использовать только что созданные:

SSLCertificateFile /etc/pki/tls/certs/server.crt
SSLCertificateKeyFile /etc/pki/tls/private/server.key

б) перезапустите службу httpd:

# systemctl restart httpd.service