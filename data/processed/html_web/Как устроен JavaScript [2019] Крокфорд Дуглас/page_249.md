---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.89
tokens: 7243
characters: 1446
timestamp: 2025-12-24T10:00:14.400633
finish_reason: stop
---

return error(token, "unexpected linebreak");
}
}

function line_check(open) {
    return (
        open
        ? at_indentation()
        : same_line()
    );
}

Функция register объявляет в области видимости функции новую переменную.
Функция lookup находит переменную в наиболее подходящей области видимости:

function register(the_token, readonly = false) {

Добавление переменной к текущей области видимости:

    if (now_function.scope[the_token.id] !== undefined) {
        error(the_token, "already defined");
    }
    the_token.readonly = readonly;
    the_token.origin = now_function;
    now_function.scope[the_token.id] = the_token;
}

function lookup(id) {

Поиск определения в текущей области видимости:

    let definition = now_function.scope[id];

Если происходит сбой, поиск в области видимости прародителей:

    if (definition === undefined) {
        let parent = now_function.parent;
        while (parent !== undefined) {
            definition = parent.scope[id];
            if (definition !== undefined) {
                break;
            }
            parent = parent.parent;
        }
    }

Если и здесь происходит сбой, поиск в фундаментальном объекте:

    if (definition === undefined) {
        definition = primordial[id];
    }

Следует помнить, что это определение используется текущей функцией:

    if (definition !== undefined) {
        now_function.scope[id] = definition;
    }
    return definition;
}