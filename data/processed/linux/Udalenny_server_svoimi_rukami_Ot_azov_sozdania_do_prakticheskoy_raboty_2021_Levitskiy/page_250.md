---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.65
tokens: 6309
characters: 1159
timestamp: 2025-12-24T04:01:41.286474
finish_reason: stop
---

cd ~/clients
./make_config user1

Если все прошло успешно, то в ~/clients/files вы найдете файл user1.ovpn.

14.5.3. Подключаем клиентов

Передайте файлы конфигурации (.ovpn) клиентам. Можете отправить по электронной почте вместе со следующей инструкцией.

Сначала рассмотрим настройку клиента в Linux. Установите openvpn:
sudo apt-get install openvpn

Откройте файл user1.ovpn, полученный с сервера. Раскомментируйте следующие строки:
script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf

Если в вашем дистрибутиве нет файла /etc/openvpn/update-resolv-conf, то делать ничего не нужно!

Теперь подключитесь к VPN-серверу:
sudo openvpn --config user1.ovpn

В Windows полученный .ovpn-файл нужно поместить в каталог C:\Program Files\OpenVPN\config, предварительно установив клиент OpenVPN для Windows. Загрузить эту программу можно с официальной странички проекта https://openvpn.net/index.php/open-source/downloads.html.

После запуска OpenVPN он должен автоматически увидеть ваш профиль. Щелкните на пиктограмме клиента на панели быстрого запуска правой кнопкой мыши и выберите команду Подключиться. Все достаточно просто.