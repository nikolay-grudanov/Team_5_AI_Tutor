---
source_image: page_141.png
page_number: 141
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.52
tokens: 7564
characters: 2193
timestamp: 2025-12-24T04:35:51.517202
finish_reason: stop
---

«суперпользователя», лишенного большинства своих привилегий, т. к. ему их умышленно уменьшили при его запуске (см. systemd(1) в главе 8) до минимально необходимого набора, достаточного для выполнения его функций¹.

Листинг 4.23. Привилегии (capabilities) процесса

fitz@ubuntu:~$ ps fo user,pid,cmd -C NetworkManager,postgres,apache2

USER      PID CMD
root      10129 /usr/sbin/apache2 -k start
www-data  10131 \_ /usr/sbin/apache2 -k start
www-data  10132 \_ /usr/sbin/apache2 -k start
postgres  6711 /usr/lib/postgresql/11/bin/postgres -D /var/lib/postgresql/11/main ...
postgres  6713 \_ postgres: 11/main: checkpointer
postgres  6714 \_ postgres: 11/main: background writer
postgres  6715 \_ postgres: 11/main: walwriter
postgres  6716 \_ postgres: 11/main: autovacuum launcher
postgres  6717 \_ postgres: 11/main: stats collector
postgres  6718 \_ postgres: 11/main: logical replication launcher
root      646 /usr/sbin/NetworkManager --no-daemon

fitz@ubuntu:~$ getpcaps 6711
Capabilities for `6711': =
fitz@ubuntu:~$ getpcaps 10129
Capabilities for `10129': =
cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,
cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,
cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,
cap_audit_read+ep

fitz@ubuntu:~$ getpcaps 646
Capabilities for `646': =
cap_dac_override,cap_kill,cap_setgid,cap_setuid,cap_net_bind_service,cap_net_admin,
cap_net_raw,cap_sys_module,cap_sys_chroot,cap_audit_write+ep

В листинге 4.24 показан типичный пример применения отдельных привилегий там, где классически применяется неявная передача всех полномочий суперпользователя при помощи механизма SUID/SGID. Например, «обычная» утилита ping(1) для выполнения своей работы должна создать «необработанный» raw(7) сетевой сокет, что

¹ Что способствует обеспечению защищенности операционной системы.