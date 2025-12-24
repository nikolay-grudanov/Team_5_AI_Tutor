---
source_image: page_263.png
page_number: 263
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.79
tokens: 7391
characters: 1832
timestamp: 2025-12-24T10:00:40.119918
finish_reason: stop
---

Инструкция def регистрирует переменные, предназначенные только для чтения:

parse_statement.def = function (the_def) {
    if (!token.alphameric) {
        return error(token, "expected a name.");
    }
    same_line();
    the_def.zeroth = token;
    register(token, true);
    advance();
    same_line();
    advance(":");
    the_def.wunth = expression();
    return the_def;
};

Инструкция fail — самый рискованный эксперимент в Neo. Механизмы исключений в большинстве языков были сведены к простым каналам связи. Инструкция fail пытается исправить положение:

parse_statement.fail = function (the_fail) {
    the_fail.disrupt = true;
    return the_fail;
};

У инструкции if есть необязательное продолжение в виде инструкций else или else if. Если прерывание или возврата есть в обеих ветвях, то прерывание или возврат происходит и в самой инструкции if:

parse_statement.if = function if_statement(the_if) {
    the_if.zeroth = expression();
    indent();
    the_if.wunth = statements();
    outdent();
    if (token.column_nr === indentation) {
        if (token.id === "else") {
            advance("else");
            indent();
            the_if.twoth = statements();
            outdent();
            the_if.disrupt = the_if.wunth.disrupt && the_if.twoth.disrupt;
            the_if.return = the_if.wunth.return && the_if.twoth.return;
        } else if (token.id.startsWith("else if ")) {
            prelude();
            prelude();
            the_if.twoth = if_statement(prev_token);
            the_if.disrupt = the_if.wunth.disrupt && the_if.twoth.disrupt;
            the_if.return = the_if.wunth.return && the_if.twoth.return;
        }
    }
    return the_if;
};

Инструкция let является в Neo инструкцией присваивания значений. Левая сторона — это не обычное выражение. На нее накладываются более серьезные