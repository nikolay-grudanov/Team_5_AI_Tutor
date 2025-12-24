---
source_image: page_398.png
page_number: 398
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.79
tokens: 7721
characters: 1573
timestamp: 2025-12-24T04:29:58.392163
finish_reason: stop
---

Листинг 14.1. Конфигурационный файл /etc/sysctl.conf

# Kernel sysctl configuration file for Red Hat Linux
# Конфигурационный файл ядра для Red Hat Linux

# For binary values, 0 is disabled, 1 is enabled.
# See sysctl(8) for more details.
# Для бинарных значений 0 — это отключен, а 1 — включен.
# Смотрите man sysctl для получения дополнительной информации

# Controls IP packet forwarding
# Контролирует переадресацию IP-пакетов
net.ipv4.ip_forward = 0

# Controls source route verification
# Контроль проверки маршрутизации от источника
net.ipv4.conf.default.rp_filter = 1

kernel.sysrq = 1

kernel.core_uses_pid = 1

#net.ipv4.tcp_ecn = 0

kernel.grsecurity.fifo_restrictions = 1
kernel.grsecurity.linking_restrictions = 1

# audit some operations
# Аудит некоторых операций
kernel.grsecurity.audit_mount = 1
kernel.grsecurity.signal_logging = 1
#kernel.grsecurity.suid_logging = 1
kernel.grsecurity.timechange_logging = 1
kernel.grsecurity.forkfail_logging = 1
kernel.grsecurity.coredump = 1

# lock all security options
# Блокировка всех опций безопасности
#kernel.grsecurity.grsec_lock = 1

Что представляют собой параметры, которые вы видите в этом файле? Попробуем разобраться на примере net.ipv4.tcp_ecn. На самом деле это путь к файлу относительно каталога /proc/sys, в котором все символы косой черты заменены точками. В данном случае имеется в виду файл /proc/sys/net/ipv4/tcp_ecn. Выполните следующую команду, чтобы просмотреть содержимое файла:

cat /proc/sys/net/ipv4/tcp_ecn

В результате на экране вы должны увидеть 0 или 1. Это и есть значение параметра.