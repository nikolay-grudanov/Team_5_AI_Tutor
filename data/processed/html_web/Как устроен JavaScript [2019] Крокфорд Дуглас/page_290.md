---
source_image: page_290.png
page_number: 290
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.70
tokens: 7297
characters: 1379
timestamp: 2025-12-24T10:01:12.847259
finish_reason: stop
---

29.10    Как работает среда выполнения

),
    big_integer.wun
);
}

function bitup(a, nr_bits) {
    return big_float.make(
        big_integer.shift_up(
            big_float.integer(a).coefficient,
            big_float.number(nr_bits)
        ),
        big_integer.wun
    );
}

function bitxor(a, b) {
    return big_float.make(
        big_integer.xor(
            big_float.integer(a).coefficient,
            big_float.integer(b).coefficient
        ),
        big_integer.wun
    );
}

Возможно, вы помните из JSCheck указатель на функцию (functino) \( f() \):

function resolve(value, ...rest) {
    return (
        typeof value === "function"
        ? value(...rest)
        : value
    );
}

Имеются также два оператора конкатенации. Оба они возвращают null, если значение null имеет один из аргументов. В противном случае они предпринимают попытку приведения своих аргументов к текстам. Если оба операнда не являются пустым текстом, указатель на функцию \( f \approx \) включает разделитель в виде пробела.

function cat(zeroth, wunth) {
    zeroth = text(zeroth);
    wunth = text(wunth);
    if (typeof zeroth === "string" && typeof wunth === "string") {
        return zeroth + wunth;
    }
}

function cats(zeroth, wunth) {
    zeroth = text(zeroth);
    wunth = text(wunth);
    if (typeof zeroth === "string" && typeof wunth === "string") {
        return (