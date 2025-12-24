---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.09
tokens: 7344
characters: 1651
timestamp: 2025-12-24T10:01:05.466581
finish_reason: stop
---

29.2 Как работает среда выполнения

Массивы в качестве ключей используют только большие числа с плавающей запятой.

    let element_nr = big_float.number(key);
    if (!Number.isSafeInteger(element_nr)) {
        return fail("set");
    }

Отрицательные индексы — это альтернативный способ доступа, поэтому применение [ -1 ] приводит к установке на последний элемент.

    if (element_nr < 0) {
        element_nr = container.length + element_nr;
    }

Ключ должен находиться в выделенном для массива диапазоне.

    if (element_nr < 0 || element_nr >= container.length) {
        return fail("set");
    }
    container[element_nr] = value;
} else {
    if (big_float.is_big_float(key)) {
        key = big_float.string(key);
    }
}

Если ключ представляет собой строковое значение, значит, это обновление объекта.

    if (typeof key === "string") {
        if (value === undefined) {
            delete container[key];
        } else {
            container[key] = value;
        }
    } else {

В противном случае это обновление weakmap-коллекции. Это будет weakmap-коллекция, связанная с каждой записью с помощью ключей в виде объектов. Следует заметить, что, когда ключом является массив, выражение typeof key !== "object" вычисляется в false.

    if (typeof key !== "object") {
        return fail("set");
    }
    let weakmap = weakmap_of_weakmaps.get(container);

Если же weakmap-коллекции, связанной с этим контейнером, еще нет, то она создается.

    if (weakmap === undefined) {
        if (value === undefined) {
            return;
        }
        weakmap = new WeakMap();
        weakmap_of_weakmaps.set(container, weakmap);
    }