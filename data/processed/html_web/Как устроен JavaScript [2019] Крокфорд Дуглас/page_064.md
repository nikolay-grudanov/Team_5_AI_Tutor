---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.72
tokens: 7318
characters: 1584
timestamp: 2025-12-24T09:55:24.389159
finish_reason: stop
---

5.7 Как работают большие рациональные числа

let frac = parts[5] || "";
let exp = (Number(parts[6]) || 0) - frac.length;
if (exp < 0) {
    return make(
        parts[1] + parts[2] + frac,
        big_integer.power(big_integer.ten, -exp)
    );
}
return make(
    big_integer.mul(
        big_integer.make(parts[1] + parts[2] + parts[5]),
        big_integer.power(big_integer.ten, exp)
    ),
    big_integer.wun
);

Аргумент является числом? Тогда оно подвергается разбору и реконструкции.

if (typeof numerator === "number" && !Number.isSafeInteger(numerator)) {
    let {sign, coefficient, exponent} = deconstruct(numerator);
    if (sign < 0) {
        coefficient = -coefficient;
    }
    coefficient = big_integer.make(coefficient);
    if (exponent >= 0) {
        return make(
            big_integer.mul(
                coefficient,
                big_integer.power(big_integer.two, exponent)
            ),
            big_integer.wun
        );
    }
    return normalize(make(
        coefficient,
        big_integer.power(big_integer.two, -exponent)
    ));
}
return make(numerator, big_integer.wun);

Функция number преобразует большое рациональное число в число JavaScript. Преобразование не гарантирует абсолютную точность, если число находится за пределами безопасной целочисленной зоны:

function number(a) {
    return big_integer.number(a.numerator) / big_integer.number(a.demoninator);
}

Функция string преобразует большое рациональное число в строку. Преобразование выполняется с абсолютной точностью:

function string(a, nr_places) {
    if (a === zero) {