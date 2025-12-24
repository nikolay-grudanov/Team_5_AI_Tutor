---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.13
tokens: 6340
characters: 1260
timestamp: 2025-12-24T04:01:40.963681
finish_reason: stop
---

sudo ufw disable
sudo ufw enable

Все готово для запуска VPN-сервера. Запустим его командой:
sudo systemctl start openvpn@server

Проверить состояние сервера можно так:
sudo systemctl status openvpn@server

Вы должны увидеть что-то вроде этого:
openvpn@server.service - OpenVPN connection to server
    Loaded: loaded (/lib/systemd/system/openvpn@.service; disabled; vendor preset: enabled)
    Active: active (running) since Tue 2020-07-10 13:16 0:05 EDT; 25s ago

Если все нормально, тогда обеспечим автоматический запуск сервера:
sudo systemctl enable openvpn@server

Теперь готовимся встречать клиентов. Прежде, чем клиенты смогут подключиться, нужно позаботиться об инфраструктуре настройки клиентов. Создадим каталог для хранения файлов:
mkdir -p ~/clients/files
chmod 700 ~/clients/files

Такие права доступа нужны, поскольку данный каталог будет содержать ключи клиентов.

Далее установим базовую конфигурацию:
cd /usr/share/doc/openvpn/examples/sample-config-files/
cp client.conf ~/clients/base.conf

Откройте файл ~/clients/base.conf. В нем нужно сделать несколько изменений:

# Укажите IP-адрес сервера и порт (1193 для UDP или 443 для TCP)
remote IP-адрес порт
# Укажите протокол udp или tcp
proto протокол
# Раскомментируйте директивы
user nobody