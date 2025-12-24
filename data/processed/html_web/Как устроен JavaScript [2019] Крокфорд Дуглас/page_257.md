---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.48
tokens: 7193
characters: 1161
timestamp: 2025-12-24T10:00:20.832231
finish_reason: stop
---

same_line();
    advance(";");
    matrix.push(array);
    array = [];
} else if (token.id === "," || !is_line_break()) {
    same_line();
    advance(",");
}
    }
    outdent();
    if (token.column_nr !== indentation) {
        return error(token, "expected at " + indentation);
    }
}
advance("]");
if (matrix.length > 0) {
    matrix.push(array);
    the_bracket.zeroth = matrix;
} else {
    the_bracket.zeroth = array;
}
return the_bracket;
});

prefix("[]", function emptyarrayliteral(the_brackets) {
    return the_brackets;
});

Парсер литерала записи распознает четыре формы полей:

• переменная;
• имя: выражение;
• "строка": выражение;
• [выражение]: выражение.

prefix("{", function recordliteral(the_brace) {
    const properties = [];
    let key;
    let value;
    const open = the_brace.line_nr !== token.line_nr;
    if (open) {
        indent();
    }
    while (true) {
        line_check(open);
        if (token.id === "[") {
            advance("[");
            key = expression();
            advance("]");
            same_line();
            advance(":");
            value = expression();
        } else {
            key = token;