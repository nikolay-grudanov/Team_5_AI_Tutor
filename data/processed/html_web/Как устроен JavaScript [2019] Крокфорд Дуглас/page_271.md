---
source_image: page_271.png
page_number: 271
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.08
tokens: 7383
characters: 1750
timestamp: 2025-12-24T10:00:56.208733
finish_reason: stop
---

В результате 1 становится $1, 98.6 преобразуется в $98_6, а -1.011e-5 — в $_1_011e_5.

    const text = big_float.string(number.number);
    const name = "$" + text.replace(rx_minus_point, "_");
    if (unique[name] !== true) {
        unique[name] = true;
        front_matter.push(
            "const " + name + " = $NEO.number(\\" + text + "\");\n"
        );
    }
    return name;
}

Большинство генераторов кода — это простые функции, преобразующие лексемы обратно в текст. Для превращения всех частей в текст они вызывают друг друга. Начнем с функции op, принимающей лексему оператора. Она выдает преобразованную форму оператора. Многие операторы придерживаются весьма простой схемы, поэтому их преобразованными формами являются строки. Если у лексемы есть прикрепленные операнды, то составляется вызов функции. Для операторов, не соответствующих данной схеме, преобразованием является функция, принимающая лексему и возвращающая строку.

function op(thing) {
    const transform = operator_transform[thing.id];
    return (
        typeof transform === "string"
        ? (
            thing.zeroth === undefined
            ? transform
            : transform + "(" + expression(thing.zeroth) + (
                thing.wunth === undefined
                ? ""
                : ", " + expression(thing.wunth)
            ) + ")"
        )
        : transform(thing)
    );
}

Функция expression обрабатывает лексемы выражений общего вида.

function expression(thing) {
    if (thing.id === "(number)") {
        return numgle(thing);
    }
    if (thing.id === "(text)") {
        return JSON.stringify(thing.text);
    }
    if (thing.alphameric) {
        return (
            thing.origin === undefined
            ? primordial[thing.id]
