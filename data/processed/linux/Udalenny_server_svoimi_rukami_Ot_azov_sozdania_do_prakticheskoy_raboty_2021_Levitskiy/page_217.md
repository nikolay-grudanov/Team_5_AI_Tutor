---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.67
tokens: 6331
characters: 1044
timestamp: 2025-12-24T04:00:53.577789
finish_reason: stop
---

Удаленный сервер своими руками

tar -czf /mnt/backup/mail/$dn.tar.gz $dn
# Если нужно, раскомментируйте строку
# scp $dn.tar.gz user@example.com:/backups/mail
done
Теперь интегрируем наши два сценария в один общий (листинг 13.1)

Листинг 13.1. Сценарий /bin/backup

#!/bin/bash

mount /dev/sdc1 /mnt/backup

# Рекурсивное удаление всего из /mnt/backup
rm -r /mnt/backup/*
# Создаем каталог для хранения базы данных
mkdir /mnt/backup/db
# Каталог для почтовых ящиков
mkdir /mnt/backup/mail

cd /home

# Копируем домашние каталоги
for dn in `ls /home`; do
    echo "Creating backup for $dn"
    tar -czf /mnt/backup/$dn.tar.gz $dn
done

# Копируем базы данных
echo "Database backup..."
cd /var/lib/mysql
for dn in `ls /var/lib/mysql`; do
    test -d && "$dn" && tar -czf /mnt/backup/db/$dn.tar.gz $dn
done

cd /var/mail

for dn in `ls /var/mail`; do
    echo "Creating backup for $dn [mail]"
    tar -czf /mnt/backup/mail/$dn.tar.gz $dn
done

# Если нужно хранить резервные копии на удаленной машине
# scp -r /mnt/backup user@example.com:/backups