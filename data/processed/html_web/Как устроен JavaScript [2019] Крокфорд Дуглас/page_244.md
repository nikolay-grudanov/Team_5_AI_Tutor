---
source_image: page_244.png
page_number: 244
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.59
tokens: 7237
characters: 1303
timestamp: 2025-12-24T10:00:01.619873
finish_reason: stop
---

26.3 Как работает разбиение на лексемы

Соответствует пробельный символ:

    if (captives[1]) {
        return token_generator();
    }

Соответствует комментарий:

    if (captives[2]) {
        return (
            comment
            ? {
                id: "(comment)",
                comment: captives[2],
                line_nr,
                column_nr,
                column_to: rx_token.lastIndex
            }
            : token_generator()
        );
    }

Соответствует имя:

    if (captives[3]) {
        return {
            id: captives[3],
            alphameric: true,
            line_nr,
            column_nr,
            column_to: rx_token.lastIndex
        };
    }

Соответствует числовой литерал:

    if (captives[4]) {
        return {
            id: "(number)",
            readonly: true,
            number: big_float.normalize(big_float.make(captives[4])),
            text: captives[4],
            line_nr,
            column_nr,
            column_to: rx_token.lastIndex
        };
    }

Соответствует текстовый литерал:

    if (captives[5]) {

Метод .replace используется для преобразования \u{xxxxxx} в кодовую точку, а JSON.parse — для обработки оставшихся эскейп-символов и кавычек:

        return {
            id: "(text)",
            readonly: true,