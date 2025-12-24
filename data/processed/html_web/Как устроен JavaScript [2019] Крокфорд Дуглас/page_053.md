---
source_image: page_053.png
page_number: 53
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.68
tokens: 7284
characters: 1392
timestamp: 2025-12-24T09:55:03.469374
finish_reason: stop
---

// [2] frac
// [3] exp

function make(a, b) {

    // (big_integer)
    // (big_integer, exponent)
    // (string)
    // (string, radix)
    // (number)

    if (big_integer.is_big_integer(a)) {
        return make_big_float(a, b || 0);
    }
    if (typeof a === "string") {
        if (Number.isSafeInteger(b)) {
            return make(big_integer.make(a, b), 0);
        }
        let parts = a.match(number_pattern);
        if (parts) {
            let frac = parts[2] || "";
            return make(
                big_integer.make(parts[1] + frac),
                (Number(parts[3]) || 0) - frac.length
            );
        }
    }
}

Если работа ведется с числом, оно принимает вид числа с экспонентой с основанием 2 и мантиссой, а затем реконструируется в виде точного числа с плавающей точкой:

    if (typeof a === "number" && Number.isFinite(a)) {
        if (a === 0) {
            return zero;
        }
        let {sign, coefficient, exponent} = deconstruct(a);
        if (sign < 0) {
            coefficient = -coefficient;
        }
        coefficient = big_integer.make(coefficient);

Если экспонента имеет отрицательное значение, можно выполнить деление на 2 ** abs(exponent):

    if (exponent < 0) {
        return normalize(div(
            make(coefficient, 0),
            make(big_integer.power(big_integer.two, -exponent), 0),
            b
        ));
    }