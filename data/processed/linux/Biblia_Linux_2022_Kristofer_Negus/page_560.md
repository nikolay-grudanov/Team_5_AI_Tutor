---
source_image: page_560.png
page_number: 560
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.56
tokens: 7552
characters: 2126
timestamp: 2025-12-24T05:01:06.987331
finish_reason: stop
---

Запуск службы NFS

Запуск сервера NFS включает в себя запуск нескольких демонов. Базовая служба NFS в системах Fedora и RHEL 8 называется nfs-server. Чтобы запустить эту службу, включите ее (чтобы она запускалась каждый раз при загрузке системы) и проверьте состояние, выполнив следующие три команды:

# systemctl start nfs-server.service
# systemctl enable nfs-server.service
# systemctl status nfs-server.service
• nfs-server.service – NFS server and services
    Loaded: loaded (/lib/systemd/system/nfs-server.service; enabled
        vendor preset: disabled)
    Active: active (exited) since Mon 2019-9-02 15:15:11 EDT; 24s ago
    Main PID: 7767 (code=exited, status=0/SUCCESS)
    Tasks: 0 (limit: 12244)
    Memory: 0B
    CGroup: /system.slice/nfs-server.service

Из состояния строки видно, что служба nfs-server включена и активна. Служба NFS требует также, чтобы служба RPC была запущена (rpcbind). Служба nfs-server автоматически запускает службу rpcbind, если это еще не было сделано.

В системе Red Hat Enterprise Linux 6 для проверки, запуска и включения службы NFS (nfs) понадобятся команды service и chkconfig. Следующие команды показывают, что в данный момент служба nfs не работает и отключена:

# service nfs status
rpc.svcgssd is stopped
rpc.mountd is stopped
nfsd is stopped
# chkconfig --list nfs
nfs 0:off  1:off  2:off  3:off  4:off  5:off  6:off

Как упоминалось ранее, для работы NFS должна быть запущена служба rpcbind. В системе RHEL 6 можно использовать следующие команды для запуска и постоянного включения служб rpcbind и nfs:

# service rpcbind start
Starting rpcbind:                [ OK ]
# service nfs start
Starting NFS services:            [ OK ]
Starting NFS quotas:              [ OK ]
Starting NFS daemon:              [ OK ]
Starting NFS mountd:              [ OK ]
# chkconfig rpcbind on
# chkconfig nfs on

Команды (mount, exportfs и т. д.) и файлы (/etc/exports, /etc/fstab и т. д.) настройки службы в основном одинаковы для всех систем Linux. Итак, после того, как вы установили и запустили NFS, просто следуйте инструкциям, приводимым в этой главе, чтобы начать применять службу.