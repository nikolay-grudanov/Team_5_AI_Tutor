---
source_image: page_031.png
page_number: 31
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.58
tokens: 7243
characters: 996
timestamp: 2025-12-24T09:21:20.556925
finish_reason: stop
---

001 /* Устанавливаем белый цвет шрифта */
002 font-family: Arial, sans-serif;
003
004 /* Устанавливаем размер шрифта 16px */
005 font-size: 16px;
006
007 /* Добавляем отступы размером 32px */
008 padding: 32px;
009
010 /* Добавляем вокруг области контента отступ размером 16px */
011 margin: 16px;

1.14. Сокращенные нотации

Назначим три различных свойства, способствующих появлению фонового изображения HTML-элемента:

001 background-color: #000000;
002 background-image: url("image.jpg");
003 background-repeat: no-repeat;
004 background-position: left top;
005 background-size: cover;
006 background-attachment: fixed;

То же самое можно сделать, используя одно сокращенное свойство background, разделяя значения пробелом:

background: background-color background-image background-repeat;

Остальные комбинации настроек фона рассматриваются в главе 14.

001 background: #000000 url("image.jpg") left top no-repeat fixed;

Сокращения также применимы к различным свойствам grid- и flex-верстки.