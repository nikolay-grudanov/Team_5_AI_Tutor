---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.87
tokens: 6312
characters: 1062
timestamp: 2025-12-24T03:59:14.487850
finish_reason: stop
---

Удаленный сервер своими руками

PubkeyAuthentication yes
#AuthorizedKeysFile %h/.ssh/authorized_keys

# Отключаем устаревшую .rhosts-аутентификацию
# Файлы ~/.rhosts and ~/.shosts читаться не будут:
IgnoreRhosts yes
RhostsRSAAuthentication no
HostbasedAuthentication no

# Запрещаем (значение no) пустые пароли
PermitEmptyPasswords no

# Не используем аутентификацию вызов-ответ
ChallengeResponseAuthentication no

# Параметры Kerberos
#KerberosAuthentication no
#KerberosGetAFSToken no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes

# Параметры GSSAPI
#GSSAPIAuthentication no
#GSSAPICleanupCredentials yes

# X11-форвардинг
X11Forwarding yes
X11DisplayOffset 10
# Выводить сообщение дня (можете отключить)
PrintMotd yes
# Выводить время последнего входа
PrintLastLog yes
# Использовать постоянные TCP-соединения
TCPKeepAlive yes
#UseLogin no

#MaxStartups 10:30:60
# Баннер
#Banner /etc/issue.net

# Разрешать клиенту передавать локальные переменные окружения
AcceptEnv LANG LC_*

# Параметры подсистемы sftp
Subsystem sftp /usr/lib/openssh/sftp-server