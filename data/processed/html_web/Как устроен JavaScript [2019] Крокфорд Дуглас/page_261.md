---
source_image: page_261.png
page_number: 261
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.05
tokens: 7254
characters: 1434
timestamp: 2025-12-24T10:00:28.308498
finish_reason: stop
---

    at_indentation();
    } else {
        the_function.wunth = expression();
        same_line();
    }
    advance(")\"");
} else {

Парсинг тела функции — тело должно содержать явно указанную инструкцию возврата return. Подразумеваемый возврат по достижении последней инструкции в теле не применяется.

    advance("{");
    indent();
    the_function.wunth = statements();
    if (the_function.wunth.return !== true) {
        return error(prev_token, "missing explicit 'return'");
    }

Парсинг обработчика сбоев:

    if (token.id === "failure") {
        outdent();
        at_indentation();
        advance("failure");
        indent();
        the_function.twoth = statements();
        if (the_function.twoth.return !== true) {
            return error(prev_token, "missing explicit 'return'");
        }
    }
    outdent();
    at_indentation();
    advance("}");
}
now_function = the_function.parent;
return the_function;
});

Функция statements выполняет парсинг инструкций, возвращая массив лексем этих инструкций. По мере надобности, чтобы отделить команду от лексемы, в ней используется функция prelude:

function statements() {
    const statement_list = [];
    let the_statement;
    while (true) {
        if (
            token === the_end
            || token.column_nr < indentation
            || token.alphameric !== true
            || token.id.startsWith("export")
        ) {
            break;
        }