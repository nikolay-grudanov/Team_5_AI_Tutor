---
source_image: page_885.png
page_number: 885
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.46
tokens: 7431
characters: 1599
timestamp: 2025-12-24T05:09:59.105299
finish_reason: stop
---

8. Чтобы создать группу томов abc из раздела LVM, создайте логический том объемом 200 Мбайт из группы data, на нем — файловую систему VFAT, временно смонтируйте логический том в новом каталоге /mnt/test, а затем убедитесь, что он был успешно смонтирован:

# pvcreate /dev/sdb3
# vgcreate abc /dev/sdb3
# lvcreate -n data -L 200M abc
# mkfs -t vfat /dev/mapper/abc-data
# mkdir /mnt/test
# mount /dev/mapper/abc-data /mnt/test

9. Чтобы увеличить объем логического тома с 200 до 300 Мбайт, введите следующее:

# lvextend -L +100M /dev/mapper/abc-data
# resize2fs -p /dev/mapper/abc-data

10. Чтобы безопасно извлечь USB-накопитель из компьютера, выполните следующее:

# umount /dev/sdb1
# swapoff /dev/sdb2
# umount /mnt/test
# lvremove /dev/mapper/abc-data
# vgremove abc
# pvremove /dev/sdb3

Теперь можете безопасно извлечь USB-накопитель из компьютера.

Глава 13. Администрирование серверов

1. Чтобы войти в любую учетную запись на другом компьютере с помощью команды ssh, введите приведенную далее команду и пароль при появлении запроса:

$ ssh joe@localhost
joe@localhost's password:
**********
[joe]$

2. Чтобы отобразить содержимое удаленного файла /etc/system-release в локальной системе с помощью команды ssh, выполните следующее:

$ ssh joe@localhost "cat /etc/system-release"
joe@localhost's password: ********
Fedora release 30 (Thirty)

3. Чтобы использовать переадресацию X11 для отображения окна gedit в локальной системе, а затем сохранить файл в удаленном домашнем каталоге, выполните следующие действия:

$ ssh -X joe@localhost "gedit newfile"
joe@localhost's password: **********