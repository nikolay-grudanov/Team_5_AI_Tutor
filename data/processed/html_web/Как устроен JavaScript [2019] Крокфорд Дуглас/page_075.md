---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.38
tokens: 7487
characters: 1844
timestamp: 2025-12-24T09:55:36.701234
finish_reason: stop
---

Если продолжить, то кажется, что на четвертом, пятом и шестом смысл несколько теряется, но со временем, когда наименьшие целые числа останутся позади, станет яснее, каким было начало отсчета.

**Инициализация**

Новый массив можно создать двумя способами:

• указав литерал массива;
• применив выражение new Array(целочисленное_значение).

let my_little_array = new Array(10).fill(0);
    // получился my_little_array вида [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
let same_thing = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

my_little_array === same_thing                // false

Обратите внимание на то, что my_little_array и same_thing абсолютно одинаковы. Но они также являются двумя отдельными, уникальными значениями. В отличие от строк, но подобно объектам, идентичные массивы считаются равными только в том случае, если это фактически один и тот же массив.

**Стеки и очереди**

У массивов есть методы, которые ведут себя с массивом как со стеком. Метод pop удаляет последний элемент массива и возвращает его значение. Метод push добавляет к массиву новый элемент.

Стеки зачастую используются в интерпретаторах и калькуляторах.

function make_binary_op(func) {
    return function (my_little_array) {
        let wunth = my_little_array.pop();
        let zeroth = my_little_array.pop();
        my_little_array.push(func(zeroth, wunth));
        return my_little_array;
    };
}

let addop = make_binary_op(function (zeroth, wunth) {
    return zeroth + wunth;
});

let mulop = make_binary_op(function (zeroth, wunth) {
    return zeroth * wunth;
});

let my_little_stack = [];           // my_little_stack имеет значение []
my_little_stack.push(3);            // my_little_stack имеет значение [3]
my_little_stack.push(5);            // my_little_stack имеет значение [3, 5]
my_little_stack.push(7);            // my_little_stack имеет значение [3, 5, 7]