---
source_image: page_049.png
page_number: 49
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.34
tokens: 7370
characters: 1772
timestamp: 2025-12-24T09:55:06.961809
finish_reason: stop
---

Как работают большие числа с плавающей точкой

Функция number превращает большое число с плавающей точкой в число JavaScript. Если число выходит за пределы безопасной зоны целых чисел, точность преобразования не гарантируется. Попробуем также разобраться с другими типами.

function number(a) {
    return (
        is_big_float(a)
        ? (
            a.exponent === 0
            ? big_integer.number(a.coefficient)
            : big_integer.number(a.coefficient) * (10 ** a.exponent)
        )
        : (
            typeof a === "number"
            ? a
            : (
                big_integer.is_big_integer(a)
                ? big_integer.number(a)
                : Number(a)
            )
        )
    );
}

Нам нужны функция абсолютного значения и функция смены знака:

function neg(a) {
    return make_big_float(big_integer.neg(a.coefficient), a.exponent);
}

function abs(a) {
    return (
        is_negative(a)
        ? neg(a)
        : a
    );
}

Сложение и вычитание даются легко: мы просто складываем мантиссы, но только при одинаковых экспонентах. Если экспоненты неодинаковы, их нужно привести в соответствие. Поскольку сложение и вычитание очень похожи, я создал функцию, выполняющую как функцию сложения, так и функцию вычитания. Если функции conform_op передать аргумент bi.add, получится функция сложения чисел с плавающей точкой. А если ей передать аргумент bi.sub, получится функция вычитания чисел с плавающей точкой:

function conform_op(op) {
    return function (a, b) {
        const differential = a.exponent - b.exponent;
        return (
            differential === 0
            ? make_big_float(op(a.coefficient, b.coefficient), a.exponent)
            : (
                differential < 0
                ? make_big_float(
