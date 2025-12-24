---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.67
tokens: 7295
characters: 1354
timestamp: 2025-12-24T09:54:35.573473
finish_reason: stop
---

3.10 Как работают большие целые числа

return addend;
}
if (is_zero(addend)) {
    return augend;
}

Если знаки разные, код превращается в вычитание:

    if (augend[sign] !== addend[sign]) {
        return sub(augend, neg(addend));
    }

Знаки одинаковые. При сложении разрядов результату присваивается тот же знак. Можно складывать числа разной длины. К более длинному применяется метод .map, и для подстановки нулей вместо несуществующих элементов используется оператор ||:

    if (augend.length < addend.length) {
        [addend, augend] = [augend, addend];
    }
    let carry = 0;
    let result = augend.map(function (element, element_nr) {
        if (element_nr !== sign) {
            element += (addend[element_nr] || 0) + carry;
            if (element >= radix) {
                carry = 1;
                element -= radix;
            } else {
                carry = 0;
            }
        }
        return element;
    });
    if (carry > 0) {
        result.push(carry);
    }
    return mint(result);
}

Если возникает переполнение, то для возможности переноса добавляется еще один элемент:

Вычитание также не составляет труда:

function sub(minuend, subtrahend) {
    if (is_zero(subtrahend)) {
        return minuend;
    }
    if (is_zero(minuend)) {
        return neg(subtrahend);
    }
    let minuend_sign = minuend[sign];