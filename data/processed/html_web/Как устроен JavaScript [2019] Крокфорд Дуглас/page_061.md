---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.36
tokens: 7307
characters: 1508
timestamp: 2025-12-24T09:55:14.089565
finish_reason: stop
---

let {numerator, denominator} = a;
if (big_integer.eq(big_integer.wun, denominator)) {
    return a;
}
    let g_c_d = big_integer.gcd(numerator, denominator);
    return (
        big_integer.eq(big_integer.wun, g_c_d)
    ? a
    : make(
        big_integer.div(numerator, g_c_d),
        big_integer.div(denominator, g_c_d)
    )
);
}

Чтобы определить равенство двух значений, нормализация не понадобится. Если:

\[
a / b = c / d
\]

то:

\[
a * d = b * c
\]

даже если они не нормализованы.

function eq(comparahend, comparator) {
    return (
        comparahend === comparator
        ? true
        : (
            big_integer.eq(comparahend.denominator, comparator.denominator)
            ? big_integer.eq(comparahend.numerator, comparator.numerator)
            : big_integer.eq(
                big_integer.mul(comparahend.numerator, comparator.denominator),
                big_integer.mul(comparator.numerator, comparahend.denominator)
            )
        )
    );
}

function lt(comparahend, comparator) {
    return (
        is_negative(comparahend) !== is_negative(comparator)
        ? is_negative(comparator)
        : is_negative(sub(comparahend, comparator))
    );
}

Функция make принимает два аргумента и создает объект, содержащий числитель numerator и знаменатель denominator. Преобразование выполняется с абсолютной точностью.

Функция принимает одно или два больших целых числа, а также строки вида "33 1/3" и "98.6" и выполняет их правильное преобразование. Она также принимает