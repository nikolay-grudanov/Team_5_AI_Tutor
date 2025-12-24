---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.12
tokens: 6446
characters: 1368
timestamp: 2025-12-24T04:00:16.709905
finish_reason: stop
---

режиме. Мы же будем использовать Unbound сугубо в кэширующем режиме.

Основной файл конфигурации называется /etc/unbound/unbound.conf. По умолчанию он практически пуст, а полный пример со всеми возможными опциями можно найти в каталоге /usr/share/doc/unbound/examples.

В листинге 10.1 представлен листинг /etc/unbound/unbound.conf, настраивающий Unbound на работу в кэширующем режиме.

Листинг 10.1. Файл /etc/unbound/unbound.conf

server:
# Порт, на котором наш сервер будет «слушать» запросы
port: 53
# Описываем интерфейсы, на которых мы будем слушать запросы
# 192.168.1.1 - сервер нашей локальной сети, на котором установлен Unbound
interface: 127.0.0.1
interface: 192.168.1.1
# Исходящий интерфейс (WAN)
outgoing-interface: xxx.xxx.xxx.xxx
# Сеть, которой разрешен доступ к нашему серверу
access-control: 192.168.1.0/24 allow
# Разрешаем IPv4 TCP/UDP, запрещаем IPv6
do-ip4: yes
do-ip6: no
do-udp: yes
do-tcp: yes
# Пользователь, от имени которого будет запускаться сервер
username: unbound
# Указываем файл журнала и отключаем использование syslog
logfile: "unbound.log"
use-syslog: no
# Путь к PID-файлу
pidfile: "/var/run/local_unbound.pid"
# Скрываем версию софта
hide-version: yes
# Уровень журналирования - 0 (только ошибки)
verbosity: 0
# Следующая строка настраивает Unbound на осуществление криптографической
# валидации DNSSEC, используя корневой ключ