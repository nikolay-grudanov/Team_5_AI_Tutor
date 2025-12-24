---
source_image: page_504.png
page_number: 504
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.87
tokens: 7816
characters: 1985
timestamp: 2025-12-24T02:54:22.424016
finish_reason: stop
---

Магическая функция %alias позволяет определять собственные сокращения для команд оболочки, например:

In [1]: %alias ll ls -l

In [2]: ll /usr
total 332
drwxr-xr-x   2 root root    69632 2012-01-29 20:36 bin/
drwxr-xr-x   2 root root     4096 2010-08-23 12:05 games/
drwxr-xr-x  123 root root   20480 2011-12-26 18:08 include/
drwxr-xr-x  265 root root  126976 2012-01-29 20:36 lib/
drwxr-xr-x   44 root root   69632 2011-12-26 18:08 lib32/
lrwxrwxrwx   1 root root     3 2010-08-23 16:02 lib64 -> lib/
drwxr-xr-x   15 root root   4096 2011-10-13 19:03 local/
drwxr-xr-x   2 root root   12288 2012-01-12 09:32 sbin/
drwxr-xr-x  387 root root  12288 2011-11-04 22:53 share/
drwxrwsr-x  24 root src    4096 2011-07-17 18:38 src/

Несколько команд можно выполнить как одну, разделив их точками с запятой:

In [558]: %alias test_alias (cd examples; ls; cd ..)

In [559]: test_alias
macrodata.csv spx.csv tips.csv

Обратите внимание, что IPython «забывает» все определенные интерактивно псевдонимы после закрытия сеанса. Чтобы создать постоянные псевдонимы, нужно прибегнуть к системе конфигурирования.

Система закладок на каталоги
В IPython имеется простая система закладок, позволяющая создавать псевдонимы часто используемых каталогов, чтобы упростить переход в них. Например, пусть требуется создать закладку, указывающую на дополнительные материалы к этой книге:

In [6]: %bookmark py4da /home/wesm/code/pydata-book

После этого с помощью магической команды %cd я смогу воспользоваться ранее определенными закладками:

In [7]: cd py4da
(bookmark:py4da) -> /home/wesm/code/pydata-book
/home/wesm/code/pydata-book

Если имя закладки конфликтует с именем подкаталога вашего текущего рабочего каталога, то с помощью флага -b можно отдать приоритет закладке. Команда %bookmark с флагом -l выводит список всех закладок:

In [8]: %bookmark -l
Current bookmarks:
py4da -> /home/wesm/code/pydata-book-source

Закладки, в отличие от псевдонимов, автоматически сохраняются после закрытия сеанса.