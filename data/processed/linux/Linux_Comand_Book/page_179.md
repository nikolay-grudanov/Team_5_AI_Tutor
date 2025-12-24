---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.35
tokens: 6019
characters: 1348
timestamp: 2025-12-24T04:08:29.023483
finish_reason: stop
---

\    Просмотреть исходный HTML-текст (нажмите еще раз, чтобы вернуться к нормальному виду)
lynx имеет более 100 командных опций, так что имеет смысл изучить его man-страницу.

Полезные опции
- dump Вывести отображенную страницу в стандартный поток вывода и выйти из программы (сравните с опцией -source)
- source Вывести исходный HTML-текст в стандартный поток вывода и выйти из программы (сравните с командами wget и curl)
-emacskeys Сделать так, чтобы lynx понимал клавишиные комбинации редактора emacs
-vikeys Сделать так, чтобы lynx понимал клавишиные комбинации редактора vim (или vi)
-homepage=URL Сделать вашей домашней страницей адрес URL
-color Включить и отключить цветной режим
-nocolor

wget [опции] URL wget
/usr/bin stdin stdout -file -opt --help --version
Команда wget идет по URL-адресу и скачивает информацию в файл или стандартный поток вывода. Она великолепно подходит для скачивания отдельных страниц или всей иерархии веб-страниц до заданной вложенности. Например, давайте скачаем главную страницу Yahoo:
$ wget http://www.yahoo.com
http://www.yahoo.com/
=> chindex.html'
Resolving www.yahoo.com... done. Connecting to www.yahoo.com[216.109.118.66]: 80... connected.
HTTP request sent, awaiting response... 200 OK Length: unspecified [text/html]
[ <=> ]
| 31,434   220.84K/S
23:19:51 (220.84 KB/s) - chindex.html' saved [31434]