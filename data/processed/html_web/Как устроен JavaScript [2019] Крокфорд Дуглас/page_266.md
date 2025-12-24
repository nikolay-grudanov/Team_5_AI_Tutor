---
source_image: page_266.png
page_number: 266
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.00
tokens: 7289
characters: 1519
timestamp: 2025-12-24T10:00:40.675184
finish_reason: stop
---

27.20    Как работает парсер

    loop[element_nr] = "return";
    }
});
if (is_line_break()) {
    return error(the_return, "'return' wants a return value.");
}
the_return.zeroth = expression();
if (token === "}") {
    return error(the_return, "Misplaced 'return'.");
}
the_return.disrupt = true;
the_return.return = true;
return the_return;
} catch (ignore) {
    return the_error;
}
};

Инструкция var объявляет переменную, значение которой может быть присвоено с помощью инструкции let. Если переменная не имеет явной инициализации, ее исходным значением становится null:

parse_statement.var = function (the_var) {
    if (!token.alphameric) {
        return error(token, "expected a name.");
    }
    same_line();
    the_var.zeroth = token;
    register(token);
    advance();
    if (token.id === ":") {
        same_line();
        advance(":");
        the_var.wunth = expression();
    }
    return the_var;
};
Object.freeze(parse_prefix);
Object.freeze(parse_suffix);
Object.freeze(parse_statement);

Инструкции import и export в parse_statement не включены, поскольку их местонахождение в исходном коде строго ограничено. Все инструкции import должны быть помещены до любых других инструкций. Разрешена только одна инструкция export, которая должна стоять самой последней.

function parse_import(the_import) {
    same_line();
    register(token, true);
    the_import.zeroth = token;
    advance();
    same_line();
    advance(":");
    same_line();
    the_import.wunth = token;
    advance("(text)");