---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.19
tokens: 7588
characters: 1999
timestamp: 2025-12-24T04:39:16.108839
finish_reason: stop
---

46 you-re.saddled.up (162.252.205.154) 310.332 ms 308.226 ms 307.612 ms
47 there-s.no.recourse (162.252.205.155) 316.779 ms 315.848 ms 311.799 ms
48 it-s.hi-ho.silver (162.252.205.156) 320.175 ms 311.570 ms 319.072 ms
49 signed.bad.horse (162.252.205.157) 313.125 ms 311.095 ms 321.902 ms

6.2.2. Автоматическое конфигурирование

За автоматическое конфигурирование сетевых интерфейсов отвечает менеджер сетевых подключений — системная служба networkmanager(8), отслеживающая физическую активацию сетевых адаптеров (подключение сетевого кабеля Ethernet или подключения к сети Wi-Fi) и взаимодействующая с другими службами, например со службой wpa_supplicant(8) (для ассоциации с Wi-Fi точками доступа и аутентификации) или с локальной службой W:[DNS] systemd-resolved(1) (см. разд. 6.3). Кроме этого, менеджер сетевых подключений может запускать «подчиненные» службы, например W:[DHCP]-клиента dhclient(8) или dhcpd(8) для автоматического получения IP-адреса, простейший локальный DNS-сервер dnsmasq(8) и т. д.

Для взаимодействия с менеджером сетевых подключений предназначены команда nmcli(1) (см. также nmcli-examples(7)), TUI-приложения nmtui(1), nmtui-edit(1), nmtui-connect(1) и GUI-приложения nm-applet(1), nm-connection-editor(1), позволяющие опрашивать его состояние и управлять его действиями.

Листинг 6.9. Конфигурирование сетевых интерфейсов (автоматически)

lumpy@ubuntu:~$ nmcli dev
DEVICE   TYPE   STATE   CONNECTION
wlp2s0   wifi   подключено   474+
eno1     ethernet   отключено   --
lo       loopback   не настроено   --

lumpy@ubuntu:~$ nmcli dev show eno1
GENERAL.DEVICE:                eno1
GENERAL.TYPE:                   ethernet
GENERAL.HWADDR:                 08:00:27:C0:67:8F
GENERAL.MTU:                    1500
GENERAL.STATE:                  30 (отключено)
GENERAL.CONNECTION:             --
GENERAL.CON-PATH:               --
WIRED-PROPERTIES.CARRIER:      вкл.

1 При помощи механизмов службы W:[D-Bus], требующей отдельного разговора, выходящего за рамки этой книги.