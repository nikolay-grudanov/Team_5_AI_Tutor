---
source_image: page_735.png
page_number: 735
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.77
tokens: 7690
characters: 2249
timestamp: 2025-12-24T05:06:05.376059
finish_reason: stop
---

Суть этих действий состоит в том, чтобы сравнить, как выглядит ваш Linux-сервер изнутри и снаружи. Если вы определили, что сетевые службы, которые должны быть закрыты, доступны для других, необходимо заблокировать доступ к ним с внешних интерфейсов.

СОВЕТ
Может возникнуть соблазн не выполнять сканирование из внутренней сети вашей организации. Так поступать не стоит. Вредоносную деятельность часто ведут сами сотрудники компании или кто-то, кто уже проник через внешнюю защиту. И здесь утилита nmap очень помогает. Чтобы получить правильное представление о том, какие порты вашего Linux-сервера видны, нужно провести сканирование из нескольких мест. Например, простой аудит настроил бы сканирование:

■ на самом сервере Linux;
■ с другого сервера в той же сети организации;
■ за пределами сети организации.

В следующих примерах выполняется часть простого аудита. Утилита nmap запускается в системе Fedora, обозначенной как Host-A. Host-A — это сервер Linux, сетевые службы которого должны быть защищены. Host-B — это Linux-сервер, использующий дистрибутив Linux Mint и находящийся в той же сети, что и Host-A.

СОВЕТ
При проведении аудиторских проверок следует учитывать параметры безопасности различных сетевых компонентов, таких как брандмауэр сервера и маршрутизаторы компании.

В этом примере аудита сканирование выполняется с хоста-А с использованием не адреса обратной связи, а фактического IP-адреса. Сначала IP-адрес для Host-A определяется с помощью команды ip addr show. IP-адрес — 10.140.67.23:

# ip addr show
fconfig
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
        valid_lft forever preferred_lft forever
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel
    state UP group default qlen 1000
    link/ether 52:54:00:c4:27:4e brd ff:ff:ff:ff:ff:ff
    inet 10.140.67.23/24 brd 10.140.67.255 scope global dynamic noprefixroute ens3
        valid_lft 3277sec preferred_lft 3277sec
    inet6 fe80::5036:9ec3:2ae8:7623/64 scope link noprefixroute
        valid_lft forever preferred_lft forever