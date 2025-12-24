---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.70
tokens: 7260
characters: 1356
timestamp: 2025-12-24T09:54:38.343416
finish_reason: stop
---

3.14 Как работают большие целые числа

Выполняем подготовку для следующего разряда. Обновляем dividend_prefix с использованием первых двух слов оставшегося делимого dividend и уменьшаем делитель divisor:

    if (is_zero(dividend)) {
        break;
    }
    dividend_prefix = last(dividend) * radix + next_to_last(dividend);
    divisor = shift_down(divisor, 24);
}

Исправляем остаток:

    quotient = mint(quotient);
    remainder = shift_down(dividend, shift);
    return [
        (
            quotient_is_negative
            ? neg(quotient)
            : quotient
        ),
        (
            remainder_is_negative
            ? neg(remainder)
            : remainder
        )
    ];

function div(dividend, divisor) {
    let temp = divrem(dividend, divisor);
    if (temp) {
        return temp[0];
    }
}

Возведение целого числа в целочисленную степень сводится к простому использованию квадрата числа и метода умножения:

    function power(big, exponent) {
        let exp = int(exponent);
        if (exp === 0) {
            return wun;
        }
        if (is_zero(big)) {
            return zero;
        }
        if (exp === undefined || exp < 0) {
            return undefined;
        }
        let result = wun;
        while (true) {
            if ((exp & 1) !== 0) {
                result = mul(result, big);
            }