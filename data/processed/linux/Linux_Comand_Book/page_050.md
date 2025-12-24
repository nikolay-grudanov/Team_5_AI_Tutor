---
source_image: page_050.png
page_number: 50
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.54
tokens: 6004
characters: 1271
timestamp: 2025-12-24T04:05:50.850400
finish_reason: stop
---

rpm -qf filename

Выводит название пакета, который установил указанный файл в вашей системе.

$ rpm -qf /usr/bin/who sh-utils-2.0-11

rpm -ivh packagel. rpm package2. rpm... Устанавливает пакеты, отсутствующие в вашей системе.
rpm -Fvh packagel. rpm package2. rpm... Обновляет пакеты, которые уже установлены в вашей системе.

rpm -e package__names

Удаляет пакеты из вашей системы. В этом случае не нужно указывать номер версии пакета, нужно задать только его название. Например, если вы установили пакет GNU Emacs из файла emacs-20.7-17. i386.rpm, то для его удаления нужно выполнить команду rpm -e emacs, а не rpm -e emacs-20.7-17.1386.rpm.

Файлы tar.gz и tar.bz2

Упакованные программные файлы с именами, оканчивающимися на .tar.gz и Jar.bz2, как правило, содержат исходный код пакета, который перед установкой вам нужно будет скомпилировать ("собрать").

1. Просмотрите содержимое пакета файл за файлом.
Убедитесь в том, что при распаковке ни одним из новых файлов вы не перепишете уже имеющиеся в системе, случайно или намеренно.

$ tar tvzf package, tar.gz I less Для gzip-файлов
$ tar tvjf package.tar.bz2 j less Для bzip1-файлов

2. Если все нормально, распакуйте файлы в новую директорию.
$ mkdir newdir
$ cd newdir
$ tar xvzf package, tar . gz Для gzip-файлов