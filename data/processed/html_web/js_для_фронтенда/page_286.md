---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.48
tokens: 6134
characters: 1155
timestamp: 2025-12-24T10:08:14.939459
finish_reason: stop
---

- несколько тестов:

% jute_submit_test --test test1.html --test test2.html

Также из командной строки вы можете прочитать список тестов из stdin:

% find . -name '*.html' -print | jute_submit_test -test -

По умолчанию выходные файлы помещаются в подкаталог output каталога docRoot. Вы можете изменить этот каталог, используя переменную конфигурации outputDir:

% jute config set jute:outputDir results

Обратите внимание, что полный путь к этому каталогу будет docRoot + outputDir, то есть выходной каталог должен находиться в пределах каталога docRoot. Все XML-результаты тестов и LCOV-данные будут помещены в этот каталог. Имена файлов с результатами тестов содержат строки User Agent, поэтому легко понять, в каком браузере проводился тот или иной тест. Рис. 8.2 показывает внешний вид панели Results после запуска теста.

У теста "toolbar" есть результаты в файле формата XML JUnit (см. гл. 4), а файл с выходной информацией содержит отладочную информацию (главным образом вывод YUI Test) и динамически сге-

![Рис. 8.2. Панель Results после запуска теста в JUTE](https://i.imgur.com/3Q5z5QG.png)

Рис. 8.2. Панель Results после запуска теста в JUTE