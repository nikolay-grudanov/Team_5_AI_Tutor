---
source_image: page_730.png
page_number: 730
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.40
tokens: 7559
characters: 2190
timestamp: 2025-12-24T05:05:50.500753
finish_reason: stop
---

#
# Note that it is presently the policy of IANA to assign ...
# Each line describes one service, and is of the form:
#
# service-name    port/protocol   [aliases ...]   [# comment]
...
echo                7/tcp
echo                7/udp
discard             9/tcp        sink null
discard             9/udp        sink null
systat              11/tcp       users
systat              11/udp       users
daytime             13/tcp
daytime             13/udp
qotd                17/tcp       quote
qotd                17/udp       quote
...
chargen             19/tcp       ttytst source
chargen             19/udp       ttytst source
ftp-data            20/tcp
ftp-data            20/udp
# 21 is registered to ftp, but also used by fsp
ftp                 21/tcp
...
http                80/tcp       www www-http   # WorldWideWeb HTTP
http                80/udp       www www-http   # HyperText Transfer
Protocol
http                80/sctp      # HyperText Transfer
Protocol
kerberos            88/tcp       kerberos5 krb5 # Kerberos v5
kerberos            88/udp       kerberos5 krb5 # Kerberos v5
...
blp5                48129/udp    # Bloomberg locator
com-bardac-dw       48556/tcp    # com-bardac-dw
com-bardac-dw       48556/udp    # com-bardac-dw
iqobject            48619/tcp    # iqobject
iqobject            48619/udp    # iqobject

Обратите внимание на три столбца информации, идущих после строк с комментариями. Левый столбец содержит названия всех служб. Средний определяет номер порта и тип протокола, используемого для этой службы. Правый содержит необязательный псевдоним или список псевдонимов для службы.

Многие дистрибутивы Linux поставляются с запущенными ненужными сетевыми службами. Такая служба угрожает безопасности вашей системы Linux. Например, если ваш сервер Linux является сервером печати, то он должен оказывать только услуги печати и не должен задействовать веб-сервисы Apache. Из-за этого ваш сервер печати может без необходимости подвергнуться любым вредоносным атакам, использующим уязвимости веб-служб.

Первоначально ограничение количества служб в системах Linux означало установку отдельных физических серверов Linux, на каждом из которых работали всего