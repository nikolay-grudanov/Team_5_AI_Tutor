---
source_image: page_901.png
page_number: 901
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.87
tokens: 7381
characters: 1649
timestamp: 2025-12-24T05:10:26.240820
finish_reason: stop
---

Глава 19. Настойка Samba-сервера

1. Чтобы установить пакеты samba и samba-client, введите из локальной системы от имени суперпользователя следующую команду:

# yum install samba samba-client

2. Чтобы запустить и включить службы smb и nmb, введите от имени суперпользователя из локальной системы следующие команды:

# systemctl enable smb.service
# systemctl start smb.service
# systemctl enable nmb.service
# systemctl start nmb.service

ИЛИ

# chkconfig smb on
# service smb start
# chkconfig nmb on
# service nmb start

3. Чтобы установить рабочую группу сервера Samba в TESTGROUP, имя NetBIOS — в MYTEST и строку сервера — в Samba Test System, от имени суперпользователя откройте файл /etc/samba/smb.conf в текстовом редакторе и измените три строки так, чтобы они выглядели следующим образом:

workgroup = TESTGROUP
netbios name = MYTEST
server string = Samba Test System

4. Чтобы добавить в свою систему пользователя Linux с именем phil и присвоить ему пароль Linux и пароль Samba, от имени суперпользователя из оболочки введите следующее:

# useradd phil
# passwd phil
New password: ********
Retype new password: ********
# smbpasswd -a phil
New SMB password: ********
Retype new SMB password: ********
Added user phil.

Обязательно запомните установленные пароли.

5. Настройте раздел [homes] таким образом, чтобы можно было просматривать домашние каталоги (yes) и записывать в них (yes) и пользователь phil являлся единственным допустимым пользователем. Откройте файл /etc/samba/smb.conf как суперпользователь и измените раздел [homes]:

[homes]
    comment = Home Directories
    browseable = Yes
    read only = No
    valid users = phil