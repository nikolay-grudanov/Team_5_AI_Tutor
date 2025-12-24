---
source_image: page_280.png
page_number: 280
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.51
tokens: 7362
characters: 1460
timestamp: 2025-12-24T04:39:55.065579
finish_reason: stop
---

В листинге 6.31 иллюстрируется использование утилиты nmblookup(1), предназначенной для диагностики службы NBNS, при помощи которой «плоское» имя NetBIOS WINXP отображается на соответствующий ему IP-адрес. Именно при помощи службы NBNS и широковещательного поиска специальных «групповых» имен NetBIOS реализуется основной способ обнаружения CIFS-серверов локальной сети, что выполняет утилита smbtree(1), иллюстрируемая ① в листинге 6.32.

В редких отдельных случаях серверы CIFS обнаружаются ② зарегистрированными в службе mDNS/DNS-SD, что характерно (как и в случае серверов NFS) для сетевых устройств хранения данных W:[NAS] или сетевых видеорегистраторов W:[NVR].

Листинг 6.32. Обнаружение CIFS-серверов

① lumpy@ubuntu:~$ smbtree -N
WORKGROUP
  \\WINXP
    \\WINXP\C$
      Стандартный общий ресурс
    \\WINXP\ADMIN$
      Удаленный Admin
    \\WINXP\media
      Фото, видео, и т. д.
    \\WINXP\D$
      Стандартный общий ресурс
    \\WINXP\IPC$
      Удаленный IPC
  \\NVR
    \\NVR\recordings
    \\NVR\multimedia
    \\NVR\download
    \\NVR\IPC$

② lumpy@ubuntu:~$ avahi-browse -rcl _smb._tcp
+ eth0 IPv4 NVR(SMB)
= eth0 IPv4 NVR(SMB)
hostname = [NVR.local]
address = [192.168.17.90]
port = [445]
txt = []

CIFS-клиенты

Различают две разные реализации клиента CIFS — внеядерную smbclient(1) (аналогичную «интерактивным» FTP-клиентам) и ядерную (аналогичную NFS-клиенту), реализуемую модулем ядра ctfs. Использование ядерного модуля позволяет монти-