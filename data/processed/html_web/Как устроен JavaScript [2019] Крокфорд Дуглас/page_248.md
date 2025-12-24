---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.15
tokens: 7262
characters: 1426
timestamp: 2025-12-24T10:00:14.633902
finish_reason: stop
---

27.2 Как работает парсер

}
prev_token = token;
token = next_token;
next_token = the_token_generator() || the_end;
}

function prelude() {

Если лексема token содержит пробел, она разбивается и ее правая часть помещается в prev_token. В противном случае выполняется переход к следующей лексеме.

    if (token.alphameric) {
        let space_at = token.id.indexOf(" ");
        if (space_at > 0) {
            prev_token = {
                id: token.id.slice(0, space_at),
                alphameric: true,
                line_nr: token.line_nr,
                column_nr: token.column_nr,
                column_to: token.column_nr + space_at
            };
            token.id = token.id.slice(space_at + 1);
            token.column_nr = token.column_nr + space_at + 1;
            return;
        }
    }
    return advance();
}

Пробельные символы играют в этом языке весьма важную роль. Перевод строки может сигнализировать о конце инструкции или элемента. Отступ может означать конец условия. Справиться с этим помогают следующие функции:

let indentation;

function indent() {
    indentation += 4;
}

function outdent() {
    indentation -= 4;
}

function at_indentation() {
    if (token.column_nr !== indentation) {
        return error(token, "expected at " + indentation);
    }
}

function is_line_break() {
    return token.line_nr !== prev_token.line_nr;
}

function same_line() {
    if (is_line_break()) {