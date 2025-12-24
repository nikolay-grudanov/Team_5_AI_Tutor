---
source_image: page_711.png
page_number: 711
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.89
tokens: 7481
characters: 2250
timestamp: 2025-12-24T05:05:11.145916
finish_reason: stop
---

Правила политики устанавливаются вместе с SELinux и группируются в пакеты, называемые также модулями.

В системе Linux имеется пользовательская документация по различным модулям политики в виде HTML-файлов. Чтобы просмотреть эту документацию на Fedora или RHEL, откройте браузер и введите следующий URL-адрес: file:///usr/share/doc/selinux-policy/html/index.html. Для Ubuntu URL-адрес такой: file:///usr/share/doc/selinux-policy-doc/html/index.html. Если у вас нет документации по политике вашей системы, можете установить ее в Fedora или RHEL, набрав команду yum install selinux-policy-doc. В Ubuntu введите в командной строке sudo apt-get install selinux-policy-doc.

Просмотрите эту документацию, чтобы узнать, как создаются и упаковываются правила политики.

Пакеты правил политики, а также режимы работы SELinux, тип политики и различные контексты безопасности работают вместе, чтобы защитить вашу систему Linux с помощью механизма SELinux. В следующих разделах описано, как начать настройку SELinux для удовлетворения потребностей вашей организации в области безопасности.

Настройка системы SELinux

Изначально система SELinux настроена. Вы можете сразу начать использовать ее функции без каких-либо дополнительных настроек. Однако предварительно настроенные параметры редко удовлетворяют всем требованиям безопасности системы Linux.

Настройки SELinux могут быть установлены и изменены только суперпользователем. Файлы конфигурации и политики находятся в каталоге /etc/selinux. Основным файлом конфигурации является файл /etc/selinux/config, он выглядит следующим образом:

# cat /etc/selinux/config
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - SELinux is fully disabled.
SELINUX=enforcing
# SELINUXTYPE= can take one of these three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy.
#                Only selected processes are protected.
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted

Этот основной файл конфигурации SELinux позволяет установить режим и тип политики.