---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.11
tokens: 6072
characters: 824
timestamp: 2025-12-24T10:04:12.786525
finish_reason: stop
---

Затем запустите JSDOC следующим образом:

/bin/sh $JSDOCDIR/jsrun.sh -d=jsdoc mySum.js

Этот код создаст несколько HTML-файлов в каталоге jsdoc. Самый интересный HTML-файл выглядит подобно изображенному на рис. 2.3.

Вывод очень симпатичный, но не до такой степени, как в случае с YUIDoc.

![HTML, сгенерированный директивами jsdoc](https://i.imgur.com/3Q5z5QG.png)

Рис. 2.3. HTML, сгенерированный директивами jsdoc

Генераторы документации Docco/Rocco

Как сказано на официальном сайте компании-производителя: "Docco — быстрый и "грамотный" генератор документации вашего кода".

Docco (http://jashkenas.github.io/docco/) — родитель целого семейства программ, которые делают одно и то же: извлекают комментарии, размеченные в стиле Markdown13, из исходного кода и преоб-

13 Markdown (Маркдаун) — облегченный язык разметки.