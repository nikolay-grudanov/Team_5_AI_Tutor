---
source_image: page_246.png
page_number: 246
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.20
tokens: 6423
characters: 1416
timestamp: 2025-12-24T04:01:38.664226
finish_reason: stop
---

Пример файла конфигурации можно взять из файла /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz. Его нужно распаковать в /etc/openvpn/server.conf.

После того, как распакуете шаблон файла конфигурации можно приступить к его редактированию. Откройте /etc/openvpn/server.conf в любимом текстовом редакторе.

Далее приведен фрагмент этого файла. Внимательно читайте комментарии:

# Раскомментируйте эту строку
tls-auth ta.key 0
# Установите key-direction в 0
key-direction 0
# Расскомментируйте эту строку
cipher AES-128-CBC
# Сразу после строки с cipher добавьте следующую строку:
auth SHA256
# Укажите имя пользователя и группы, от имени которых будет запускаться сервер%
user nobody
group nogroup
# Чтобы VPN-соединение использовалось для всего трафика,
# нужно «протолкнуть»
# настройки DNS на машины клиентов. Для этого раскомм.
# следующую строку:
push "redirect-gateway def1 bypass-dhcp"
# Также добавьте DNS-серверы (используем OpenDNS):
push "dhcp-option DNS 208.67.222.222"
push "dhcp-option DNS 208.67.220.220"
# При необходимости измените порт и протокол:
port 443
proto tcp
# Если при вызове build-key-server вы указали значение,
# отличное от
# «server», измените имена файлов сертификата и ключа
cert server.crt
key server.key

Теперь нужно немного настроить сам сервер. Разрешите пересылать трафик, если вы этого еще не сделали. Откройте файл sysctl.conf:

sudo mcedit /etc/sysctl.conf