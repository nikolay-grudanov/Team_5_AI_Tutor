---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.79
tokens: 7308
characters: 1551
timestamp: 2025-12-24T10:00:17.645112
finish_reason: stop
---

if (definition === undefined) {
    return error(the_token, "expected a variable");
}
left = definition;
advance();
} else {

Лексема может быть префиксом: (, [, {, f.

    definition = parse_prefix[the_token.id];
    if (definition === undefined) {
        return error(the_token, "expected a variable");
    }
    advance();
    left = definition.parser(the_token);
}

У нас есть левая часть. Есть ли в правой части суффиксный оператор? Позволяет ли уровень приоритета использовать его? Если да, объединяем левую и правую части, чтобы сформировать новую левую часть.

while (true) {
    the_token = token;
    definition = parse_suffix[the_token.id];
    if (
        token.column_nr < indentation
        || (!open && is_line_break())
        || definition === undefined
        || definition.precedence <= precedence
    ) {
        break;
    }
    line_check(open && is_line_break());
    advance();
    the_token.class = "suffix";
    left = definition.parser(left, the_token);
}

После прохождения цикла ноль и более раз появляется возможность возвратить дерево парсинга выражения.

return left;
}

function expression(precedence, open = false) {

Выражения проверяются на наличие пробельного символа, а для выражений аргументов такая проверка не нужна.

    line_check(open);
    return argument_expression(precedence, open);
}

Свойство precedence определяет порядок парсинга суффиксного оператора. Свойство parser является функцией для парсинга префикса или суффикса. Свойство class может иметь значения "suffix", "statement" или undefined.