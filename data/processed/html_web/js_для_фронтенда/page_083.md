---
source_image: page_083.png
page_number: 83
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.16
tokens: 6144
characters: 1099
timestamp: 2025-12-24T10:04:07.478924
finish_reason: stop
---

Рис. 2.2. Сгенерированный YUIDoc HTML-код

На мой взгляд, YUIDoc генерирует гораздо более привлекательные шаблоны (с возможностью поиска!), а его библиотека тегов более дружественна, чем в случае с JSDoc, с которым мы познакомимся в следующем разделе. Но выбор за вами. Наша задача состоит в том, чтобы дать обзор возможных решений.

Расширенные возможности генерации документации с помощью инструмента JSDoc

JSDoc (https://github.com/jsdoc/jsdoc) подобен YUIDoc, но обладает более обширным списком тегов (https://github.com/jsdoc/jsdoc).

Примечание.
Есть такой инструмент, как Google Closure Compiler (https://github.com/google/closure-compiler/wiki/Annotating-JavaScript-for-the-Closure-Compiler), который предназначен для минимизации, оптимизации и компиляции JavaScript-кода. Так вот он очень активно использует теги JSDoc, так что, изначально ориентируясь на оптимизацию с GCC, вы, используя теги JSDoc для комментирования, в итоге можете убить двух зайцев одним выстрелом.

JSDoc — это по сути Java-программа с немного аляповатой настройкой. Сама программа находится в JAR-файле + к нему ряд