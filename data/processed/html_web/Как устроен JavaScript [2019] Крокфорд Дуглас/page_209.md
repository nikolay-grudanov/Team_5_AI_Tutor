---
source_image: page_209.png
page_number: 209
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.88
tokens: 7363
characters: 1605
timestamp: 2025-12-24T09:59:07.844437
finish_reason: stop
---

Ранее уже упоминалось применение literal в качестве constant. Это позволяет отключать функции, и у вас может быть функция, прошедшая все попытки:

function literal(value) {
    return function () {
        return value;
    };
}

Спецификатор boolean производит генератор, который создает булевы значения:

function boolean(bias = 0.5) {

Сигнатура способна содержать булеву спецификацию. Может быть предоставлен необязательный параметр смещения (bias). Если смещение равно 0,25, то примерно четверть произведенных булевых значений будет true:

    bias = resolve(bias);
    return function () {
        return Math.random() < bias;
    };
}

Спецификатор number, что неудивительно, производит числа в диапазоне:

function number(from = 1, to = 0) {
    from = Number(resolve(from));
    to = Number(resolve(to));
    if (from > to) {
        [from, to] = [to, from];
    }
    const difference = to - from;
    return function () {
        return Math.random() * difference + from;
    };
}

Спецификатор wun_of принимает массив значений и генераторов и возвращает генератор, выдающий эти значения случайным образом. Спецификатор wun_of может дополнительно принимать массив показателей веса, способный смещать выбор:

function wun_of(array, weights) {

У спецификатора wun_of имеется две сигнатуры:

// wun_of(array)
//    Из массива берется и разрешается один элемент.
//    Элементы выбираются случайным образом с равными вероятностями.

// wun_of(array, weights)
//    Оба аргумента являются массивами одинаковой длины.
//    Чем больше показатель веса, тем выше вероятность, что элемент будет выбран.