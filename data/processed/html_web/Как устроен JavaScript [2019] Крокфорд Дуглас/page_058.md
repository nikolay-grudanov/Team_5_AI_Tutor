---
source_image: page_058.png
page_number: 58
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.74
tokens: 7329
characters: 1667
timestamp: 2025-12-24T09:55:14.329757
finish_reason: stop
---

5.1 Как работают большие рациональные числа

Эти обстоятельства допускают применение весьма привлекательных способов выполнения арифметических действий. Можно выстраивать их реализацию на основе использования больших целых чисел:

import big_integer from "./big_integer.js";

Начнем с некоторых предикатных функций:

function is_big_rational(a) {
    return (
        typeof a === "object"
        && big_integer.is_big_integer(a.numerator)
        && big_integer.is_big_integer(a.denominator)
    );
}

function is_integer(a) {
    return (
        big_integer.eq(big_integer.wun, a.denominator)
        || big_integer.is_zero(
            big_integer.divrem(a.numerator, a.denominator)[1]
        )
    );
}

function is_negative(a) {
    return big_integer.is_negative(a.numerator);
}

А это константы, которые я счел полезными. Можно без особого труда определить дополнительные константы:

function make_big_rational(numerator, denominator) {
    const new_big_rational = Object.create(null);
    new_big_rational.numerator = numerator;
    new_big_rational.denominator = denominator;
    return Object.freeze(new_big_rational);
}
const zero = make_big_rational(big_integer.zero, big_integer.wun);
const wun = make_big_rational(big_integer.wun, big_integer.wun);
const two = make_big_rational(big_integer.two, big_integer.wun);

Понадобятся также функции абсолютного значения и отрицания. В соответствии с соглашением знак определяется числителем. Знаменатель всегда положительное число.

function neg(a) {
    return make(big_integer.neg(a.numerator), a.denominator);
}

function abs(a) {
    return (
        is_negative(a)
        ? neg(a)
        : a
    );
}