---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.68
tokens: 6445
characters: 1649
timestamp: 2025-12-24T03:59:48.942739
finish_reason: stop
---

Когда-то стандартом де-факто был wu-ftpd. Старый и проверенный временем сервер. На данный момент он полностью вытеснен ProFTPD и по ряду причин рекомендуется использовать именно ProFTPD.

Для небольших проектов можно использовать ruge-ftpd — это простой сервер, который вообще не нужно настраивать, но на производственных (читайте — реальных) серверах его использовать не рекомендуется.

9.2. Универсальный солдат - ProFTPD

9.2.1. Установка и управление сервером

Данный сервер устанавливается, как и любой другой — путем установки соответствующего пакета, который в данном случае называется proftpd. Пакет имеется практически во всех дистрибутивах Linux и называется везде одинаково, что упрощает его установку (не нужно загружать его исходники, выполнять компиляцию, нужно только подставить имя пакета в команду установки). Для установки нужно ввести одну из команд в зависимости от дистрибутива Linux:

sudo apt install proftpd      # Ubuntu, Debian
sudo dnf install proftpd       # Fedora, CentOS

Конфигурация сервера хранится в каталоге /etc/proftpd. Основной конфигурационный файл называется proftpd.conf и будет рассмотрен в следующем разделе. В некоторых дистрибутивах файл proftpd.conf находится в каталоге /etc, то есть полное его имя - /etc/proftpd.conf

Для управления сервером (для запуска, перезапуска, останова) используются следующие команды:

sudo systemctl start proftpd
sudo systemctl restart proftpd
sudo systemctl stop proftpd
sudo systemctl status proftpd

В старых дистрибутивах используется команда service вместо systemctl:

# service proftpd start
# service proftpd restart
# service proftpd stop
# service proftpd status