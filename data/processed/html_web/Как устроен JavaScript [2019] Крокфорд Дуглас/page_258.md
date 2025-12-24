---
source_image: page_258.png
page_number: 258
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.60
tokens: 7235
characters: 1358
timestamp: 2025-12-24T10:00:23.269025
finish_reason: stop
---

27.12    Как работает парсер

    advance();
    if (key.alphameric === true) {
        if (token.id === ":") {
            same_line();
            advance(":");
            value = expression();
        } else {
            value = lookup(key.id);
            if (value === undefined) {
                return error(key, "expected a variable");
            }
        }
        key = key.id;
    } else if (key.id === "(text)") {
        key = key.text;
        same_line();
        advance(":");
        value = expression();
    } else {
        return error(key, "expected a key");
    }
    properties.push({
        zeroth: key,
        wunth: value
    });
    if (token.column_nr < indentation || token.id === "}") {
        break;
    }
    if (!open) {
        same_line();
        advance(",");
    }
    if (open) {
        outdent();
        at_indentation();
    } else {
        same_line();
    }
    advance("}");
    the_brace.zeroth = properties;
    return the_brace;
});

prefix("{}", function emptyrecordliteral(the_braces) {
    return the_braces;
});

Парсер функционального литерала создает новые функции. Он также предоставляет доступ к указателям на функции (functinos). Это название появилось у меня в результате опечатки.

    const functino = (function make_set(array, value = true) {
        const object = Object.create(null);