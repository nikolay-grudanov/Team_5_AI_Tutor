---
source_image: page_126.png
page_number: 126
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.87
tokens: 7387
characters: 1989
timestamp: 2025-12-24T09:57:03.149149
finish_reason: stop
---

13.5 Как работают генераторы

значения от первого генератора, пока тот не выдаст значение undefined, затем переключается на следующий генератор. Фабрика concat использует показанную ранее фабрику element, чтобы распорядиться генераторами должным образом.

function concat(...generators) {
    const next = element(generators);
    let generator = next();
    return function concat_generator(...args) {
        if (generator !== undefined) {
            const value = generator(...args);
            if (value === undefined) {
                generator = next();
                return concat_generator(...args);
            }
            return value;
        }
    };
}

Фабрика join получает функцию от одного или нескольких генераторов, возвращая новый генератор. При каждом вызове нового генератора вызываются все прежние генераторы и их результаты передаются функции. Фабрику join можно использовать с repeat для выполнения всех действий, которые вы привыкли делать с применением конструкции for of. Функциональный аргумент для join выполняет действия, запрограммированные в блоке. Фабрика join способна работать одновременно с потоками нескольких генераторов.

function join(func, ...gens) {
    return function join_generator() {
        return func(...gens.map(function (gen) {
            return gen();
        }));
    };
}

Всем этим можно воспользоваться для создания функции map, работающей наподобие array-метода map. Она получает функцию и массив, а возвращает новый массив, в каждом элементе которого содержится результат вызова функции в отношении каждого элемента массива.

function map(array, func) {
    return harvest(join(func, element(array)));
}

Фабрика objectify предоставляет еще один способ конструирования объектов данных.

function objectify(...names) {
    return function objectify_constructor(...values) {
        const object = Object.create(null);
        names.forEach(function (name, name_nr) {
            object[name] = values[name_nr];
        });
