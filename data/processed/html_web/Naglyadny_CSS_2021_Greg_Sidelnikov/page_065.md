---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.06
tokens: 7103
characters: 730
timestamp: 2025-12-24T09:21:58.970527
finish_reason: stop
---

Далее свойству text-orientation присваивается значение upright. При- менимо к SVG-элементам свойство use-glyph-direction заменяет устаревшие свойства use-direction-vertical и use-direction-horizontal.

writing-mode: vertical-rl;
text-orientation: use-glyph-orientation;

writing-mode: vertical-lr;
text-orientation: use-glyph-orientation;

writing-mode: vertical-rl;
text-orientation: upright;

writing-mode: vertical-lr;
text-orientation: upright;

Чтобы центрировать текст по вертикали в любом элементе, установите его высоту строки с помощью свойства line-height: 60px. Размер шрифта и значение свойства line-height не всегда совпадают:

Элемент <body> или любой другой родительский контейнер, такой как <div>
line-height: 60px