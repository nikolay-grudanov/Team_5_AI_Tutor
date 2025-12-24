---
source_image: page_502.png
page_number: 502
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.66
tokens: 11343
characters: 557
timestamp: 2025-12-24T09:47:56.532070
finish_reason: stop
---

Рис. 15.6. Если вы посмотрите на этот заголовок в реальном Web-браузере, вы увидите, что текст все время меняет размер, привлекая к себе внимание

ременная growIncrement определяет, насколько меняется размер шрифта при каждом выполнении кода браузером (первоначально он увеличивается каждый раз на 2 пиксела).

<!DOCTYPE html>

<html>
<head>
    <title>Dynamic HTML</title>
    <script>
        //<![CDATA[
            // Текущий размер шрифта
            var size = 10
            // Величина, на которую изменяется размер
            var growIncrement = 2