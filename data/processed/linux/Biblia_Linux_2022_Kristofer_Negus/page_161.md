---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.74
tokens: 7686
characters: 2499
timestamp: 2025-12-24T04:49:38.673006
finish_reason: stop
---

Вот что нужно знать о поиске файлов с помощью команды locate.

● Команда locate имеет и преимущества, и недостатки по сравнению с командой find. Она находит файлы быстрее, потому что ищет по готовой базе данных, а не по всей файловой системе. Недостатком является то, что locate не учитывает файлы, добавленные в систему после последнего обновления базы данных.
● Не каждый файл файловой системы хранится в базе данных. Содержимое файла /etc/updatedb.conf ограничивает, какие имена файлов отсекаются в зависимости от выбранных типов монтирования, типов файловой системы, типов файлов и точек монтирования. Например, не собираются имена файлов из удаленных файловых систем (cifs, inf и т. д.) или локально смонтированных CD или DVD (iso9660). Пути, содержащие временные файлы (/tmp) и файлы в очереди обработки (/var/spool/cups), также исключаются. При необходимости отсекаемые элементы можно добавить в базы данных locate или удалить из них. В дистрибутиве RHEL 8 файл updatedb.conf содержит:

PRUNE_BIND_MOUNTS = "yes"
PRUNESFS = "9p afs anon_inodefs auto autofs bdev binfmt_misc cgroup cifs coda configfs cpuset debugfs devpts ecryptfs exofs fuse fuse .sshfs fusectl gfs gfs2 gpfs hugetlbfs inotifyfs iso9660 jffs2 lustre mqueue ncpfs nfs nfs4 nfsd pipefs proc ramfs rootfs rpc_pipefs securityfs selinuxfs sfs sockfs sysfs tmpfs ubifs udf usbfs ceph fuse.ceph"
PRUNENAMES = ".git .hg .svn .bzr .arch-ids {arch} CVS"
PRUNEPATHS = "/afs /media /mnt /net /sfs /tmp /udev /var/cache/ ccache /var/lib/yum/yumdb /var/lib/dnf/yumdb /var/spool/cups /var/spool/squid /var/tmp /var/lib/ceph"

Обычный пользователь не может просматривать файлы из базы данных locate, которые не отображаются в файловой системе. Например, если не получается ввести ls для просмотра файлов в каталоге /root, то и файлы, хранящиеся в этом каталоге, найти не получится.

● Строка, которую ищут, может находиться в любом месте пути к файлу. Например, при поиске passwd можно найти /etc/passwd, /usr/bin/passwd, /home/chris/passwd/pwdfiles.txt и многие другие файлы со словом passwd в пути.
● Если добавить файлы в систему после запуска updatedb, их нельзя будет найти до тех пор, пока updatedb не запустится снова (вероятно, в ту же ночь). Чтобы база данных содержала все файлы, появившиеся до текущего момента, можно снова запустить updatedb из оболочки от имени суперпользователя.

Пример использования команды locate для поиска файлов:

$ locate .bashrc
/etc/skel/.bashrc
/home/cnegus/.bashrc
# locate .bashrc
/etc/skel/.bashrc