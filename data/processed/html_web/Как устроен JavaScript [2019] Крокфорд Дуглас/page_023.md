---
source_image: page_023.png
page_number: 23
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.77
tokens: 7356
characters: 954
timestamp: 2025-12-24T09:53:56.184044
finish_reason: stop
---

Возвращаем объект, содержащий три компонента и исходное число:

return {
    sign,
    coefficient,
    exponent,
    number
};

Теперь, имея оснащение, рассмотрим само чудовище.

Когда будет выполнен разбор Number.MAX_SAFE_INTEGER, мы получим:

{
    "sign": 1,
    "coefficient": 9007199254740991,
    "exponent": 0,
    "number": 9007199254740991
}

Number.MAX_SAFE_INTEGER — наибольшее число, помещающееся в 54-разрядное целое число со знаком.

После разбора числа 1 мы получим:

{
    "sign": 1,
    "coefficient": 9007199254740992,
    "exponent": -53,
    "number": 1
}

Заметьте, что 1 * 9007199254740992 * (2 ** -53) равняется 1.

А теперь усложним задачу и разберем число 0.1. Одну десятую. Цент:

{
    "sign": 1,
    "coefficient": 7205759403792794,
    "exponent": -56,
    "number": 0.1
}

Если вычислить 1 * 7205759403792794 * 2 ** -56, то получится значение не 0.1, а более точно: 0.100000000000000055511151231257827021181583404541015625.