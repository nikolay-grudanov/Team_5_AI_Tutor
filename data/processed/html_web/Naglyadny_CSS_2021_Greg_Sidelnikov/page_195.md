---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.25
tokens: 7347
characters: 1319
timestamp: 2025-12-24T09:25:04.327111
finish_reason: stop
---

обходимо изучить только основы. Они будут рассмотрены в следующих разделах данной главы.

В ряде случаев SCSS и SASS будут использоваться взаимозаменяемо, хотя синтаксис немного отличается. Однако прежде всего мы сосредоточимся на SCSS.

Весь код SASS/SCSS компилируется обратно в стандартный CSS, поэтому браузер может реально понимать и отображать результаты (сегодня браузеры не имеют прямой поддержки SASS/SCSS или любого другого препроцессора CSS).

25.2. Необходимые условия

Препроцессоры CSS добавляют новые функции к синтаксису языка CSS.

Существует пять препроцессоров CSS: SASS, SCSS, Less, Stylus и PostCSS.

Данная глава охватывает только SCSS, который подобен SASS. Больше узнать о SASS можно на сайте www.SASS-lang.com.

□ SASS (.SASS) — Syntactically Awesome Style Sheets.
□ SCSS (.scss) — SASSy Cascading Style Sheets.

Расширения .SASS и .scss похожи, но не одинаковы. Можно конвертировать из формата .SASS в .scss и обратно.

001 # Преобразование Sass в SCSS
002 $ sass-convert style.sass style.scss
003
004 # Преобразование SCSS в Sass
005 $ sass-convert style.scss style.sass

SASS являлась первой спецификацией для SASSy CSS с расширением файла .SASS. Разработка началась в 2006 году. Но позже был разработан альтернативный синтаксис с расширением .scss, лучший по мнению некоторых разработчиков.