---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.00
tokens: 7399
characters: 1747
timestamp: 2025-12-24T09:57:00.508193
finish_reason: stop
---

function harvest(generator) {
    const array = [];
    repeat(collect(generator, array));
    return array;
}

const result = harvest(integer(0, 7));
    // result имеет значение [0, 1, 2, 3, 4, 5, 6]

Фабрика limit получает функцию и возвращает функцию, которая может использоваться ограниченное количество раз. Когда лимит будет исчерпан, функция не будет делать ничего, кроме возвращения undefined. Второй аргумент фабрики — допустимое количество вызовов новой функции.

function limit(generator, count = 1) {
    return function (...args) {
        if (count >= 1) {
            count -= 1;
            return generator(...args);
        }
    };
}

Фабрика limit может использоваться с любой функцией. Например, если ей передать функцию, исполняющую желания, и задать лимит 3, получится функция, исполняющая три желания.

Функция filter получает генератор и функцию предиката. Так называется функция, возвращающая true или false. Она возвращает новый генератор, работающий наподобие прежнего, за исключением того, что он доставляет только значения, для которых предикат возвращает true.

function filter(generator, predicate) {
    return function filter_generator(...args) {
        const value = generator(...args);
        if (value !== undefined && !predicate(value)) {
            return filter_generator(...args);
        }
        return value;
    };
}

const my_third_array = harvest(filter(
    integer(0, 42),
    function divisible_by_three(value) {
        return (value % 3) === 0;
    }
));
    // my_third_array имеет вид [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]

Фабрика concat может получить два и более генератора и объединить их для создания генератора, сочетающего последовательность их действий. Он получает