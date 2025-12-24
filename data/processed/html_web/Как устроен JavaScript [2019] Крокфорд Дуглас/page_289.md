---
source_image: page_289.png
page_number: 289
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.97
tokens: 7174
characters: 1131
timestamp: 2025-12-24T10:01:11.348213
finish_reason: stop
---

return (
    big_float.is_big_float(a)
    ? big_float.fraction(a)
    : undefined
);
}

function integer(a) {
    return (
        big_float.is_big_float(a)
        ? big_float.integer(a)
        : undefined
    );
}

function neg(a) {
    return (
        big_float.is_big_float(a)
        ? big_float.neg(a)
        : undefined
    );
}

Далее идет группа поразрядных функций. Их работа выполняется с использованием big_integer:

function bitand(a, b) {
    return big_float.make(
        big_integer.and(
            big_float.integer(a).coefficient,
            big_float.integer(b).coefficient
        ),
        big_integer.wun
    );
}

function bitdown(a, nr_bits) {
    return big_float.make(
        big_integer.shift_down(
            big_float.integer(a).coefficient,
            big_float.number(nr_bits)
        ),
        big_integer.wun
    );
}

function bitmask(nr_bits) {
    return big_float.make(big_integer.mask(big_float.number(nr_bits)));
}

function bitor(a, b) {
    return big_float.make(
        big_integer.or(
            big_float.integer(a).coefficient,
            big_float.integer(b).coefficient