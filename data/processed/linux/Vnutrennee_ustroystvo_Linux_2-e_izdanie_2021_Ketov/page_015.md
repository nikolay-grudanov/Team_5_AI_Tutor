---
source_image: page_015.png
page_number: 15
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.46
tokens: 7455
characters: 1738
timestamp: 2025-12-24T04:32:16.081051
finish_reason: stop
---

bart@ubuntu:~$ sudo apt install finger
[sudo] password for bart:
Чтение списков пакетов... Готово
Построение дерева зависимостей
Чтение информации о состоянии... Готово
Следующие НОВЫЕ пакеты будут установлены:
finger
Обновлено 0 пакетов, установлено 1 новых пакетов, для удаления отмечено 0 пакетов, и 11 пакетов не обновлено.
Необходимо скачать 16,9 kB архивов.
После данной операции объём занятого дискового пространства возрастёт на 51,2 kB.
Пол:1 http://ru.archive.ubuntu.com/ubuntu eoan/universe amd64 finger amd64 0.17-17 [16,9 kB]
Получено 16,9 kB за 0с (200 kB/s)
Подготовка к распаковке .../finger_0.17-17_amd64.deb ...
Распаковывается finger (0.17-17) ...
Настраивается пакет finger (0.17-17) ...
Обрабатываются триггеры для man-db (2.8.7-3) ...

В редких случаях, когда нужно узнать, с каким, даже еще неустановленным, пакетом программного обеспечения поставляется тот или иной файл, может выручить утилита apt-file(1) (1, листинг ВЗ). В обратную сторону посмотреть список файлов, входящих в еще неустановленный пакет, можно этой же утилитой 2.

Листинг ВЗ. В каком пакете файл (файлы)?

1 bart@ubuntu:~$ apt-file search bin/7z
Finding relevant cache files to search ...E: The cache is empty. You need to run "apt-file update" first.
bart@ubuntu:~$ sudo apt-file update
Сущ:1 http://ru.archive.ubuntu.com/ubuntu eoan InRelease
Пол:2 http://ru.archive.ubuntu.com/ubuntu eoan-updates InRelease [97,5 kB]
Пол:3 http://ru.archive.ubuntu.com/ubuntu eoan-backports InRelease [88,8 kB]
Получено 91,9 MB за 37с (2 515 kB/s)
Чтение списков пакетов... Готово
Построение дерева зависимостей
Чтение информации о состоянии... Готово
bart@ubuntu:~$ apt-file search bin/7z
p7zip: /usr/bin/7zr
p7zip-full: /usr/bin/7z
p7zip-full: /usr/bin/7za