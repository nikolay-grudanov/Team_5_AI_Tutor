---
source_image: page_911.png
page_number: 911
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.16
tokens: 7498
characters: 1949
timestamp: 2025-12-24T05:10:40.930748
finish_reason: stop
---

Чтобы перечислить различные модули PAM в системе Ubuntu, введите:

# find / -name pam*.so

9. Чтобы найти в своей системе файл конфигурации PAM other, введите ls /etc/pam.d/other в командной строке. Файл конфигурации other применяет запрет Implicit Deny и должен выглядеть примерно так:

$ cat /etc/pam.d/other
#%PAM-1.0
auth    required      pam_deny.so
account required      pam_deny.so
password required     pam_deny.so
session  required     pam_deny.so

10. Чтобы найти файл конфигурации ограничений PAM, введите следующее:

$ ls /etc/security/limits.conf

Чтобы вывести содержимое файла на экран, введите:

$ cat /etc/security/limits.conf

В этом файле настройки для предотвращения работы вредоносной программы (fork-бомбы) выглядят следующим образом:

@student    hard    nproc    50
@student    -       maxlogins    4

Глава 24. Повышенная безопасность с технологией SELinux

1. Чтобы перевести систему в разрешительный режим для SELinux, введите setenforce permissive в командной строке. Также можно ввести команду setenforce 0.
2. Соблюдайте осторожность при переводе системы SELinux в принудительный режим без изменения основного файла конфигурации SELinux. Лучше всего не запускать эту команду в системе для выполнения упражнения, пока не начнете использовать SELinux. Введите команду setenforce enforcing в командной строке. Можно также ввести команду setenforce 1.
3. Чтобы найти и просмотреть постоянную политику SELinux (задается во время загрузки), перейдите в основной файл конфигурации SELinux — /etc/selinux/config. Чтобы просмотреть его, введите cat/etc/selinux | config / grep SELINUX= в командной строке. Чтобы узнать, как он установлен в данный момент, введите команду getenforce.
4. Чтобы перечислить контекст безопасности файла /etc/hosts и определить различные атрибуты контекста безопасности, введите ls -Z /etc/hosts в командной строке:

$ ls -Z /etc/hosts
-rw-r--r--. root root system_u:object_r:net_conf_t:s0 /etc/hosts