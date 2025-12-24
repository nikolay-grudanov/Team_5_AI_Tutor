---
source_image: page_712.png
page_number: 712
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.67
tokens: 7347
characters: 1566
timestamp: 2025-12-24T05:05:05.950727
finish_reason: stop
---

Установка режима SELinux

Чтобы определить режим SELinux в своей системе, используйте команду getenforce. Чтобы увидеть как текущий режим, так и режим, заданный в файле конфигурации, примените команду sestatus. Обе команды показаны в следующем примере:

# getenforce
Enforcing
# sestatus
SELinux status: enabled
SELinuxfs mount: /sys/fs/selinux
SELinux root directory: /etc/selinux
Loaded policy name: targeted
Current mode: enforcing
Mode from config file: enforcing
Policy MLS status: enabled
Policy deny_unknown status: allowed
Memory protection checking: actual (secure)
Max kernel policy version: 31

Чтобы изменить настройку режима, используйте команду setenforce newsetting, где newsetting — это один из вариантов:

• enforcing или 1;
• permissive или 0.

Обратите внимание на то, что вы не можете применить команду setenforce для перевода SELinux в отключенный режим.

В следующем примере показано, что с помощью команды setenforce режим SELinux немедленно изменяется на разрешительный. Команда sestatus показывает текущий режим работы и режим в файле конфигурации, который не был изменен. Когда система перезагружается, она определяет режим работы SELinux из файла конфигурации. Таким образом, разрешительный режим, установленный в следующем примере, временный, поскольку в файле конфигурации установлен принудительный режим:

# setenforce 0
# getenforce
Permissive
# sestatus
SELinux status: enabled
SELinuxfs mount: /sys/fs/selinux
SELinux root directory: /etc/selinux
Loaded policy name: targeted
Current mode: permissive
Mode from config file: enforcing