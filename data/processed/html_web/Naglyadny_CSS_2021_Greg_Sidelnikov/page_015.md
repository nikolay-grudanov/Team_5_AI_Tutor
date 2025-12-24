---
source_image: page_015.png
page_number: 15
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.03
tokens: 7171
characters: 812
timestamp: 2025-12-24T09:20:44.482350
finish_reason: stop
---

1.2. Внутреннее размещение

Вы можете ввести CSS-код непосредственно в HTML-документ между двумя тегами элемента style:

<html>
<head>
<style type = "text/css">
body p {
    background: white;
    color: black;
    font-family: Arial, sans-serif;
    font-size: 16px;
    line-height: 1.58;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
}
</style>
</head>
<body>
<p>CSS-стили внутри элемента style и применяются к этому абзацу в HTML-коде веб-страницы</p>
</body>
</html>

1.3. Строковое размещение

Строковое размещение CSS-кода с использованием атрибута style в элементе HTML:

<html>
<head></head>
<body style = "font-family: Arial;">
<p>При выводе в браузере этот абзац наследует форматирование шрифтом Arial из строкового стиля в родительском элементе.</p>
</body>
</html>