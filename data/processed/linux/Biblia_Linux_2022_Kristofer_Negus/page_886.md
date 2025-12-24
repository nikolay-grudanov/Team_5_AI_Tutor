---
source_image: page_886.png
page_number: 886
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.20
tokens: 7583
characters: 2066
timestamp: 2025-12-24T05:10:05.219736
finish_reason: stop
---

$ ssh joe@localhost "cat newfile"
joe@localhost's password: *********
This is text from the file I saved in joe's remote home directory

4. Чтобы рекурсивно скопировать все файлы из каталога /usr/share/selinux удаленной системы в каталог /tmp локальной системы таким образом, чтобы все время изменения файлов обновлялось до времени их копирования в локальной системе, выполните следующее:

$ scp -r joe@localhost:/usr/share/selinux /tmp
joe@localhost's password:
*********
irc.pp.bz2                100% 9673   9.5KB/s  00:00
dcc.pp.bz2                100% 15KB  15.2KB/s  00:01
$ ls -l /tmp/selinux | head
total 20
drwxr-xr-x. 3 root root 4096 Apr 18 05:52 devel
drwxr-xr-x. 2 root root 4096 Apr 18 05:52 packages
drwxr-xr-x. 2 root root 12288 Apr 18 05:52 targeted

5. Чтобы рекурсивно скопировать все файлы из каталога /usr/share/logwatch удаленной системы в каталог /tmp локальной системы таким образом, чтобы все время изменения файлов из удаленной системы сохранялись в локальной, выполните следующие действия:

$ rsync -av joe@localhost:/usr/share/logwatch /tmp
joe@localhost's password: *********
receiving incremental file list
logwatch/
logwatch/default.conf/
logwatch/default.conf/logwatch.conf
$ ls -l /tmp/logwatch | head
total 16
drwxr-xr-x. 5 root root 4096 Apr 19 2011 default.conf
drwxr-xr-x. 4 root root 4096 Feb 28 2011 dist.conf
drwxr-xr-x. 2 root root 4096 Apr 19 2011 lib

6. Чтобы создать пару «открытый/закрытый ключ» для применения для SSH-связи (без ключевой фразы), скопируйте файл открытого ключа в учетную запись удаленного пользователя с помощью команды ssh-copy-id и примените аутентификацию на основе ключа для входа в эту учетную запись пользователя без ввода пароля:

$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/joe/.ssh/id_rsa): ENTER
/home/joe/.ssh/id_rsa already exists.
Enter passphrase (empty for no passphrase): ENTER
Enter same passphrase again: ENTER
Your identification has been saved in /home/joe/.ssh/id_rsa.
Your public key has been saved in /home/joe/.ssh/id_rsa.pub.