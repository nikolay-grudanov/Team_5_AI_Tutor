---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.43
tokens: 7355
characters: 1650
timestamp: 2025-12-24T09:56:46.723469
finish_reason: stop
---

function фабрика (параметры фабрики) {

    Инициализация состояния генератора

    return function генератор (параметры генератора) {

        обновление состояния

        return значение;
    };
}

Разумеется, вариантов может быть множество. Состояние генератора надежно хранится в переменных фабрики.

Простейший полезный экземпляр такого шаблона — фабрика constant. Она получает значение, а возвращает генератор, который всегда возвращает это же значение:

function constant(value) {
    return function constant_generator() {
        return value;
    };
}

Более полезный экземпляр — фабрика integer. Она возвращает генератор, возвращающий при каждом вызове следующее целочисленное значение последовательности. В конце последовательности возвращается значение undefined. Оно служит сигналом о ее окончании.

function integer(from = 0, to = Number.MAX_SAFE_INTEGER, step = 1) {
    return function () {
        if (from < to) {
            const result = from;
            from += step;
            return result;
        }
    };
}

Фабрика element получает массив, а возвращает генератор, возвращающий при каждом вызове элемент этого массива. Когда элементы заканчиваются, возвращается значение undefined. Фабрика может получать второй необязательный аргумент — генератор, выдающий номера элементов, использующиеся для извлечения самих элементов. По умолчанию поочередно извлекаются все элементы.

function element(array, gen = integer(0, array.length)) {
    return function element_generator(...args) {
        const element_nr = gen(...args);
        if (element_nr !== undefined) {
            return array[element_nr];
        }
    };
}