---
source_image: page_481.png
page_number: 481
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.06
tokens: 7526
characters: 1875
timestamp: 2025-12-24T04:58:57.250184
finish_reason: stop
---

Пакет httpd

Чтобы изучить пакет httpd в системах Fedora или RHEL перед установкой, загрузите его с помощью команды yumdownloader и выполните несколько команд rpm для просмотра содержимого пакета:

# yumdownloader httpd
# rpm -qpi httpd-*rpm
Name        : httpd
Version     : 2.4.41
Release     : 1.fc30
Architecture: x86_64
Install Date: (not installed)
Group       : Unspecified
Size        : 5070831
License     : ASL 2.0
Signature   : RSA/SHA256, Mon 19 Aug 2019 06:06:09 AM EDT, Key ID ef3c111fcfc659b9
Source RPM  : httpd-2.4.41-1.fc30.src.rpm
Build Date  : Thu 15 Aug 2019 06:07:29 PM EDT
Build Host  : buildvm-30.phx2.fedoraproject.org
Relocations : (not relocatable)
Packager    : Fedora Project
Vendor      : Fedora Project
URL         : http://httpd.apache.org/
Bug URL     : https://bugz.fedoraproject.org/httpd
Summary     : Apache HTTP Server
Description :
The Apache HTTP Server is a powerful, efficient, and extensible web server.

Команда yumdownloader загружает последнюю версию пакета httpd в текущий каталог. Команда rpm -qpi запрашивает информацию из только что загруженного пакета httpd RPM. В примере видно, что пакет был создан проектом Fedora и это действительно пакет HTTP-сервера Apache. Затем загляните внутрь пакета, чтобы увидеть следующие файлы конфигурации:

# rpm -qpc httpd-*rpm
/etc/httpd/conf.d/autoindex.conf
/etc/httpd/conf.d/userdir.conf
/etc/httpd/conf.d/welcome.conf
/etc/httpd/conf.modules.d/00-base.conf
/etc/httpd/conf.modules.d/00-dav.conf
...
/etc/httpd/conf/httpd.conf
/etc/httpd/conf/magic
/etc/logrotate.d/httpd
/etc/sysconfig/htcacheclean

Основной файл конфигурации Apache — это /etc/httpd/conf/httpd.conf. Файл welcome.conf определяет домашнюю страницу по умолчанию, пока не будет добавлено другое содержимое. Файл Magic создает правила, которые сервер может использовать для определения типа файла при попытке его открыть.