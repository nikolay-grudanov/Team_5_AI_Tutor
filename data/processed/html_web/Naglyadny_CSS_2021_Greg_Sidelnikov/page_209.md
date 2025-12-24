---
source_image: page_209.png
page_number: 209
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.11
tokens: 7264
characters: 857
timestamp: 2025-12-24T09:25:12.593791
finish_reason: stop
---

Цикл @while

001 $index: 5;
002 @while $index > 0 {
003     .element-#{$index} { width: 10px * $index; }
004     $index: $index - 1;
005 }

Список из пяти HTML-элементов, созданных циклом while:

001 .element-5 { width: 50px; }
002 .element-4 { width: 40px; }
003 .element-3 { width: 30px; }
004 .element-2 { width: 20px; }
005 .element-1 { width: 10px; }

25.11. Функции SASS

С помощью SASS/SCSS можно определять функции, как и на любом другом языке.

Создадим функцию three-hundred-px(), возвращающую значение 300px:

001 @function three-hundred-px() {
002     @return 300px;
003 }
004
005 .name {
006     width: three-hundred-px();
007     border: 1px solid gray;
008     display: block;
009     position: absolute;
010 }

001 <div class = "name">Hello.</div>

Когда класс .name применяется к элементу, ему будет присвоено значение ширины 300px.

Hello.