---
source_image: page_214.png
page_number: 214
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.70
tokens: 7549
characters: 2199
timestamp: 2025-12-24T04:51:04.802844
finish_reason: stop
---

● Служба HTTP (system-config-httpd). Настраивает компьютер под веб-сервер Apache.
● Служба NFS (system-config-nfs). Настраивает каталоги системы для совместного использования с другими компьютерами в сети.
● Служба Root Password (system-config-rootpassword). Позволяет сменить пароль суперпользователя.
● Служба Samba NFS (system-config-samba). Настраивает общий доступ к файлам Windows (SMB). Для настройки других функций Samba можно задействовать окно SWAT.

До появления RHEL 8 в системах Fedora и RHEL были доступны следующие инструменты с графическим интерфейсом.

● Службы (Services) (system-config-services). Отображение и изменение запущенных в системе Fedora служб на разных уровнях выполнения в окне Service Configuration (Настройка служб).
● Аутентификация (Authentication) (system-config-authentication). Изменение способа аутентификации пользователей в системе. Как правило, выбираются теневые пароли и пароли MD5. Однако, если ваша сеть поддерживает аутентификацию LDAP, Kerberos, SMB, NIS или Hesiod, можете выбрать любой из этих типов аутентификации.
● Дата и время (Date & Time) (system-config-date). Установка даты и времени вручную или синхронизация системного времени с сервером NTP.
● Брандмауэр (Firewall) (system-config-firewall). Настройка брандмауэра, которая разрешает или запрещает службам доступ к компьютерам из сети.
● Язык (Language) (system-config-language). Установка для системы языка по умолчанию.
● Печать (Printing) (system-config-printer). Настройка локальных и удаленных принтеров.
● Управление SELinux (SELinux Management) (system-config-selinux). Установка режимов принудительного использования SELinux и политики по умолчанию.
● Пользователи и группы (Users & Groups) (system-config-users). Добавление, отображение и изменение учетных записей пользователей и групп системы Fedora.

Другие административные утилиты собраны в меню Applications (Приложения) на верхней панели. Выберите пункт System Tools (Системные утилиты) в GNOME 2 или перейдите в меню Activities (Обзор) в GNOME 3, чтобы выбрать один из приведенных далее инструментов (если они установлены).

● Пакет Configuration Editor (gconf-editor). Позволяет редактировать базу данных настроек GNOME.