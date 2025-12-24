---
source_image: page_240.png
page_number: 240
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.29
tokens: 6417
characters: 1296
timestamp: 2025-12-24T04:01:29.318788
finish_reason: stop
---

14.4. Шифрование данных

В этом разделе мы поговорим о криптографической файловой системе eCryptfs и зашифруем каталог с данными (/opt/data).

Первым делом нужно установить утилиты eCryptfs. На данный момент у меня Debian, поэтому для их установки буду использовать apt-get:

sudo apt install ecryptfs-utils

Чтобы зашифровать каталог, нужно его подмонтировать, указав тип файловой системы ecryptfs:

sudo mount -t ecryptfs /opt/data /opt/data

Вывод будет таким (жирным выделено то, что нужно ввести вам):

Passphrase: <секретная фраза>
Select cipher:
1) aes: blocksize = 16; min keysize = 16; max keysize = 32 (not loaded)
2) blowfish: blocksize = 16; min keysize = 16; max keysize = 56 (not loaded)
3) des3_ede: blocksize = 8; min keysize = 24; max keysize = 24 (not loaded)
4) twofish: blocksize = 16; min keysize = 16; max keysize = 32 (not loaded)
5) cast6: blocksize = 16; min keysize = 16; max keysize = 32 (not loaded)
6) cast5: blocksize = 8; min keysize = 5; max keysize = 16 (not loaded)
Selection [aes]: просто нажмите Enter
Select key bytes:
1) 16
2) 32
3) 24
Selection [16]: нажмите Enter
Enable plaintext passthrough (y/n) [n]: n
Enable filename encryption (y/n) [n]: n
Attempting to mount with the following options:
ecryptfs_unlink_sigs
ecryptfs_key_bytes=16
ecryptfs_cipher=aes