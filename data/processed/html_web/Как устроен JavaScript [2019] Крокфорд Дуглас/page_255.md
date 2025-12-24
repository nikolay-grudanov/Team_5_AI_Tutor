---
source_image: page_255.png
page_number: 255
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.86
tokens: 7313
characters: 1501
timestamp: 2025-12-24T10:00:28.236607
finish_reason: stop
---

suffix("/", 666);
suffix(".", 777, parse_dot);
suffix("[", 777, parse_subscript);
suffix("(", 777, parse_invocation);

Чтобы защититься от ошибок \( a < b \leq c \), отношение к реляционным операторам выстраивается немного иначе.

const rel_op = Object.create(null);

function relational(operator) {
    rel_op[operator] = true;
    return suffix(operator, 333, function (left, the_token) {
        the_token.zeroth = left;
        the_token.wunth = expression(333);
        if (rel_op[token.id] === true) {
            return error(token, "unexpected relational operator");
        }
        return the_token;
    });
}

relational("=");
relational("#");
relational("<");
relational(">");
relational("≤");
relational("≥");

Функция prefix создает массив parse_prefix. Следует обратить внимание на то, что левая круглая скобка (( ) и левая квадратная скобка ([ ) также находятся в массиве sparse_suffix. В этом нет никакой проблемы. Какая-либо двусмысленность напрочь отсутствует. Префиксные операторы не нуждаются в приоритете.

function prefix(id, parser) {
    const the_symbol = Object.create(null);
    the_symbol.id = id;
    the_symbol.parser = parser;
    parse_prefix[id] = Object.freeze(the_symbol);
}

prefix("(", function (ignore) {
    let result;
    if (is_line_break()) {
        indent();
        result = expression(0, true);
        outdent();
        at_indentation();
    } else {
        result = expression(0);
        same_line();
    }
    advance(")");
    return result;
});