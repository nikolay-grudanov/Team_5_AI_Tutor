---
source_image: page_300.png
page_number: 300
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.83
tokens: 7303
characters: 1589
timestamp: 2025-12-24T10:01:14.471475
finish_reason: stop
---

31.2 Как устроена эта книга

Если строк для сканирования больше нет, выполняется доставка результата:

    if (string == "") {
        return callback(result);
    }

Попытка сопоставления регулярного выражения с оставшейся строкой:

    object_of_matching = rx_include.exec(string);

Если соответствий не было, значит, наша работа выполнена:

    if (!object_of_matching) {
        return callback(result + string);
    }

Символы слева от выражения являются частью результата. Удаление отсканированного результата из строки:

    result += string.slice(0, object_of_matching.index);
    string = string.slice(
        object_of_matching.index + object_of_matching[0].length
    );

Вызов функции get_inclusion для получения строки замены с передачей assistant_minion и ключа:

    return get_inclusion(
        assistant_minion,
        object_of_matching[1]
    );
}

function junior_assistant_minion(processed_inclusion) {

Прием включения, обработанного функцией include, и добавление его к результату — затем вызов функции minion для начала поиска следующего выражения @include:

    result += processed_inclusion;
    return minion();
}

function assistant_minion(inclusion) {

Если функция get_inclusion не доставила строку, к результату добавляется выражение @include, экономно оставляя эту часть строки без изменений:

    if (typeof inclusion !== "string") {
        result += object_of_matching[0];
        return minion();
    }

Включение может содержать собственные выражения @include, поэтому из обработки вызывается include с передачей junior_assistant_minion, добавляющей