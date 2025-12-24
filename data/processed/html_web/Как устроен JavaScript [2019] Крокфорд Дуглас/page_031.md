---
source_image: page_031.png
page_number: 31
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.07
tokens: 7315
characters: 1419
timestamp: 2025-12-24T09:54:28.752124
finish_reason: stop
---

При наличии функции lt будет легче выполнить другие сравнения путем дополнений и перестановок:

function ge(a, b) {
    return !lt(a, b);
}

function gt(a, b) {
    return lt(b, a);
}

function le(a, b) {
    return !lt(b, a);
}

Теперь создадим функции поразрядной обработки. Каждое из больших целых чисел содержит разряды. Мы будем исходить из того, что знаки не имеют никакого отношения к поразрядным операциям, поэтому игнорируются во входных данных, а в выходных данных игнорируется знак «+».

Нашими первыми поразрядными функциями станут and, or и xor. Для функции and желательно предусмотреть обработку самого короткого массива. Лишние слова в более длинном массиве ей неинтересны. Лишние слова обнуляются и стираются. Функциям or и xor требуется работа с самым длинным массивом.

function and(a, b) {

Превращение a в самый короткий массив:

    if (a.length > b.length) {
        [a, b] = [b, a];
    }
    return mint(a.map(function (element, element_nr) {
        return (
            element_nr === sign
                ? plus
                : element & b[element_nr]
        );
    }));

function or(a, b) {

Превращение a в самый длинный массив:

    if (a.length < b.length) {
        [a, b] = [b, a];
    }
    return mint(a.map(function (element, element_nr) {
        return (
            element_nr === sign
                ? plus
                : element | (b[element_nr] || 0)
        );
    }));