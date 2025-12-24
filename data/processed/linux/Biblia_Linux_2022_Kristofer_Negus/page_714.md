---
source_image: page_714.png
page_number: 714
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.05
tokens: 7407
characters: 1758
timestamp: 2025-12-24T05:05:18.469600
finish_reason: stop
---

Установка типа политики SELinux

Выбранный тип политики определяет, будет ли SELinux применять базовую политику или политики TE, MLS. Тип непосредственно определяет наборы правил политики, используемых для настройки того, к чему может получить доступ объект.

По умолчанию для типа политики задано значение targeted. Чтобы изменить тип политики по умолчанию, отредактируйте файл /etc/selinux/config. Замените строку SELINUXTYPE= одной из следующих:

● SELINUX=targeted;
● SELINUX=mls;
● SELINUX=minimum.

Если вы установили тип SELinux в mls или minimum, вначале убедитесь, что установлен подходящий пакет политики. Проверьте это, введя следующую команду:
yum list selinux-policy-mls or yum list selinux-policy-minimum

ПРИМЕЧАНИЕ
Чтобы проверить пакеты политики SELinux в дистрибутиве Ubuntu, задействуйте команду sudo apt-cache policy package_name.

Приведенный далее пример файла конфигурации SELinux показывает, что тип был установлен в mls. Теперь, когда происходит перезагрузка системы, тип политики изменяется:

# cat /etc/selinux/config
# This file controls the state of SELinux on the system.
...
# SELINUXTYPE= type of policy in use. Possible values are:
#
# targeted - Targeted processes are protected,
# minimum - Modification of targeted policy.
#           Only selected processes are protected.
# mls - Multi Level Security protection.
SELINUXTYPE=mls

Управление контекстами безопасности SELinux

Контекст безопасности SELinux позволяет системе применять правила политики для доступа субъектов к объектам. Система Linux поставляется с уже назначенными контекстами безопасности.

Чтобы просмотреть текущие контексты безопасности файлов и процессов SELinux, используйте команду secon. В табл. 24.1 перечислены доступные параметры команды secon.