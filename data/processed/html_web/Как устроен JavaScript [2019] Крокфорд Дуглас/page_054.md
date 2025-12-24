---
source_image: page_054.png
page_number: 54
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.91
tokens: 7377
characters: 1647
timestamp: 2025-12-24T09:55:14.329671
finish_reason: stop
---

4.7 Как работают большие числа с плавающей точкой

Если экспонента больше нуля, мантиссу можно умножить на 2 ** экспоненты:

    if (exponent > 0) {
        coefficient = big_integer.mul(
            coefficient,
            big_integer.power(big_integer.two, exponent)
        );
        exponent = 0;
    }
    return make(coefficient, exponent);
}
if (is_big_float(a)) {
    return a;
}

Функция string преобразует большое число с плавающей точкой в строку. Преобразование выполняется с абсолютной точностью. Основная часть работы заключается во вставке десятичного знака и заполнении нулевых позиций. Аналогичная функция для двоичной плавающей точки была бы значительно сложнее.

function string(a, radix) {
    if (is_zero(a)) {
        return "0";
    }
    if (is_big_float(radix)) {
        radix = normalize(radix);
        return (
            (radix && radix.exponent === 0)
            ? big_integer.string(integer(a).coefficient, radix.coefficient)
            : undefined
        );
    }
    a = normalize(a);
    let s = big_integer.string(big_integer.abs(a.coefficient));
    if (a.exponent < 0) {
        let point = s.length + a.exponent;
        if (point <= 0) {
            s = "0".repeat(1 - point) + s;
            point = 1;
        }
        s = s.slice(0, point) + "." + s.slice(point);
    } else if (a.exponent > 0) {
        s += "0".repeat(a.exponent);
    }
    if (big_integer.is_negative(a.coefficient)) {
        s = "-" + s;
    }
    return s;
}

Существует два соглашения по представлению десятичного знака: в виде точки (.) и в виде запятой (,). В большинстве стран используется один из этих знаков. В преде-