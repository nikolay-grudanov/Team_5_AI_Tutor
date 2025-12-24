---
source_image: page_905.png
page_number: 905
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.94
tokens: 7530
characters: 1970
timestamp: 2025-12-24T05:10:33.532127
finish_reason: stop
---

-A INPUT -m state --state NEW -m udp -p udp --dport 2049 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 20048 -j ACCEPT
-A INPUT -m state --state NEW -m udp -p udp --dport 20048 -j ACCEPT

Система SELinux должна иметь возможность совместно задействовать файловые системы NFS в принудительном режиме без каких-либо изменений в контекстах файлов или логических типах. Чтобы убедиться в том, что созданный общий ресурс доступен только для чтения, выполните от имени суперпользователя на сервере NFS следующую команду:

# setsebool -P nfs_export_all_ro on

7. Чтобы просмотреть общие ресурсы, доступные на сервере NFS (имя сервера NFS — nfsserver), введите в клиенте NFS следующее:

# showmount -e nfsserver
Export list for nfsserver:
/var/mystuff *

8. Чтобы создать каталог /var/remote и временно смонтировать каталог /var/mystuff с сервера NFS (в данном примере nfsserver) в этой точке монтирования, введите в качестве суперпользователя следующее:

# mkdir /var/remote
# mount -t nfs nfsserver:/var/mystuff /var/remote

9. Чтобы добавить запись так, чтобы то же самое монтирование выполнялось автоматически при перезагрузке, сначала размонтируйте каталог /var/remote следующим образом:

# umount /var/remote

Затем добавьте в файл /etc/fstab следующую запись:

/var/remote    nfsserver:/var/mystuff    nfs bg,ro 0 0

Чтобы проверить правильность настроек общего ресурса, введите в клиенте NFS в качестве суперпользователя следующие данные:

# mount -a
# mount -t nfs4
nfsserver:/var/mystuff on /var/remote type nfs4
(ro,vers=4,rsize=524288...

10. Чтобы скопировать некоторые файлы в каталог /var/mystuff, введите на сервере NFS следующую команду:

# cp /etc/hosts /etc/services /var/mystuff

Чтобы убедиться, что вы можете видеть только что добавленные в этот каталог файлы и не можете записывать файлы в него из клиента, введите:

# ls /var/remote
hosts    services
# touch /var/remote/file1
touch: cannot touch '/var/remote/file1': Read-only file system