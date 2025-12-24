---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.75
tokens: 7167
characters: 892
timestamp: 2025-12-24T09:54:47.540622
finish_reason: stop
---

Подсчет общего количества разрядов, содержащих 1:

return big.reduce(
    function (reduction, element, element_nr) {
        return reduction + (
            element_nr === sign
                ? 0
                : population_32(element)
        );
    },
    0
);

function significant_bits(big) {

Подсчет общего количества разрядов, исключая лидирующие нули:

return (
    big.length > 1
    ? make((big.length - 2) * log2_radix + (32 - Math.clz32(last(big))))
    : zero
);

И в завершение все эти полезные объекты экспортируются в виде модуля:

export default Object.freeze({
    abs,
    abs_lt,
    add,
    and,
    div,
    divrem,
    eq,
    gcd,
    is_big_integer,
    is_negative,
    is_positive,
    is_zero,
    lt,
    make,
    mask,
    mul,
    neg,
    not,
    number,
    or,
    population,
    power,
    random,
    shift_down,
    shift_up,
    significant_bits,