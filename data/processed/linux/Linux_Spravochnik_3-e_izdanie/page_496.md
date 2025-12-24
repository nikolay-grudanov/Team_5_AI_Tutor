---
source_image: page_496.png
page_number: 496
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.15
tokens: 11623
characters: 1342
timestamp: 2025-12-24T03:37:33.742750
finish_reason: stop
---

кать gnorpm, даже если GNOME не используется. При запуске gnorpm открывает окно, которое позволяет управлять пакетами rpm посредством графического интерфейса. Формат вызова gnorpm следующий:

gnorpm [options]

Параметры gnorpm

В gnorpm доступны следующие параметры:

--geometry=geom
Определить геометрические параметры главного окна в стандартном для системы X формате (т. е. \( w \times h + x + y \)).

-i pkgfiles, --install pkgfiles
Установить указанные пакеты.

-p pkgs, --packages pkgs
Пакеты находятся в файлах, а не в базе данных rpm, т. е. еще не были установлены.

-q pkgs, --query pkgs
Создать окно запроса для указанных установленных пакетов.

-qr pkgfiles, --query --packages pkgfiles
Создать окно запроса для указанных файлов пакета. Идентично указанию параметров -q и -p.

-U pkgfiles, --upgrade pkgfiles
Обновить указанные пакеты.

-K pkgfiles, --checksig pkgfiles
Проверить подписи указанных пакетов.

-y pkgs, --verify pkgs
Проверить указанные пакеты.

-?, --help
Отобразить справку и завершить работу.

--root=dir
Считать dir корнем файловой системы.

--usage
Отобразить краткую справку по использованию и завершить работу.

Окно GNOME-RPM

Главное окно GNOME-RPM делится на пять частей. Наверху расположено меню с тремя кнопками:

Packages (Пакеты)
Содержит пункты Query (Запрос), Uninstall (Удаление) и Verify (Проверка).