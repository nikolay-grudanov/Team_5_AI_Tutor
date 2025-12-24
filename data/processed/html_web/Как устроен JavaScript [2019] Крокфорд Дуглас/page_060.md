---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.68
tokens: 7357
characters: 1641
timestamp: 2025-12-24T09:55:20.396028
finish_reason: stop
---

5.3 Как работают большие рациональные числа

    big_integer.mul(multiplicand.numerator, multiplier.numerator),
    big_integer.mul(multiplicand.denominator, multiplier.denominator)
    );
}

function div(a, b) {
    return make(
        big_integer.mul(a.numerator, b.denominator),
        big_integer.mul(a.denominator, b.numerator)
    );
}

function remainder(a, b) {
    const quotient = div(normalize(a), normalize(b));
    return make(
        big_integer.divrem(quotient.numerator, quotient.denominator)[1]
    );
}

function reciprocal(a) {
    return make(a.denominator, a.numerator);
}

function integer(a) {
    return (
        a.denominator === wun
            ? a
            : make(big_integer.div(a.numerator, a.denominator), big_integer.wun)
    );
}

function fraction(a) {
    return sub(a, integer(a));
}

Функция нормализации normalize сокращает дробь, избавляя ее от общих множителей. Разложение на множители больших чисел — весьма непростая задача. К счастью, нам не нужно выполнять разложение на множители для операции сокращения. Следует просто найти наибольший общий делитель, на который затем и выполняется сокращение.

Фактически нормализация не нужна. Значение в результате нормализации не изменяется. Большие целые числа внутри рационального объекта могут быть уменьшены, и это способно сократить потребность в памяти (что редко играет важную роль) и ускорить выполнение последующих арифметических операций.

function normalize(a) {

Нормализация большого рационального числа выполняется делением двух его компонентов на наибольший общий делитель (НОД). Если НОД равен единице, значит, число уже нормализовано: