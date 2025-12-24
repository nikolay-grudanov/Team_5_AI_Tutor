---
source_image: page_312.png
page_number: 312
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.56
tokens: 6096
characters: 978
timestamp: 2025-12-24T10:08:47.768723
finish_reason: stop
---

Рис. 8.20. Публикация дублирующегося кода в Jenkins

плагин Jenkins: установите плагин Duplicate Code Scanner (https://wiki.jenkins-ci.org/display/JENKINS/DRY+Plugin), он же DRY Plugin, в результате будет создано действие Publish duplicate code analysis results, которое вы можете использовать в своем проекте (рис. 8.20).

Пороговые значения приоритета позволяют вам настроить, сколько дублирующих строк является нормальным. Плагин тогда будет отслеживать число дублирующихся строк и выведет график всех дублирующихся секций кода. В расширенных настройках (кнопка Advanced) можно установить лимиты, когда плагин пометит сборку нестабильной (unstable) или неудачной (failed), см. рис. 8.21.

Рис. 8.21. Конфигурация пороговых значений дублирования кода в Jenkins

Установить dupfind просто. Скачайте dupfind.jar по адресу https://github.com/sfrancisx/dupfind и добавьте следующие строки в ваш make-файл:

dupfind: $(SRC)
    java -Xmx512m -jar ./dupfind.jar > output/dupfind.out