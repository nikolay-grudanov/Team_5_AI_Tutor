---
source_image: page_252.png
page_number: 252
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.62
tokens: 7413
characters: 1774
timestamp: 2025-12-24T10:00:29.390201
finish_reason: stop
---

27.6 Как работает парсер

Рассмотрим простой суффиксный оператор. Парсеру точки (.) передаются выражение слева и точка (.). Он проверяет допустимость выражения, расположенного слева. Также проверяет, является ли именем текущая лексема. Затем он собирает все в лексему . (точка) и возвращает ее.

function parse_dot(left, the_dot) {

Выражение слева должно быть переменной или выражением, способным возвратить объект (исключая литералы объектов).

    if (
        !left.alphameric
        && left.id !== "."
        && (left.id !== "[" || left.wunth === undefined)
        && left.id !== "("
    ) {
        return error(token, "expected a variable");
    }
    let the_name = token;
    if (the_name.alphameric !== true) {
        return error(the_name, "expected a field name");
    }
    the_dot.zeroth = left;
    the_dot.wunth = the_name;
    same_line();
    advance();
    return the_dot;
}

Парсер индекса ([ ]) немного интереснее. Ему передаются выражение слева и лексема левой квадратной скобки ([). Он проверяет допустимость выражения, расположенного слева. Затем вызывается выражение для получения содержимого в квадратных скобках. Если после левой квадратной скобки ([]) был перевод строки, значит, это открытое выражение. Парсер проходит мимо закрывающей квадратной скобки (]).

function parse_subscript(left, the_bracket) {
    if (
        !left.alphameric
        && left.id !== "."
        && (left.id !== "[" || left.wunth === undefined)
        && left.id !== "("
    ) {
        return error(token, "expected a variable");
    }
    the_bracket.zeroth = left;
    if (is_line_break()) {
        indent();
        the_bracket.wunth = expression(0, true);
        outdent();
        at_indentation();
    } else {
        the_bracket.wunth = expression();