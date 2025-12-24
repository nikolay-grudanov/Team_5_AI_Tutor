---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.00
tokens: 7492
characters: 2141
timestamp: 2025-12-24T04:33:09.118607
finish_reason: stop
---

/usr/share/man/ru/man1/man.1.gz: gzip compressed data, max compression, from Unix,
original size modulo 2^32 65164

finn@ubuntu:~$ file -z /usr/share/man/ru/man1/man.1.gz
/usr/share/man/ru/man1/man.1.gz: troff or preprocessor input, UTF-8 Unicode text
(gzip compressed data, max compression, from Unix)

finn@ubuntu:~$ whatis file
file (1) - determine file type

Команда man(1), таким образом, ответственна за поиск указанной пользователем страницы, распаковку ее сжатого файла при помощи распаковщика gzip(1), форматирования при помощи процессора troff(1) и (по умолчанию) вывод результата на терминал при помощи постраничного «листателя» less(1). Именно процессор troff умеет посредством управляющих последовательностей нужного терминала раскрывать вывод страниц руководства правильным образом, а «листатель» less прокручивать подготовленную справку вперед и назад.

Использование языка разметки позволяет форматировать страницу одинаково удобно для просмотра на разных терминалах с различным количеством столбцов, которые учитывает troff, и разным количеством строк, учитываемым less. Так, например, результат одинаково хорош и на псевдотерминале в окне эмулятора терминала xterm или gnome-terminal развернутого в любой размер, и на виртуальном терминале консоли с загруженным шрифтом любого размера. Более того, использование универсального языка разметки и соответствующий «драйвер» troff позволяет преобразовывать страницы руководства в самые разные виды. Например, в «принтерный» PostScript или PCL, пригодный для печати на принтере с высокой разрешающей способностью, или в HTML¹ для просмотра в html-браузере (листинг 2.18).

Листинг 2.18. Форматирование справочных страниц руководства для печати и для html-браузера

finn@ubuntu:~$ man -t man > man.print.1
finn@ubuntu:~$ file man.print.1
man.print.1: PostScript document text conforming DSC level 3.0
finn@ubuntu:~$ man -Tlj4 man > man.print.2
finn@ubuntu:~$ file man.print.2
man.print.2: HP PCL printer data
finn@ubuntu:~$ man -Thtml man > man.html
finn@ubuntu:~$ file man.html
man.html: HTML document, ASCII text, with very long lines

¹ При наличии установленного пакета groff.