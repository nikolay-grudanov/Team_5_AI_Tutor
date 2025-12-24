---
source_image: page_052.png
page_number: 52
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.91
tokens: 7304
characters: 1350
timestamp: 2025-12-24T09:55:03.708428
finish_reason: stop
---

4.5 Как работают большие числа с плавающей точкой

);
    exponent = 0;
} else {
    let quotient;
    let remainder;

Если же экспонента — отрицательное число, а мантисса делится на 10, выполняется деление и к экспоненте добавляется единица.

Чтобы ускорить эту работу, сначала попробуем взять из младших разрядов блоки по 10 000 000, убирая сразу семь нулей:

    while (exponent <= -7 && (coefficient[1] & 127) == 0) {
        [quotient, remainder] = big_integer.divrem(
            coefficient,
            big_integer_ten_million
        );
        if (remainder != big_integer.zero) {
            break;
        }
        coefficient = quotient;
        exponent += 7;
    }
    while (exponent < 0 && (coefficient[1] & 1) == 0) {
        [quotient, remainder] = big_integer.divrem(
            coefficient,
            big_integer.ten
        );
        if (remainder != big_integer.zero) {
            break;
        }
        coefficient = quotient;
        exponent += 1;
    }
}
return make_big_float(coefficient, exponent);

Функция make получает большое целое число, или строку, или число JavaScript и преобразует его в большое число с плавающей точкой. Преобразование выполняется с абсолютной точностью:

const number_pattern = /
    ^
    ( -? \d+ )
    (?: \. ( \d* ) )?
    (?: e ( -? \d+ ) )?
    $
/;
// Capturing groups
// [1] int