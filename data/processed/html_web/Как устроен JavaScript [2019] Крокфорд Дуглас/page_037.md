---
source_image: page_037.png
page_number: 37
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.82
tokens: 7337
characters: 1538
timestamp: 2025-12-24T09:54:42.474302
finish_reason: stop
---

Если знаки разные, код превращается в сложение:

    if (minuend_sign !== subtrahend[sign]) {
        return add(minuend, neg(subtrahend));
    }

Вычитание меньшего из большего:

    if (abs_lt(minuend, subtrahend)) {
        [subtrahend, minuend] = [minuend, subtrahend];
        minuend_sign = (
            minuend_sign === minus
            ? plus
            : minus
        );
    }
    let borrow = 0;
    return mint(minuend.map(function (element, element_nr) {
        if (element_nr === sign) {
            return minuend_sign;
        }
        let diff = element - ((subtrahend[element_nr] || 0) + borrow);
        if (diff < 0) {
            diff += 16777216;
            borrow = 1;
        } else {
            borrow = 0;
        }
        return diff;
    }));

Умножение несколько сложнее. Мы используем вложенные функции forEach, поскольку нужно перемножить каждый элемент multiplicand с каждым элементом multiplier. Каждое из этих произведений может быть 48-разрядным, но в элементе могут содержаться только 24 разряда, поэтому переполнение должно быть перенесено:

function mul(multiplicand, multiplier) {
    if (is_zero(multiplicand) || is_zero(multiplier)) {
        return zero;
    }
}

Если знаки совпадают, знак результата будет «+»:

    let result = [
        multiplicand[sign] === multiplier[sign]
        ? plus
        : minus
    ];

Перемножение каждого элемента multiplicand с каждым элементом multiplier с распространением переноса:

    multiplicand.forEach(function (
        multiplicand_element,