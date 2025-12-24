---
source_image: page_259.png
page_number: 259
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.03
tokens: 7287
characters: 1525
timestamp: 2025-12-24T10:00:28.710806
finish_reason: stop
---

array.forEach(function (element) {
    object[element] = value;
});
return Object.freeze(object);
}([
    "?", "|", "/\\", "\\/", "=", "#", "<", ">", "≤",
    "~", "~", "+", "-", ">>", "<<", "*", "/", "[", "("
]));

prefix("f", function function_literal(the_function) {

Если за символом \( f \) следует суффиксный оператор, создается соответствующий указатель на функцию.

    const the_operator = token;
    if (
        functino[token.id] === true
        && (the_operator.id !== "(" || next_token.id === ")")
    ) {
        advance();
        if (the_operator.id === "(") {
            same_line();
            advance(")");
        } else if (the_operator.id === "[") {
            same_line();
            advance("]");
        } else if (the_operator.id === "?") {
            same_line();
            advance("!");
        } else if (the_operator.id === "|") {
            same_line();
            advance("|");
        }
        the_function.zeroth = the_operator.id;
        return the_function;
    }

Настройка новой функции:

    if (loop.length > 0) {
        return error(the_function, "Do not make functions in loops.");
    }
    the_function.scope = Object.create(null);
    the_function.parent = now_function;
    now_function = the_function;

// Параметры функции поступают в трех формах.
//     имя
//     имя | значение_по_умолчанию |
//     имя...

Список параметров может быть открытым или закрытым:

    const parameters = [];
    if (token.alphameric === true) {
        let open = is_line_break();