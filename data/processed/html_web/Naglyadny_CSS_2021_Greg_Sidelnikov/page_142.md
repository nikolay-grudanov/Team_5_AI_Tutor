---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.42
tokens: 7221
characters: 936
timestamp: 2025-12-24T09:23:51.262246
finish_reason: stop
---

Как видите, нельзя создавать grid-области неправильной формы. Они должны быть квадратными или прямоугольными.

Наш grid-макет может быть создан следующим образом:

div#grid {
    display: grid;
    grid-template-areas:
        'x y y y y'
        'x center center center w'
        'x center center center w'
        'x z z z z';
}

Соответствующий HTML-код выглядит так:

<div id = "grid">
    <div style = "grid-area: x">Left</div>
    <div style = "grid-area: y">Header</div>
    <div style = "grid-area: z">Footer</div>
    <div style = "grid-area: w">Right</div>
    <div style = "grid-area: center">Main</div>
</div>

Grid-области шаблона весьма уместны при создании первичной внешней рамки для макета. Часто внутренним ячейкам веб-разработчики назначают свойство display: flex.

21.1. Grid-верстка и медиазапросы

Медиазапросы

Медиазапросы похожи на оператор if. Они начинаются с правила @media, а в скобках указывается условие.