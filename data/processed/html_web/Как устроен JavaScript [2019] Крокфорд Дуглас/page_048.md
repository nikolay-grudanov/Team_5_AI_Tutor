---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.91
tokens: 7346
characters: 1723
timestamp: 2025-12-24T09:54:59.397295
finish_reason: stop
---

4.1 Как работают большие числа с плавающей точкой

Они возникают, если размер не ограничен. Поскольку это способно вызывать ошибки, следует по возможности избавиться от странностей.

Большие целые числа можно использовать также для экспоненты, но это будет излишним. Вполне хватит и чисел JavaScript. Гигабайты памяти были бы исчерпаны еще до того, как свойство Number.MAX_SAFE_INTEGER стало бы ограничением.

Большие числа с плавающей точкой будут представлены в виде объектов со свойствами coefficient и exponent.

После того как большие целые числа взяты на вооружение, разобраться с числами с плавающей точкой не составит особого труда:

import big_integer from "./big_integer.js";

Функция is_big_float используется для обнаружения объекта больших чисел с плавающей точкой:

function is_big_float(big) {
    return (
        typeof big === "object"
        && big_integer.is_big_integer(big.coefficient)
        && Number.isSafeInteger(big.exponent)
    );
}

function is_negative(big) {
    return big_integer.is_negative(big.coefficient);
}

function is_positive(big) {
    return big_integer.is_positive(big.coefficient);
}

function is_zero(big) {
    return big_integer.is_zero(big.coefficient);
}

Отдельное значение zero представляет все нули:

const zero = Object.create(null);
zero.coefficient = big_integer.zero;
zero.exponent = 0;
Object.freeze(zero);

function make_big_float(coefficient, exponent) {
    if (big_integer.is_zero(coefficient)) {
        return zero;
    }
    const new_big_float = Object.create(null);
    new_big_float.coefficient = coefficient;
    new_big_float.exponent = exponent;
    return Object.freeze(new_big_float);
}

const big_integer_ten_million = big_integer.make(10000000);