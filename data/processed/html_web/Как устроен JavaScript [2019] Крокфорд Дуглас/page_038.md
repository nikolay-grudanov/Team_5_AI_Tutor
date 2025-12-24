---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.06
tokens: 7360
characters: 1806
timestamp: 2025-12-24T09:54:44.911211
finish_reason: stop
---

3.12 Как работают большие целые числа

    multiplicand_element_nr
) {
    if (multiplicand_element_nr !== sign) {
        let carry = 0;
        multiplier.forEach(function (
            multiplier_element,
            multiplier_element_nr
        ) {
            if (multiplier_element_nr !== sign) {
                let at = (
                    multiplicand_element_nr + multiplier_element_nr - 1
                );
                let product = (
                    (multiplicand_element * multiplier_element)
                    + (result[at] || 0)
                    + carry
                );
                result[at] = product & 16777215;
                carry = Math.floor(product / radix);
            }
        });
        if (carry > 0) {
            result[multiplicand_element_nr + multiplier.length - 1] = carry;
        }
    }
});
return mint(result);
}

Функция divrem выполняет деление, возвращая как частное, так и остаток. Для удобства предоставим также функцию div, возвращающую только частное от деления:

function divrem(dividend, divisor) {
    if (is_zero(dividend) || abs_lt(dividend, divisor)) {
        return [zero, dividend];
    }
    if (is_zero(divisor)) {
        return undefined;
    }
}

Придадим операндам положительные значения:

let quotient_is_negative = dividend[sign] !== divisor[sign];
let remainder_is_negative = dividend[sign] === minus;
let remainder = dividend;
dividend = abs(dividend);
divisor = abs(divisor);

Выполним привычное по школьным временам деление в столбик. Оценим следующую цифру частного. Вычтем столько значений делителя, сколько получится в результате оценки делимого, а затем повторим это действие. Вместо основания 10 примем основание 16 777 216 и воспользуемся более системным подходом в прогнозировании следующей цифры частного.