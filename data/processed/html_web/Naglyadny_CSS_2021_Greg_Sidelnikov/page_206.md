---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.50
tokens: 7254
characters: 872
timestamp: 2025-12-24T09:25:09.614263
finish_reason: stop
---

Функция if()

if() — это функция.

Ее синтаксис довольно примитивен. Оператор вернет одно из двух указанных значений согласно условию:

001 /* Применение функции if() */
002 if(true, 1px, 2px) => 1px
003 if(false, 1px, 2px) => 2px

Директива @if

@if — это директива, используемая для ветвления в зависимости от условия.

001 /* Применение директивы @if */
002 p {
003   @if 1 + 1 == 2 { border: 1px solid; }
004   @if 7 < 5    { border: 2px dotted; }
005   @if null     { border: 3px double; }
006 }

Оператор if в SASSy состоит из:

001 p { border: 1px solid; }

Пример использования одного оператора if или конструкции if-else:

001 /* Создание переменной $type */
002 $type: river;
003
004 /* Окрашивание в синий, если переменной присвоено значение river */
006 div {
007   @if $type == river {
008     color: blue;
009   }
010 }
011
012 /* Условные цвета по абзацу */