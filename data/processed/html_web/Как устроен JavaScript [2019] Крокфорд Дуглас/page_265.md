---
source_image: page_265.png
page_number: 265
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.71
tokens: 7376
characters: 1720
timestamp: 2025-12-24T10:00:45.152054
finish_reason: stop
---

advance(":");
if (readonly) {
    return error(left, "assignment to a constant");
}
the_let.zeroth = left;
the_let.wunth = expression();

В данной позиции символы [ ] указывают на операцию извлечения элемента из массива:

    if (token.id === "[" && left.id !== "[" && (
        the_let.wunth.alphameric === true
        || the_let.wunth.id === "."
        || the_let.wunth.id === "["
        || the_let.wunth.id === "("
    )) {
        token.zeroth = the_let.wunth;
        the_let.wunth = token;
        same_line();
        advance("[]");
    }
    return the_let;
};

Инструкция loop сохраняет стек для работы с вложенными циклами. Записи в стеке являются условиями выхода из циклов. Если явного выхода нет, статус стека имеет значение "infinite". Если единственный выход — это инструкция return, его статус — "return". Если выход из цикла выполняется с помощью инструкции break, его статусом становится "break". В данном случае fail не является явным условием выхода.

parse_statement.loop = function (the_loop) {
    indent();
    loop.push("infinite");
    the_loop.zeroth = statements();
    const exit = loop.pop();
    if (exit === "infinite") {
        return error(the_loop, "A loop wants a 'break'.");
    }
    if (exit === "return") {
        the_loop.disrupt = true;
        the_loop.return = true;
    }
    outdent();
    return the_loop;
};

Инструкция return изменяет статус циклов с "infinite" на "return":

parse_statement.return = function (the_return) {
    try {
        if (now_function.parent === undefined) {
            return error(the_return, "'return' wants to be in a function.");
        }
        loop.forEach(function (element, element_nr) {
            if (element === "infinite") {