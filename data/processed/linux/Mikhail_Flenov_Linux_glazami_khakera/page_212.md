---
source_image: page_212.png
page_number: 212
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.30
tokens: 7701
characters: 1223
timestamp: 2025-12-24T04:24:45.230818
finish_reason: stop
---

В стиле Samba

; password server = <NT-Server-Name>
; password level = 8
; username level = 8
encrypt passwords = yes
smb passwd file = /etc/samba/smbpasswd
; usershare max shares = 100

unix password sync = Yes
passwd program = /usr/bin/passwd %u
passwd chat = *New*password* %n\n *Retype*new*password* %n\n*passwd:*all*authentication*tokens*updated*successfully*
pam password change = yes
; username map = /etc/samba/smbusers

; include = /etc/samba/smb.conf.%m
obey pam restrictions = yes

# Настройка сокета
socket options = TCP_NODELAY SO_RCVBUF=8192 SO_SNDBUF=8192
; interfaces = 192.168.12.2/24 192.168.13.2/24
; bind interfaces only = yes

# Настройка просмотра
; remote browse sync = 192.168.3.25 192.168.5.255
; remote announce = 192.168.1.255 192.168.2.44
; local master = no
; os level = 33
; domain master = yes
; preferred master = yes

# Работа с сервером
; domain logons = yes
; logon script = %m.bat
; logon script = %U.bat
; logon path = \\%L\Profiles\%U
; wins support = yes

# WINS-сервер
wins support = no
wins server = w.x.y.z
dns proxy = no
name resolve order = lmhosts host wins bcast

# Отображение файлов
; preserve case = no
; short preserve case = no
; default case = lower
; case sensitive = no