---
source_image: page_241.png
page_number: 241
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.47
tokens: 6426
characters: 1507
timestamp: 2025-12-24T04:01:31.195547
finish_reason: stop
---

Удаленный сервер своими руками

ecryptfs_sig=bd28c38da9fc938b
WARNING: Based on the contents of [/root/.ecryptfs/sig-cache.txt],
it looks like you have never mounted with this key before. This could mean that you have typed your passphrase wrong.
Would you like to proceed with the mount (yes/no)? : yes
Would you like to append sig [bd28c38da9fc938b] to [/root/.ecryptfs/sig-cache.txt]
in order to avoid this warning in the future (yes/no)? : yes
Successfully appended new sig to user sig cache file
Mounted eCryptfs

Теперь разберемся, что произошло. Мы согласились на использование алгоритма по умолчанию (AES). Если считаете, что другой алгоритм лучше, можете выбрать его. Также мы отказались от шифрования имен файлов (Enable filename encryption): если что-то случится с зашифрованным каталогом, то разобраться, где и какой файл, будет сложно.

На данный момент /opt/data зашифрован. Осталось самое главное — проверить, а зашифрован ли на самом деле каталог? Попробуем скопировать в него любой файл из незашифрованной файловой системы:

cp /etc/motd /optta

Размонтируем зашифрованный каталог:

sudo umount /opt/data

Теперь пробуем прочитать /opt/data/motd:

cat /opt/data/motd

Если вы увидите всякого рода иероглифы и абракадабру, значит, шифрование работает.

14.5. Настройка VPN-сервера

Представим, что у нас есть торговая организация, представители которой «рассекают» по всей стране. Им часто приходится пользоваться публичными Wi-Fi сетями (например, в ресторанах и отелях) для передачи данных