---
source_image: page_535.png
page_number: 535
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.42
tokens: 7448
characters: 1869
timestamp: 2025-12-24T05:00:21.849088
finish_reason: stop
---

# service smb status
smbd (pid 28056) is running...
# chkconfig --list smb
smb        0:off  1:off  2:on   3:on   4:on   5:on   6:off

Независимо от того, используете ли вы сервер Samba в RHEL, Fedora или другой системе Linux, проверить доступ к нему можно с помощью команды smbclient (из клиентского пакета samba). Основную информацию с сервера Samba можно получить с помощью следующей команды:

# smbclient -L localhost
Enter SAMBA\root's password: <ENTER>
Anonymous login successful

    Sharename    Type    Comment
    ----------   ----    --------
    print$       Disk    Printer Drivers
    IPC$         IPC     IPC Service
    (Samba Server Version 4.10.10)
    deskjet      Printer deskjet
Reconnecting with SMB1 for workgroup listing.
Anonymous login successful
    Server           Comment
    ----------       --------
    Workgroup        Master
    ----------       ---------

Вывод команды smbclient позволяет увидеть, какие службы доступны с сервера. По умолчанию анонимный вход разрешен при запросе сервера (поэтому я просто нажал клавишу Enter, когда было предложено ввести пароль). Из этого вывода по умолчанию вы можете узнать о настройке сервера Samba следующее.

● Все принтеры, совместно используемые через сервер CUPS в вашей системе Linux, доступны также с сервера Samba, работающего в этой системе.
● Никакие каталоги сервера еще не являются общими.
● Служба имен NetBIOS еще не запущена с сервера Samba.

После этого вы можете решить, хотите ли запустить службу имен NetBIOS на своем сервере Samba.

Запуск сервера имен NetBIOS (nmbd)

Если в сети не работает сервер домена Windows, как в данном случае, можете запустить службу nmb на хосте Samba, чтобы подключить ее. Чтобы запустить службу nmb (демон nmbd) в Fedora или RHEL 7, введите следующее:

# systemctl enable nmb.service
# systemctl start nmb.service
# systemctl status nmb.service