---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.34
tokens: 7275
characters: 1445
timestamp: 2025-12-24T09:58:02.077912
finish_reason: stop
---

Создание объекта причины reason — эти объекты используются для исключений и отмен и создаются из объектов Error:

    const reason = new Error("parseq." + factory_name + (
        excuse === undefined
        ? ""
        : ": " + excuse
    ));
    reason.evidence = evidence;
    return reason;
}

Функция обратного вызова с двумя параметрами:

function check_callback(callback, factory_name) {
    if (typeof callback !== "function" || callback.length !== 2) {
        throw make_reason(factory_name, "Not a callback.", callback);
    }
}

Нужно убедиться, что все элементы в массиве — это функции-запросчики:

function check_requestor_array(requestor_array, factory_name) {

Массив requestor содержит только запросчики. Запросчик — это функция, принимающая один или два аргумента: функцию обратного вызова callback и необязательное исходное значение initial_value.

if (
    !Array.isArray(requestor_array)
    || requestor_array.length < 1
    || requestor_array.some(function (requestor) {
        return (
            typeof requestor !== "function"
            || requestor.length < 1
            || requestor.length > 2
        );
    })
) {
    throw make_reason(
        factory_name,
        "Bad requestors array.",
        requestor_array
    );
}

Функция run является сердцевиной Parseq. Она запускает запросчики и управляет соблюдением лимита времени, отменой и регулятором.

function run(
    factory_name,
    requestor_array,