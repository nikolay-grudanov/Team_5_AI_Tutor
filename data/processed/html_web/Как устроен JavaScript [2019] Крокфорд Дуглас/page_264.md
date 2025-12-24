---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.72
tokens: 7281
characters: 1566
timestamp: 2025-12-24T10:00:34.096960
finish_reason: stop
---

ограничения. Она называется lvalue и может быть переменной (var, а не def) или выражением, которое находит поле или элемент:

parse_statement.let = function (the_let) {

Инструкция let — единственное место, где разрешено вносить изменения.

Следующей лексемой должно быть имя:

    same_line();
    const name = token;
    advance();
    const id = name.id;
    let left = lookup(id);
    if (left === undefined) {
        return error(name, "expected a variable");
    }
    let readonly = left.readonly;

Теперь рассмотрим суффиксные инструкции [ ], ., [ и {.

    while (true) {
        if (token === the_end) {
            break;
        }
        same_line();

В данной позиции символы [ ] указывают на операцию добавления элемента в массив:

        if (token.id === "[[]") {
            readonly = false;
            token.zeroth = left;
            left = token;
            same_line();
            advance("[]");
            break;
        }
        if (token.id === ".") {
            readonly = false;
            advance(".");
            left = parse_dot(left, prev_token);
        } else if (token.id === "[") {
            readonly = false;
            advance("[");
            left = parse_subscript(left, prev_token);
        } else if (token.id === "(") {
            readonly = false;
            advance("(");
            left = parse_invocation(left, prev_token);
            if (token.id === ":") {
                return error(left, "assignment to the result of a function");
            }
        } else {
            break;
        }
    }