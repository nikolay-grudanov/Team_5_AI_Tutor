---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.00
tokens: 7741
characters: 1693
timestamp: 2025-12-24T04:24:35.681965
finish_reason: stop
---

defaults
{
    instances                = 60
    log_type                 = SYSLOG authpriv
    log_on_success           = HOST PID
    log_on_failure           = HOST
    cps                      = 25 30
}
includedir /etc/xinetd.d

После ключевого слова defaults в фигурных скобках описываются настройки по умолчанию для всех сервисов. Любое из этих значений можно изменить для каждого отдельного сервиса.

Последняя строка подключает каталог /etc/xinet.d. В этом каталоге для каждой службы есть собственный конфигурационный файл, где можно изменить параметры. Имена файлов соответствуют названиям сервисов, а содержимое — похоже на /etc/xinetd.conf. В листинге 5.4 приведено содержимое конфигурационного файла /etc/xinet.d/telnet для сервиса Telnet.

Листинг 5.4. Конфигурационный файл для сервиса Telnet

# default: on
# По умолчанию включен
# description: The telnet server serves telnet sessions; it uses \
#   unencrypted username/password pairs for authentication.
# Описание: telnet-сервис обслуживает сессии telnet. Он использует
#   незашифрованные имя пользователя и пароль для аутентификации
service telnet
{
    disable      = no
    flags        = REUSE
    socket_type  = stream
    wait         = no
    user         = root
    server       = /usr/sbin/in.telnetd
    log_on_failure += USERID
}

Рассмотрим основные параметры, которые можно изменять:

☐ disable — параметр, установка которого в yes запрещает исполнение сервиса.
Как уже говорилось, сервис Telnet небезопасен, и поэтому имеет смысл его запретить;

☐ flags — атрибуты выполнения сервиса;

☐ socket_type — тип используемого сокета. Для протокола TCP здесь должно быть значение stream, а для протокола UDP — dgram;