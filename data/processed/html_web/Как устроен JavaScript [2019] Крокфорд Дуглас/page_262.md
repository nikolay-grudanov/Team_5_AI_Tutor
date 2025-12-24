---
source_image: page_262.png
page_number: 262
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.81
tokens: 7341
characters: 1699
timestamp: 2025-12-24T10:00:34.106525
finish_reason: stop
---

27.16 Как работает парсер

    at_indentation();
    prelude();
    let parser = parse_statement[prev_token.id];
    if (parser === undefined) {
        return error(prev_token, "expected a statement");
    }
    prev_token.class = "statement";
    the_statement = parser(prev_token);
    statement_list.push(the_statement);
    if (the_statement.disrupt === true) {
        if (token.column_nr === indentation) {
            return error(token, "unreachable");
        }
        break;
    }
}
if (statement_list.length === 0) {
    if (!token.id.startsWith("export")) {
        return error(token, "expected a statement");
    }
} else {
    statement_list.disrupt = the_statement.disrupt;
    statement_list.return = the_statement.return;
}
return statement_list;

Свойство disrupt помечает инструкции или списки инструкций, вызывающие отмену или возвращение. Свойство return помечает инструкции или списки инструкций, вызывающие возвращение.

Инструкция break вызывает отмену цикла. Парсеру передается лексема break. Она устанавливает условие выхода из текущего цикла:

parse_statement.break = function (the_break) {
    if (loop.length === 0) {
        return error(the_break, "'break' wants to be in a loop.");
    }
    loop[loop.length - 1] = "break";
    the_break.disrupt = true;
    return the_break;
};

Инструкция call вызывает функцию и игнорирует возвращаемое значение. Она используется для идентификации вызовов, происходящих исключительно из-за их побочных эффектов:

parse_statement.call = function (the_call) {
    the_call.zeroth = expression();
    if (the_call.zeroth.id !== "(") {
        return error(the_call, "expected a function invocation");
    }
    return the_call;
};