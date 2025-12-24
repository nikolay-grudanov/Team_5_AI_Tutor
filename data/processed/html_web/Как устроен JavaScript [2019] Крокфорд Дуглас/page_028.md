---
source_image: page_028.png
page_number: 28
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.31
tokens: 7382
characters: 1701
timestamp: 2025-12-24T09:54:26.371858
finish_reason: stop
---

3.2 Как работают большие целые числа

return array[array.length - 1];
}
function next_to_last(array) {
    return array[array.length - 2];
}

Создадим несколько констант. В них нет насущной потребности, но код с ними будет проще читаться:

const zero = Object.freeze([plus]);
const wun = Object.freeze([plus, 1]);
const two = Object.freeze([plus, 2]);
const ten = Object.freeze([plus, 10]);
const negative_wun = Object.freeze([minus, 1]);

Для обнаружения как положительных, так и отрицательных больших целых чисел нам нужны предикативные функции:

function is_big_integer(big) {
    return Array.isArray(big) && (big[sign] === plus || big[sign] === minus);
}

function is_negative(big) {
    return Array.isArray(big) && big[sign] === minus;
}

function is_positive(big) {
    return Array.isArray(big) && big[sign] === plus;
}

function is_zero(big) {
    return !Array.isArray(big) || big.length < 2;
}

Функция mint удаляет последние слова из массива, если они нулевые. При наличии соответствия она выполняет подстановку одной из констант. Если соответствия нет, массив замораживается. Если позволить изменять массивы, то в некоторых случаях реализация могла бы работать быстрее, но тогда она усложнится и станет способна допускать больше ошибок. Наши большие целые числа неизменяемые, как и числа JavaScript:

function mint(proto_big_integer) {

Создание большого целого числа из его прототипа. Удаление лидирующих нулевых мегацифр. Подстановка по возможности популярных констант:

while (last(proto_big_integer) === 0) {
    proto_big_integer.length -= 1;
}
if (proto_big_integer.length <= 1) {
    return zero;
}
if (proto_big_integer[sign] === plus) {
    if (proto_big_integer.length === 2) {