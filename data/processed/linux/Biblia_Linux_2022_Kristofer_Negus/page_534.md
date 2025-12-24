---
source_image: page_534.png
page_number: 534
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.38
tokens: 7497
characters: 1853
timestamp: 2025-12-24T05:00:20.499277
finish_reason: stop
---

Active: active (running) since Fri 2020-01-31 07:23:37 EDT; 6s ago
    Docs: man:smbd(8)
          man:samba(7)
          man:smb.conf(5)
    Status: "smbd: ready to serve connections..."
    Tasks: 4 (limit: 12216)
    Memory: 20.7M
    Main PID: 4838 (smbd)
CGroup: /system.slice/smb.service
├─4838 /usr/sbin/smbd --foreground --no-process-group
└─4840 /usr/sbin/smbd --foreground --no-process-group

Первая команда systemctl включает службу, вторая сразу же запускает ее, а третья отображает состояние. Обратите внимание на то, что файл службы располагается по адресу /usr/lib/systemd/system/smb.service. Посмотрите на содержимое этого файла:

# cat /usr/lib/systemd/system/smb.service
[Unit]
Description=Samba SMB Daemon
Documentation=man:smbd(8) man:samba(7) man:smb.conf(5)
Wants=network-online.target
After=network.target network-online.target nmb.service winbind.service
[Service]
Type=notify
NotifyAccess=all
PIDFile=/run/smbd.pid
LimitNOFILE=16384
EnvironmentFile=-/etc/sysconfig/samba
ExecStart=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS
ExecReload=/bin/kill -HUP $MAINPID
LimitCORE=infinity
Environment=KRB5CCNAME=FILE:/run/samba/krb5cc_samba
[Install]
WantedBy=multi-user.target

Процесс демона Samba (smbd) запускается после целевых network, network-online, nmb и winbind. Файл /etc/sysconfig/samba содержит переменные, которые передаются в качестве аргументов демонам smbd, nmbd и winbindd при их запуске. Ни для одного из этих демонов по умолчанию не задано никаких параметров. Строка WantedBy указывает, что служба smb.service должна запускаться при загрузке системы в многопользовательский режим (многопользовательская цель), что происходит по умолчанию.

В RHEL 6 и более ранних версиях системы сервер Samba можно запустить следующим образом:

# service smb start
Starting SMB services:      [ OK ]
# chkconfig smb on