---
source_image: page_044.png
page_number: 44
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.59
tokens: 7419
characters: 1951
timestamp: 2025-12-24T04:33:04.441751
finish_reason: stop
---

система man-pages(7) состоит из отдельных страниц, посвященных отдельным командам, специальным файлам устройств, конфигурационным файлам, системным и библиотечным вызовам и другим понятиям, которые сгруппированы по восьми (обычно, но есть исключения из правил) секциям. Каждая секция имеет заголовочную страницу intro, описывающую назначение самой секции (листинг 2.16).

**Листинг 2.16. Секции справочной системы man(1)**

finn@ubuntu:~$ whatis intro
intro (8)      - introduction to administration and privileged commands
intro (7)      - introduction to overview and miscellany section
intro (3)      - introduction to library functions
intro (4)      - introduction to special files
intro (1)      - introduction to user commands
intro (5)      - introduction to file formats and filesystems
intro (6)      - introduction to games
intro (2)      - introduction to system calls

finn@ubuntu:~$ whatis whatis
whatis (1)     - показывает односторочные описания справочных страниц

finn@ubuntu:~$ whatis apropos
apropos (1)    - поиск в именах справочных страниц и кратких описаниях

finn@ubuntu:~$ whatis man
man (1)        - доступ к справочным страницам
man (7)        - macros to format man pages

Естественным образом справочная система описывает сама себя, поэтому известнейшей «мантрой» в операционной системе является man man, т. е. запрос страницы руководства, посвященной самой команде man(1). Сами страницы руководства написаны на языке разметки текста roff¹ и размещаются в сжатых gz-файлах «секционных» подкаталогов man1, man2, ..., man8 каталога /usr/share/man (листинг 2.17). Страницы руководства частично поставляются переведенными на различные национальные языки, отличные от английского.

**Листинг 2.17. Формат страниц справочной системы man**

finn@ubuntu:~$ man -w man
/usr/share/man/ru/man1/man.1.gz
finn@ubuntu:~$ file /usr/share/man/ru/man1/man.1.gz

¹ Система подготовки текстов, доставшаяся в наследство от классической UNIX.