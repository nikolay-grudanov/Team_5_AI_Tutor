---
source_image: page_124.png
page_number: 124
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.97
tokens: 7433
characters: 1943
timestamp: 2025-12-24T09:56:54.653487
finish_reason: stop
---

13.3 Как работают генераторы

Фабрика property делает то же самое в отношении объектов. Она возвращает каждое свойство объекта в форме массива, содержащего ключ и значение. Когда свойства заканчиваются, возвращается значение undefined. Фабрика может получать второй аргумент — генератор, выдающий ключи, используемые для извлечения свойств. По умолчанию извлекаются все принадлежащие объекту свойства в том порядке, в котором они в него вставлялись.

function property(object, gen = element(Object.keys(object))) {
    return function property_generator(...args) {
        const key = gen(...args);
        if (key !== undefined) {
            return [key, object[key]];
        }
    };
}

Фабрика collect получает генератор и массив. Она возвращает генератор, работающий точно так же, как и полученный ею генератор, за исключением того, что он также добавляет в массив интересные возвращаемые значения. Все аргументы, передаваемые новой функции, передаются и старой функции.

function collect(generator, array) {
    return function collect_generator(...args) {
        const value = generator(...args);
        if (value !== undefined) {
            array.push(value);
        }
        return value;
    };
}

Функция repeat используется в качестве драйвера. Она получает функцию и вызывает ее до тех пор, пока та не возвратит значение undefined. Это единственный нужный нам цикл. Его можно написать с применением инструкции do, но я предпочитаю концевую рекурсию (см. главу 18).

function repeat(generator) {
    if (generator() !== undefined) {
        return repeat(generator);
    }
}

Для сбора данных можно воспользоваться функцией collect.

const my_array = [];
repeat(collect(integer(0, 7), my_array));
    // my_array имеет значение [0, 1, 2, 3, 4, 5, 6]

Для достижения нужного результата можно объединить функции repeat и collect. Функция harvest не является фабрикой или генератором, но получает генератор в качестве аргумента.