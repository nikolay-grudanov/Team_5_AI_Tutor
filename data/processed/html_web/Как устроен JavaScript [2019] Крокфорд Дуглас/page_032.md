---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.83
tokens: 7284
characters: 1611
timestamp: 2025-12-24T09:54:33.441585
finish_reason: stop
---

3.6 Как работают большие целые числа

function xor(a, b) {
    Превращение а в самый длинный массив:
        if (a.length < b.length) {
            [a, b] = [b, a];
        }
        return mint(a.map(function (element, element_nr) {
            return (
                element_nr === sign
                    ? plus
                    : element ^ (b[element_nr] || 0)
            );
        }));
}

Некоторые функции получают в качестве аргумента малое целое число. Функция int упрощает работу как с числами, так и с большими целыми числами:

function int(big) {
    let result;
    if (typeof big == "number") {
        if (Number.isSafeInteger(big)) {
            return big;
        }
    } else if (is_big_integer(big)) {
        if (big.length < 2) {
            return 0;
        }
        if (big.length === 2) {
            return (
                is_negative(big)
                    ? -big[least]
                    : big[least]
            );
        }
        if (big.length === 3) {
            result = big[least + 1] * radix + big[least];
            return (
                is_negative(big)
                    ? -result
                    : result
            );
        }
        if (big.length === 4) {
            result = (
                big[least + 2] * radix_squared
                + big[least + 1] * radix
                + big[least]
            );
            if (Number.isSafeInteger(result)) {
                return (
                    is_negative(big)
                        ? -result
                        : result
                );
            }
        }
    }
}