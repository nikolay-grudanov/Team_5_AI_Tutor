---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.41
tokens: 7270
characters: 1398
timestamp: 2025-12-24T09:54:59.801831
finish_reason: stop
---

```javascript
if (is_zero(divisor)) {
    return undefined;
}
let {coefficient, exponent} = dividend;
exponent -= divisor.exponent;

Масштабируем мантиссу до нужной точности:

if (typeof precision !== "number") {
    precision = number(precision);
}
if (exponent > precision) {
    coefficient = big_integer.mul(
        coefficient,
        big_integer.power(big_integer.ten, exponent - precision)
    );
    exponent = precision;
}
let remainder;
[coefficient, remainder] = big_integer.divrem(
    coefficient,
    divisor.coefficient
);

Округляем результат, если это необходимо:

if (!big_integer.abs_lt(
    big_integer.add(remainder, remainder),
    divisor.coefficient
)) {
    coefficient = big_integer.add(
        coefficient,
        big_integer.signum(dividend.coefficient)
    );
}
return make_big_float(coefficient, exponent);
}

Большое число с плавающей точкой нормализовано, если экспонента максимально приблизилась к нулю без потери значимости:

function normalize(a) {
    let {coefficient, exponent} = a;
    if (coefficient.length < 2) {
        return zero;
    }
}

Если экспонента равна нулю, значит, число уже нормализовано:

if (exponent !== 0) {

Если экспонента — положительное число, выполняется умножение мантиссы на 10 ** экспоненты:

if (exponent > 0) {
    coefficient = big_integer.mul(
        coefficient,
        big_integer.power(big_integer.ten, exponent)
```