---
source_image: page_378.png
page_number: 378
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.77
tokens: 11745
characters: 1595
timestamp: 2025-12-24T03:32:05.901348
finish_reason: stop
---

---
primary_language: ru
is_rotation_valid: True
rotation_correction: 0
is_table: True
is_diagram: False
---
---version
    Вывести информацию о номере версии и завершить работу.
- Читать данные со стандартного ввода.

Примеры
Разбить файл bigfile на сегменты по 1000 строк:
    split bigfile
Объединить четыре файла, затем разбить результат на файлы по 10 строк, имеющие имена new.aa, new.ab и т. д. Обратите внимание, что без параметра «-» (стандартный ввод) имя new. трактовалось бы как несуществующий исходный файл:
    cat list[1-4] | split -10 - new.

stat filename [filenames...]
Для указанных файлов отобразить информацию по единицам inode в удобном для восприятия виде. Сообщения об ошибках «Can’t stat file» или «Can’t lstat file» обычно означают, что файл не существует. Ошибка «Can’t readlink file» обычно означает сбой при чтении символьской ссылки.

Результат работы
Пример вывода команды:
    stat /
    File: "/"
    Size 1024    Filetype: Directory
    Mode: (0755/drwxr-xr-x)  Uid: (   0/ root) Gid: (   0/ system)
    Device 3,3   Inode: 2   Links: 21
    Access: Tue Apr 11 04:02:01 2000(00000.11:47:35)
    Modify: Wed Nov 17 11:46:38 1999(00146.03:02:58)
    Change: Wed Nov 17 11:46:38 1999(00146.03:02:58)

strace [options] command [arguments]
Отслеживание системных вызовов и сигналов в процессе выполнения указанной команды с необязательными аргументами. strace позволяет определить, как передаются данные между программой и ядром системы. Команда strace без аргументов отображает в стандартный поток ошибок по одной строке на каждый системный вызов. Для каждого вызова