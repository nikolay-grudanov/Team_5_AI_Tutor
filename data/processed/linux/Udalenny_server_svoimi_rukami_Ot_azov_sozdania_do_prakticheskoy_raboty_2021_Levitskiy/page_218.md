---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.57
tokens: 6406
characters: 1504
timestamp: 2025-12-24T04:00:56.469451
finish_reason: stop
---

# Сбрасываем буферы на диск (не обязательно)
sync
# Размонтируем файловую систему
umount /mnt/backup

Наш сценарий готов полностью. Осталось только настроить SSH-сервер на аутентификацию без пароля. Для этого на клиенте (то есть на нашем сервере, резервное копирование которого вы будете производить, далее SSH-клиент) введите команду:

# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.

Эта команда создает пару приватного/публичного ключей. Обратите внимание, что когда программа попросит вас ввести ключевую фразу, вводить ничего не нужно - вы же не хотите вводить пароль?

Теперь на SSH-сервере (на компьютере, на который вы будете отправлять резервные копии) откройте файл конфигурации sshd. Обычно это /etc/ssh/sshd_config. Добавьте в него строки:

RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile %h/.ssh/authorized_keys

Обычно они в нем уже есть, но их нужно раскомментировать. Строка «%h/.ssh/authorized_keys» означает, что ключи будут храниться в домашнем каталоге пользователя (%h), подкаталог .ssh, файл authorized_keys. Если вы этого файла там нет, вы можете его создать самостоятельно.

Скопируем наш файл публичный ключ на SSH-сервер (команду вводим на SSH-клиенте):

scp /root/.ssh/id_rsa.pub root@example.com:/root/