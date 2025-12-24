---
source_image: page_487.png
page_number: 487
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.78
tokens: 11634
characters: 1601
timestamp: 2025-12-24T03:36:57.527100
finish_reason: stop
---

---
primary_language: ru
is_rotation_valid: True
rotation_correction: 0
is_table: False
is_diagram: False
---
--quiet
Отображать только сообщения об ошибках.
--rcfile filename
Использовать указанный файл в качестве файла настроек, заменяющего общесистемный файл /etc/rpmrc или $HOME/.rpmrc.
--root dir
Выполнять все операции в каталоге dir.
--version
Отобразить номер версии rpm.
-vv
Отобразить отладочную информацию.

Параметры install, upgrade и freshen
Установка или обновление RPM-пакета. Команда install имеет следующий формат:

rpm -i [install-options] package_file ...
rpm --install [install-options] package_file ...

Для того чтобы установить новую версию пакета и удалить при этом существующую, выполните команду upgrade:

rpm -U [install-options] package_file ...
rpm --upgrade [install-options] package_file ...

При использовании -U, если пакет отсутствует в системе, rpm ведет себя так, как если бы был указан параметр -i и просто устанавливает пакет. Обратного можно добиться с помощью команды freshen. rpm произведет обновление пакета только в том случае, если будет найдена предыдущая версия.
Формат команды freshen:

rpm -F [install-options] package_file ...
rpm --freshen [install-options] package_file ...

Следующие параметры доступны для установки и обновления:
--allfiles
Установка или обновление всех файлов.
--badreloc
Применяется совместно с --relocate, для того чтобы выполнить принудительное перемещение, даже если пакет не является перемещаемым.
--excludedocs
Не устанавливать файлы документации.
--excludepath path
Не устанавливать файлы, имена которых начинаются с path.