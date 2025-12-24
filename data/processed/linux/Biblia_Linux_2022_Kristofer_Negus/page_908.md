---
source_image: page_908.png
page_number: 908
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.09
tokens: 7419
characters: 1588
timestamp: 2025-12-24T05:10:33.431690
finish_reason: stop
---

10. Чтобы просмотреть задействование памяти и подкачки из веб-интерфейса Cockpit, откройте в браузере Cockpit (https://hostname:9090). Выберите System ▸ Memory & Swap (Система ▸ Память и обмен).

Глава 22. Базовые методы обеспечения безопасности

1. Чтобы проверить сообщения из журнала systemd для служб NetworkManager.service, sshd.service и auditd.service, введите следующее:

# journalctl -u NetworkManager.service
...
# journalctl -u sshd.service
...
# journalctl -u auditd.service
...

2. Пароли пользователей хранятся в файле /etc/shadow. Чтобы увидеть его права, введите команду ls-l /etc/shadow в командной строке. (Если файла не существует, необходимо запустить команду pwconv.)
Далее приведены соответствующие настройки:

# ls -l /etc/shadow
----------. 1 root root 1049 Feb 10 09:45 /etc/shadow

3. Чтобы определить срок действия пароля вашей учетной записи с помощью одной команды, введите chage -l user_name, например:

# chage -l chris

4. Чтобы начать аудит событий в файле /etc/shadow с помощью демона auditd, введите в командной строке следующее:

# auditctl -w /etc/shadow -p w

5. Чтобы проверить настройки аудита, введите auditctl -l в командной строке. Чтобы создать отчет из демона auditd в файле /etc/shadow, введите ausearch -f /etc/shadow в командной строке. Чтобы отключить аудит этого файла, введите auditctl -W /etc/shadow -p w.

6. Чтобы установить пакет lemon, повредите файл /usr/bin/lemon и удалите пакет lemon, введя следующую команду:

# yum install -y lemon
# cp /etc/services /usr/bin/lemon
# rpm -V lemon
S.5....T.    /usr/bin/lemon
# yum erase lemon