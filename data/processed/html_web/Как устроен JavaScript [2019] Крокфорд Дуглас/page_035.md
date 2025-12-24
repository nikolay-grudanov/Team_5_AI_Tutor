---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.75
tokens: 7412
characters: 1710
timestamp: 2025-12-24T09:54:40.740171
finish_reason: stop
---

let result = new Array(mega + 1).fill(radix - 1);
result[sign] = plus;
let leftover = nr_bits - (mega * log2_radix);
if (leftover > 0) {
    result.push((1 << leftover) - 1);
}
return mint(result);
}

function not(a, nr_bits) {
    return xor(a, mask(nr_bits));
}

Функция random создает произвольное (случайное) большое целое число. Она получает количество генерируемых разрядов, а также необязательную функцию генератора случайных чисел, возвращающую числа между 0 и 1. Если функция генератора случайных чисел не передается, используется функция Math.random, подходящая для того, чтобы достичь большинства поставленных целей, но только не для криптографических приложений:

function random(nr_bits, random = Math.random) {

Создание строки случайных разрядов. Если решаются вопросы обеспечения безопасности, этой функции можно передать более серьезный генератор случайных чисел.

Сначала создается строка единичных разрядов:

const wuns = mask(nr_bits);
if (wuns !== undefined) {

Для каждой мегацифры берется случайное число между 0.0 и 1.0. Затем берется часть верхних разрядов и часть нижних разрядов и над ними проводится операция xor. Далее с помощью операции and формируется мегацифра, которая помещается в новое число:

return mint(wuns.map(function (element, element_nr) {
    if (element_nr === sign) {
        return plus;
    }
    const bits = random();
    return ((bits * radix_squared) ^ (bits * radix)) & element;
})));
}

Сложение выполняется так же, как это делалось в школе, за исключением того, что вместо основания 10 используется основание 16 777 216. Чтобы сделать перенос доступным сумматору, применяется замкнутое выражение:

function add(augend, addend) {
    if (is_zero(augend)) {