---
source_image: page_890.png
page_number: 890
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.20
tokens: 7549
characters: 1850
timestamp: 2025-12-24T05:10:11.299277
finish_reason: stop
---

Kernel IP routing table
Destination   Gateway   Genmask   Flags Metric Ref Use Iface
192.168.0.1   0.0.0.0   255.255.255.0   U   600   0   0 enp4s0
192.168.99.0  192.168.0.5 255.255.255.0   UG  600   0   0 enp4s0

10. Чтобы проверить, настроена ли ваша система на маршрутизацию пакетов IPv4 между сетевыми интерфейсами, введите следующее:

# cat /proc/sys/net/ipv4/ip_forward
0

Значение 0 показывает, что переадресация пакетов IPv4 отключена, значение 1 — что включена.

Глава 15. Запуск и остановка служб

1. Чтобы определить, какой демон инициализации используется вашим сервером в данный момент, рассмотрим следующее:
а) в большинстве случаев PID 1 задействуется как демон systemd:

# ps -ef | head
UID     PID  PPID  C STIME TTY      TIME CMD
root    1     0   0 17:01 ?        00:00:04 /usr/lib/systemd/systemd --
switched-root --system --deserialize 18

Если ввести команду ps -ef и PID 1 — это init, то это все равно может быть демон systemd. Задействуйте команду strings, чтобы узнать, используется ли демон systemd в системе:

# strings /sbin/init | grep -i systemd
systemd.unit=
systemd.log_target=
systemd.log_level=
...

б) скорее всего, у вас есть демон инициализации Upstart, SysVinit или BSD, если ваш демон init не является systemd. Но лучше это дважды проверить на wikipedia.org/wiki/Init.

2. Инструменты, применяемые для управления службами, в первую очередь зависят от используемой системы инициализации. Запустите команды systemctl и service, чтобы определить тип сценария инициализации для службы ssh в вашей системе:
а) для демона systemd положительный результат, показанный здесь, означает, что служба sshd была преобразована в systemd:

# systemctl status sshd.service
sshd.service - OpenSSH server daemon
Loaded: loaded (/lib/systemd/system/sshd.service; enabled)
Active: active (running) since Mon, 20 Apr 2020 12:35:20...