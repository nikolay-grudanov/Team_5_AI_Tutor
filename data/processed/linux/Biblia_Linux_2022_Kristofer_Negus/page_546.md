---
source_image: page_546.png
page_number: 546
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.32
tokens: 7470
characters: 2093
timestamp: 2025-12-24T05:00:43.469953
finish_reason: stop
---

Добывление папки общего доступа на сервер

Если каталог /var/salesdata создан и правильно настроен для совместного использования Samba, то вот как может выглядеть общая папка (называемая salesdata) в файле smb.conf:

[salesdata]
    comment = Sales data for current year
    path = /var/salesdata
    read only = no
    browseable = yes
    valid users = chris

Перед формированием общего ресурса был создан каталог /var/salesdata с пользователем chris, назначенным в качестве пользователя и группы, и каталог был настроен на чтение и запись для него. (Контекст файла SELinux также должен быть установлен, если SELinux находится в принудительном режиме.) Имя пользователя Samba chris должно быть представлено вместе с паролем для доступа к общему ресурсу. После того как пользователь chris подключен к общему ресурсу, он может его читать и записывать в нем (read only = no).

Теперь, когда вы ознакомились с настройками Samba по умолчанию и настройками простого общего каталога (папки), изучите следующие несколько разделов, чтобы узнать, как еще настроить общие ресурсы. В частности, в примерах показано, как сделать общие ресурсы доступными для конкретных пользователей, хостов и сетевых интерфейсов.

Проверка общего доступа на сервере

Чтобы изменения в конфигурации Samba вступили в силу, необходимо перезапустить службу smb. После этого убедитесь, что созданный вами общий ресурс Samba открыт и любой пользователь, назначенный этому ресурсу, может получить к нему доступ. Чтобы сделать это, введите от имени суперпользователя из оболочки на сервере Samba следующие команды:

# systemctl restart smb.service
# smbclient -L localhost -U chris
Enter SAMBA\chris's password: ********
    Sharename        Type        Comment
    ----------       ----        --------
    salesdata        Disk        Sales data for current year
    print$           Disk        Printer Drivers
    IPC$             IPC         IPC Service (Samba 4.10.4)
    chris            Disk        Home Directories
Reconnecting with SMB1 for workgroup listing.
    Server           Comment
    ----------       --------