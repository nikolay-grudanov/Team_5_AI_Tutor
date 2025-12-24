---
source_image: page_208.png
page_number: 208
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.22
tokens: 7294
characters: 1045
timestamp: 2025-12-24T09:25:16.326915
finish_reason: stop
---

Директива @for

Эта директива может использоваться для повторения определений CSS несколько раз подряд.

Цикл for для пяти элементов:

001 @for $i from 1 through 5 {
002     .definition-#{$i} { width: 10px * $i; }
003 }

Данный цикл будет скомпилирован в следующий код CSS:

001 .definition-1 { width: 10px; }
002 .definition-2 { width: 20px; }
003 .definition-3 { width: 30px; }
004 .definition-4 { width: 40px; }
005 .definition-5 { width: 50px; }

Директива @each

Эта директива может использоваться для перебора списка значений:

001 @each $animal in platypus, lion, sheep, dove {
002     #{$animal}-icon {
003         background-image: url("/images/#{$animal}.png");
004     }
005 }

Этот код будет скомпилирован в следующий код CSS:

001 .platypus-icon {
002     background-image: url("/images/platypus.png");
003 }
004 .lion-icon {
005     background-image: url("/images/lion.png");
006 }
007 .sheep-icon {
008     background-image: url("/images/sheep.png");
009 }
010 .dove-icon {
011     background-image: url("/images/dove.png");
012 }