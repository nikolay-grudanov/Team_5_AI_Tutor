---
source_image: page_050.png
page_number: 50
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.16
tokens: 7426
characters: 1921
timestamp: 2025-12-24T09:55:13.856791
finish_reason: stop
---

4.3 Как работают большие числа с плавающей точкой

    op(
        big_integer.mul(
            a.coefficient,
            big_integer.power(big_integer.ten, -differential)
        ),
        b.coefficient
    ),
    b.exponent
)
    : make_big_float(
        op(
            a.coefficient,
            big_integer.mul(
                b.coefficient,
                big_integer.power(big_integer.ten, differential)
            )
        ),
        a.exponent
    )
);
}
const add = conform_op(big_integer.add);
const sub = conform_op(big_integer.sub);

Умножение реализуется еще проще. Мы просто перемножаем мантиссы и складываем экспоненты:

function mul(multiplicand, multiplier) {
    return make_big_float(
        big_integer.mul(multiplicand.coefficient, multiplier.coefficient),
        multiplicand.exponent + multiplier.exponent
    );
}

Сложность деления заключается в том, чтобы не ошибиться с моментом остановки. Проще всего остановиться в целочисленном делении. Остановка выполняется, когда заканчиваются цифры. Также просто определить момент остановки, работая с числами с плавающей точкой, имеющими фиксированный размер. Остановка выполняется, когда заканчиваются разряды, но при работе с большими целыми числами такие ограничения отсутствуют. Деление может продолжаться до нахождения точного результата, но нет никакой гарантии, что его получится достичь. Так что оставим все это на усмотрение программиста. Функция div получает необязательный третий аргумент, указывающий на точность результата. Указывается место десятичной точки. Младший разряд (разряд единиц) находится на нулевой позиции. Дробные позиции выражены отрицательными числами. Деление возвращает как минимум столько знаков после точки, сколько было указано. По умолчанию используется значение -4, то есть четыре цифры после точки:

function div(dividend, divisor, precision = -4) {
    if (is_zero(dividend)) {
        return zero;
    }