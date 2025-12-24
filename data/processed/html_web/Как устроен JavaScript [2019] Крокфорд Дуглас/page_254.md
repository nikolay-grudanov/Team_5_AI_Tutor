---
source_image: page_254.png
page_number: 254
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.38
tokens: 7302
characters: 1355
timestamp: 2025-12-24T10:00:24.397641
finish_reason: stop
---

27.8 Как работает парсер

    } else {
        same_line();
    }
}
advance(")\"");
the_paren.zeroth = left;
the_paren.wunth = args;
return the_paren;
}

Функция suffix создает массив parse_suffix. Она принимает оператор и уровень приоритета, а также необязательный парсер. Он может предоставить функцию парсера, используемую по умолчанию и работающую для большинства операторов.

function suffix(
    id,
    precedence,
    optional_parser = function infix(left, the_token) {
        the_token.zeroth = left;
        the_token.wunth = expression(precedence);
        return the_token;
    }
) {

Создание инфиксного или суффиксного оператора:

const the_symbol = Object.create(null);
the_symbol.id = id;
the_symbol.precedence = precedence;
the_symbol.parser = optional_parser;
parse_suffix[id] = Object.freeze(the_symbol);
}

suffix("|", 111, function parse_default(left, the_bar) {
    the_bar.zeroth = left;
    the_bar.wunth = expression(112);
    advance("|");
    return the_bar;
});

suffix("?", 111, function then_else(left, the_then) {
    the_then.zeroth = left;
    the_then.wunth = expression();
    advance("!");
    the_then.twoth = expression();
    return the_then;
});
suffix("\\\\", 222);
suffix("\\/", 222);
suffix("~", 444);
suffix("≈", 444);
suffix("+", 555);
suffix("-", 555);
suffix("<<", 555);
suffix(">>", 555);
suffix("*", 666);