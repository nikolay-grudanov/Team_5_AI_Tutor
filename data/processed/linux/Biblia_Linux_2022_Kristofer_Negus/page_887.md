---
source_image: page_887.png
page_number: 887
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.55
tokens: 7743
characters: 1932
timestamp: 2025-12-24T05:10:13.610058
finish_reason: stop
---

The key fingerprint is:
58:ab:c1:95:b6:10:7a:aa:7c:c5:ab:bd:f3:4f:89:1e joe@cnegus.csb
The key's randomart image is:
...
$ ssh-copy-id -i ~/.ssh/id_rsa.pub joe@localhost
joe@localhost's password: **********
Now try logging into the machine, with "ssh 'joe@localhost'",
and check in:
.ssh/authorized_keys
to make sure we haven't added extra keys that you weren't expecting.
$ ssh joe@localhost
$ cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAyN2Psp5/LRUC9E8BDCx53yPUa0qoOPdv6H4sF3vmn04V6E7D1iXpzwPzdo4rpvmR1ZiinHR2xGAEr2uZag7feKgLnww2KPcQ6SiR7lzrOhQjV+SGb/a1dxrIeZqKMq1Tk07G4EvboIrq//9J47vI4l7iNu0xRmjI3TTxaDdCTbpG6J3uSJm1BKzdUtwb413x35W2bRgMI75aIdeBsDgQBBiOdu+zuTMrXJj2viCA XeJ7gIWvBaMQdOSvSdlkX353tmIjmJheWdgCccM/1jKdoELpaevg9anCe/yUP3so31 tTo4I+qTfzAQD5+66oqW0LgMkWvfZI7dUz3WUPmcMw== chris@abc.example.com

7. Чтобы создать в файле /etc/rsyslog.conf запись, которая хранит все сообщения аутентификации на уровне информации и выше в файле с именем /var/log/myauth, выполните показанные далее действия. Наблюдайте с терминала, как поступают данные:

# vim /etc/rsyslog.conf
authpriv.info /var/log/myauth
# service rsyslog restart
or
# systemctl restart rsyslog.service
<Terminal 1> <Terminal 2>
# tail -f /var/log/myauth
Apr 18 06:19:34 abc unix_chkpwd[30631]
Apr 18 06:19:34 abc sshd[30631]
:pam_unix(sshd:auth):
authentication failure;logname= uid=501 euid=501 tty=ssh ruser= rhost=localhost user=joe
Apr 18 06:19:34 abc sshd[30631]:
Failed password for joe from 127.0.0.1 port 5564 ssh2

$ ssh joe@localhost
joe@localhost's password:
Permission denied,try again

8. Чтобы определить самые большие структуры каталогов в каталоге /usr/share, отсортировать их от самых больших к самым маленьким и перечислить десять самых больших с помощью команды du, введите следующее:

$ du -s /usr/share/* | sort -rn | head
527800 /usr/share/locale
277108 /usr/share/fonts
196232 /usr/share/help

134984 /usr/share/backgrounds
...