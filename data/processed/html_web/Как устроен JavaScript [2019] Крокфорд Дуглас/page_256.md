---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.65
tokens: 7361
characters: 1734
timestamp: 2025-12-24T10:00:33.946050
finish_reason: stop
---

27.10    Как работает парсер

Парсер литерала массива вызывает для каждого элемента функцию expression. Элемент — это любое выражение, за которым может стоять многоточие (...). Существует три способа записи литерала массива:

• пустой — [], массив нулевой длины;
• закрытый — весь литерал в одну строку, в качестве разделителей — запятые;
• открытый — после левой квадратной скобки ([]) перевод строки, углубление отступа, правая квадратная скобка (]), которая восстанавливает прежний отступ, выражение с разделителями в виде запятой (,) или точки с запятой (;) и/или перевод строки.

С помощью точки с запятой (;) создаются двумерные массивы.

[[2, 7, 6], [9, 5, 1], [4, 3, 8]]

может быть записан в виде:

[2, 7, 6; 9, 5, 1; 4, 3, 8]

prefix("[", function arrayliteral(the_bracket) {
    let matrix = [];
    let array = [];
    if (!is_line_break()) {
        while (true) {
            array.push(ellipsis(expression()));
            if (token.id == ",") {
                same_line();
                advance(",");
            } else if (
                token.id == ";"
                && array.length > 0
                && next_token != "]"
            ) {
                same_line();
                advance(";");
                matrix.push(array);
                array = [];
            } else {
                break;
            }
        }
        same_line();
    } else {
        indent();
        while (true) {
            array.push(ellipsis(expression(0, is_line_break())));
            if (token.id == "]" || token == the_end) {
                break;
            }
            if (token.id == ";") {
                if (array.length == 0 || next_token.id == "]") {
                    break;
                }
