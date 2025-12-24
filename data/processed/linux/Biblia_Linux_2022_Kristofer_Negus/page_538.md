---
source_image: page_538.png
page_number: 538
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.13
tokens: 7762
characters: 2640
timestamp: 2025-12-24T05:00:38.482787
finish_reason: stop
---

Настройка брандмауэра для сервера Samba

Если брандмауэр iptables или firewalld настроен для системы при ее установке, он обычно разрешает любые запросы на услуги от локальных, но не от внешних пользователей. Вот почему при установке (как сказано в посвященном ей разделе в этой главе) необходимо проверить, подключается ли служба Samba с помощью команды smbclient из локальной системы. Но если бы запрос исходил из другой системы, он был бы отклонен.

Настройка правил брандмауэра для Samba в основном состоит из открытия входящих портов, на которых прослушиваются демоны smbd и nmbd. Перечислю порты, которые необходимо открыть, чтобы получить работающий сервис Samba в вашей системе Linux.

• Порт TCP 445. Это основной порт, на котором слушает демон Samba smbd. Брандмауэр должен поддерживать входящие на этот порт пакетные запросы, чтобы служба Samba работала.
• Порт TCP 139. Демон smbd также прослушивает порт TCP 139 для того, чтобы обрабатывать данные, связанные с именами хостов NetBIOS. Службу Samba можно использовать через порт TCP, не открывая порт, но это не рекомендуется.
• Порты UDP 137 и 138. Демон nmbd использует эти два порта для входящих запросов NetBIOS. Если вы применяете демон nmbd, они должны быть открыты для новых пакетных запросов для разрешения имен NetBIOS.

Для систем Fedora и RHEL разрешить входящий доступ к этим четырем портам очень просто. Откройте окно Firewall Configuration (Брандмауэр) и на вкладке Services (Службы) установите флажки samba и sambaclient. Эти порты сразу становятся доступными (без перезапуска службы firewalld).

Для более ранних систем Fedora и RHEL, которые используют службу iptables вместо службы firewalld, открытие брандмауэра — это ручной процесс. Рассмотрим брандмауэр по умолчанию дистрибутива Fedora, который разрешает входящие пакеты от локального хоста и от установленных соединений и связанных с установленными соединениями пакетов, но запрещает все остальные входящие пакеты. В следующем примере представлен набор правил брандмауэра в файле /etc/sysconfig/iptables с четырьмя новыми правилами (выделены):

*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT
-I INPUT -m state --state NEW -m udp -p udp --dport 137 -j ACCEPT
-I INPUT -m state --state NEW -m udp -p udp --dport 138 -j ACCEPT
-I INPUT -m state --state NEW -m tcp -p tcp --dport 139 -j ACCEPT
-I INPUT -m state --state NEW -m tcp -p tcp --dport 445 -j ACCEPT
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
COMMIT