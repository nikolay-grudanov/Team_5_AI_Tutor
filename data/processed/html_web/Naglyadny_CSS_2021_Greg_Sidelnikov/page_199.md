---
source_image: page_199.png
page_number: 199
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.14
tokens: 7344
characters: 1445
timestamp: 2025-12-24T09:25:12.212342
finish_reason: stop
---

001 @mixin flexible() {
002     display: flex;
003     justify-content: center;
004     align-items: center;
005 }
006
007 .centered-elements {
008     @include flexible();
009     border: 1px solid gray;
010 }

Теперь каждый раз, когда вы применяете класс .centered-elements к HTML-элементу, последний превращается во flex-элемент. Одним из ключевых преимуществ примесей является то, что их можно использовать вместе с другими свойствами CSS. Здесь я также добавил стиль border: 1px solid gray к классу .centered-elements в дополнение к примеси.

Вы даже можете передать аргументы @mixin, как если бы это была функция, а затем назначить их свойствам CSS. Мы рассмотрим данный процесс в следующем разделе.

25.8. Поддержка разных браузеров

Некоторые экспериментальные функции (например, -webkit-свойства) или Firefox (-moz-свойства) работают только в отдельных браузерах.

Примеси могут быть полезны для определения специфичных для браузера свойств CSS в одном классе. Например, при необходимости повернуть элемент в браузерах на движке Webkit, а также в других можно создать примесь, принимающую аргумент $degree.

001 @mixin rotate($degree) {
002     -webkit-transform: rotate($degree); // движок WebKit
003     -moz-transform: rotate($degree);    // Firefox
004     -ms-transform: rotate($degree);     // Internet Explorer
005     -o-transform: rotate($degree);      // Opera
006     transform: rotate($degree);         // Стандарт CSS
007 }