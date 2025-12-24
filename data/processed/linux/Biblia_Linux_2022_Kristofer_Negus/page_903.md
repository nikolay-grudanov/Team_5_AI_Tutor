---
source_image: page_903.png
page_number: 903
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.51
tokens: 7491
characters: 1837
timestamp: 2025-12-24T05:10:30.668129
finish_reason: stop
---

-A INPUT -i lo -j ACCEPT
-I INPUT -m state --state NEW -m udp -p udp --dport 137 -j ACCEPT
-I INPUT -m state --state NEW -m udp -p udp --dport 138 -j ACCEPT
-I INPUT -m state --state NEW -m tcp -p tcp --dport 139 -j ACCEPT
-I INPUT -m state --state NEW -m tcp -p tcp --dport 445 -j ACCEPT
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
COMMIT

Затем введите следующую команду для правил брандмауэра, чтобы перезагрузить его:

# service iptables restart

10. Чтобы снова открыть общий ресурс [homes] от имени пользователя phil из другой системы в вашей сети (Windows или Linux) и убедиться, что можете перетащить в него файлы, выполните следующие действия:
а) сначала повторите описанный ранее пример окна Nautilus (Файлы) или обратитесь к окну Explorer (Проводник) в Windows и откройте общий ресурс, выбрав сеть, а затем сервер Samba. Сложность заключается в том, что служба должна быть доступна в функциях безопасности сервера Linux;
б) если не можете получить доступ к общему ресурсу Samba, отключите брандмауэр, а затем отключите SELinux. Если общий ресурс доступен при отключении любой из этих служб, вернитесь назад и ликвидируйте проблему с неработающей службой:

# setenforce 0
# service iptables stop

в) когда исправите ее, вновь установите SELinux в принудительный режим и перезапустите службу iptables:

# setenforce 1
# service iptables start

Глава 20. Настройка NFS-сервера

1. Чтобы установить пакеты, необходимые для настройки службы NFS в выбранной вами системе Linux, введите от имени суперпользователя (в системе Fedora или RHEL) следующую команду:

# yum install nfs-utils

2. Чтобы перечислить файлы документации, входящие в пакет программного обеспечения сервера NFS, введите следующее:

# rpm -qd nfs-utils
/usr/share/doc/nfs-utils-1.2.5/ChangeLog
...