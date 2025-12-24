---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.70
tokens: 7914
characters: 2219
timestamp: 2025-12-24T04:23:44.808174
finish_reason: stop
---

Строка состоит из двух параметров, разделенных двоеточием. Первым указывается имя сервиса (или список, разделенный запятыми), доступ к которому нужно ограничить. Второй — это адреса (для файла /etc/hosts.allow — разрешенные, а для /etc/hosts.deny — запрещенные), разделенные запятыми. В качестве параметров можно использовать ключевое слово ALL, которое соответствует любому адресу или сервису.

Рассмотрим пример конфигурирования файла. Для начала закроем любой доступ. Для этого в файле /etc/hosts.deny нужно прописать запрет для всех пользователей на любые сервисы. Для этого добавляем строку ALL: ALL. В результате ваш файл будет выглядеть следующим образом:

# hosts.deny    This file describes the names of the hosts which are
#                *not* allowed to use the local INET services, as decided
#                by the '/usr/sbin/tcpd' server.
#
# The portmap line is redundant, but it is left to remind you that
# the new secure portmap uses hosts.deny and hosts.allow. In particular
# you should know that NFS uses portmap!

ALL: ALL

Теперь в файле hosts.allow санкционируем только следующий доступ:
- компьютеру с адресом 192.168.1.1 разрешено подключение ко всем сервисам;
- с ftpd-сервисом могут работать только компьютеры с адресами 192.168.1.2 и 192.168.1.3.

# hosts.allow    This file describes the names of the hosts
#                which are allowed to use the local INET services,
#                as decided by the '/usr/sbin/tcpd' server.
#

ALL: 192.168.1.1
ftpd: 192.168.1.2, 192.168.1.3

Если вам нужно целой сети позволить доступ к какому-либо сервису, то можно указать неполный адрес:

ftpd: 192.168.1.

Эта строка разрешает доступ к ftpd-сервису всем компьютерам сети 192.168.1.x (последнее число адреса не указано, значит, оно может быть любым).

Как видите, использовать файлы /etc/hosts.allow и /etc/hosts.deny намного проще, потому что не требуется прописывать правила для входящих и исходящих пакетов. Но возможности этих файлов слишком ограничены, и любой сетевой экран позволяет осуществлять куда более тонкие настройки.

Я рекомендую использовать файлы /etc/hosts.allow и /etc/hosts.deny для решения временных проблем безопасности. Если в каком-либо сервисе найдена уязвимость,