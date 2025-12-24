---
source_image: page_866.png
page_number: 866
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.48
tokens: 7448
characters: 1784
timestamp: 2025-12-24T05:09:24.327689
finish_reason: stop
---

9. Как добавить постоянный псевдоним mypass, который отображает содержимое файла /etc/passwd:
а) введите команду nano $HOME/.bashrc;
б) переместите курсор на открытую строку в нижней части страницы. (При необходимости нажмите клавишу Enter, чтобы открыть новую строку);
в) в отдельной строке введите alias m="cat /etc/passwd";
г) нажмите сочетание клавиш Ctrl+O, чтобы сохранить изменения, и Ctrl+X, чтобы закрыть файл;
д) введите команду source $HOME/.bashrc;
е) введите команду alias m, чтобы убедиться в том, что псевдоним установлен правильно: alias m='cat/etc/passwd';
ж) введите команду m (файл /etc/passwd появится на экране).
10. Чтобы отобразить справочную страницу системного вызова mount, используйте команду man -k. Затем примените команду mount с правильным номером раздела (8), чтобы открыть нужную справочную страницу mount:

$ man -k mount | grep ^mount
mount      (2)   - mount filesystem
mount      (8)   - mount a filesystem
...
mountpoint (1)   - see if a directory is a mountpoint
mountstats (8)   - Displays various NFS client per-mount statistics
$ man 2 mount
MOUNT(2)    Linux Programmer's Manual MOUNT(2)
NAME
    mount - mount file system
SYNOPSIS
    #include <sys/mount.h>

Глава 4. Файловая система

1. Создайте каталог projects, девять пустых файлов (от house1 до house9) и перечислите только эти файлы:

$ mkdir $HOME/projects/
$ touch $HOME/projects/house{1..9}
$ ls $HOME/projects/house{1..9}

2. Создайте путь к каталогу $HOME/projects/houses/doors/ и несколько пустых файлов в нем:

$ cd
$ mkdir $HOME/projects/houses
$ touch $HOME/projects/houses/bungalow.txt
$ mkdir $HOME/projects/houses/doors/
$ touch $HOME/projects/houses/doors/bifold.txt
$ mkdir -p $HOME/projects/outdoors/vegetation/
$ touch $HOME/projects/outdoors/vegetation/landscape.txt