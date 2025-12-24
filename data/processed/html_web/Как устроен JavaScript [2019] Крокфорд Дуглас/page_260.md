---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.40
tokens: 7220
characters: 1263
timestamp: 2025-12-24T10:00:23.094196
finish_reason: stop
---

27.14    Как работает парсер

if (open) {
    indent();
}
while (true) {
    line_check(open);
    let the_parameter = token;
    register(the_parameter);
    advance();
    if (token.id === "...") {
        parameters.push(ellipsis(the_parameter));
        break;
    }
    if (token.id === "|") {
        advance("|");
        parameters.push(parse_suffix["|"](the_parameter, prev_token));
    } else {
        parameters.push(the_parameter);
    }
    if (open) {
        if (token.id === ","") {
            return error(token, "unexpected ','");
        }
        if (token.alphameric !== true) {
            break;
        }
    } else {
        if (token.id !== ","") {
            break;
        }
        same_line();
        advance(",");
        if (token.alphameric !== true) {
            return error(token, "expected another parameter");
        }
    }
    if (open) {
        outdent();
        at_indentation();
    } else {
        same_line();
    }
}
the_function.zeroth = parameters;

У функции может быть (возвращаемое_выражение) или {тело_функции}.

Парсинг возвращаемого выражения:

if (token.id === "(") {
    advance("(");
    if (is_line_break()) {
        indent();
        the_function.wunth = expression(0, true);
        outdent();