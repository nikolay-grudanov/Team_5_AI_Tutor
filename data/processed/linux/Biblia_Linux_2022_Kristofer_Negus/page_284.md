---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.76
tokens: 7492
characters: 1917
timestamp: 2025-12-24T04:53:09.580955
finish_reason: stop
---

В примере подкоманда groupinstall установила 101 новый пакет и обновила пять установленных. Чтобы удалить всю группу сразу, задействуйте подкоманду groupremove:

# yum groupremove LXDE

Базы данных и кэш пакетов RPM

Несколько подкоманд yum помогают выполнять задачи обслуживания, например проверку наличия проблем с базой данных RPM или очистку кэша. В YUM есть инструменты для обслуживания пакетов RPM и обеспечения эффективности и безопасности ПО системы.

Время от времени необходимо очищать кэш. Если сохранить загруженные пакеты после их установки (по умолчанию они удаляются благодаря параметру keepcache=0 файла /etc/yum.conf), то каталоги с кэшем (в каталоге /var/cache/yum) могут заполниться. Метаданные, хранящиеся в каталогах кэша, можно очистить, что вызовет загрузку свежих метаданных из всех подключенных репозиториев YUM при следующем запуске yum. Варианты очистки кэша:

# yum clean packages
14 files removed
# yum clean metadata
Cache was expired
16 files removed
# yum clean all
68 files removed

Вполне возможно, хотя и маловероятно, что база данных RPM окажется повреждена. Это может случиться, если во время установки пакета произойдет что-то неожиданное, например внезапное отключение системы. Вы можете проверить базу данных RPM на наличие ошибок (yum check) или просто перестроить ее файлы. Пример поврежденной базы данных RPM и команда rpm, которая используется для ее исправления:

# yum check
error: db5 error(11) from dbenv->open: Resource temporarily unavailable
error: cannot open Packages index using db5-Resource temporarily unavailable(11)
error: cannot open Packages database in /var/lib/rpm
Error: Error: rpmbd open failed
# rpm --rebuilddb
# yum check

Здесь команда yum clean удаляет кэшированные данные из подкаталогов /var/cache/yum. Команда rpm --rebuilddb перестраивает базу данных. Команда yum check проверяет наличие проблем с локальным кэшем RPM и базой данных, но обрати-