---
source_image: page_904.png
page_number: 904
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.13
tokens: 7563
characters: 2045
timestamp: 2025-12-24T05:10:34.712544
finish_reason: stop
---

904 Приложения

/usr/share/man/man5/exports.5.gz
/usr/share/man/man5/nfs.5.gz
/usr/share/man/man5/nfsmount.conf.5.gz
/usr/share/man/man7/nfsd.7.gz
/usr/share/man/man8/blkmapd.8.gz
/usr/share/man/man8/exportfs.8.gz
...

3. Чтобы запустить и включить службу NFS, введите от имени суперпользователя на сервере NFS следующие данные:

# systemctl start nfs-server.service
# systemctl enable nfs-server.service

4. Чтобы проверить состояние только что запущенной службы NFS, от имени суперпользователя введите следующее:

# systemctl status nfs-server.service

5. Чтобы сделать каталог /var/mystuff доступным для всех, но только для чтения суперпользователем на клиенте, который имеет основной доступ к общему ресурсу, сначала создайте каталог монтирования следующим образом:

# mkdir /var/mystuff

Затем создайте запись в файле /etc/exports, как в примере далее:

/var/mystuff *(ro,no_root_squash,insecure)

Чтобы сделать общий ресурс доступным, введите следующее:

# exportfs -v -a
exporting *:/var/mystuff

6. Чтобы убедиться, что созданный вами общий ресурс доступен всем хостам, сначала убедитесь, что демон rpcbind не заблокирован TCP-оболочками, добавив следующую запись в начало файла /etc/hosts.allow:

rpcbind: ALL

а) чтобы открыть брандмауэр в системах, использующих службу firewalld (RHEL 8 и недавние системы Fedora), установите пакет firewall-config. Затем запустите firewall-config из появившегося окна Firewall (Межсетевой экран), убедитесь, что NFS и rpc-bind включены в постоянные настройки брандмауэра;
б) чтобы открыть порты, позволяющие клиентам войти на сервер NFS через брандмауэр iptables (на RHEL 6 и более ранних системах Fedora, где нет службы firewalld), нужно открыть порты TCP и UDP 111 (демон rpcbind), 20048 (mountd) и 2049 (NFS), добавив следующее правило в файл /etc/sysconfig/iptables и при запуске службы iptables:

-A INPUT -m state --state NEW -m tcp -p tcp --dport 111 -j ACCEPT
-A INPUT -m state --state NEW -m udp -p udp --dport 111 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 2049 -j ACCEPT