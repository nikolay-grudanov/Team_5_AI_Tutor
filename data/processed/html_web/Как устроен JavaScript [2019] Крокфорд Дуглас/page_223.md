---
source_image: page_223.png
page_number: 223
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.12
tokens: 7173
characters: 1024
timestamp: 2025-12-24T09:59:29.379088
finish_reason: stop
---

if (classifier !== undefined) {
    classification = classifier(...args);
    if (typeof classification !== "string") {
        return reject;
    }
}

Создание функции вердикта, которая заключает в себя функцию регистрации:

let verdict = function (result) {
    return register(serial, result);
};

Регистрация объекта, представляющего данную попытку:

register(serial, {
    args,
    claim: the_claim,
    classification,
    classifier,
    name,
    predicate,
    serial,
    signature,
    verdict
});

Вызов предиката, передача ему функции вердикта и всех аргументов примера; чтобы сигнализировать о результате примера, предикат должен использовать обратный вызов вердикта:

return predicate(verdict, ...args);
}
all_claims.push(the_claim);
}

И наконец, создается и возвращается экземпляр:

return Object.freeze({
Спецификаторы:
    any,
    array,
    boolean,
    character,
    falsy,
    integer,
    literal,
    number,
    object,
    wun_of,
    sequence,
    string

Основные функции:
    check,
    claim