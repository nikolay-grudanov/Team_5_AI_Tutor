---
source_image: page_281.png
page_number: 281
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.43
tokens: 7322
characters: 1825
timestamp: 2025-12-24T10:01:03.599588
finish_reason: stop
---

weakmap-коллекции не понадобятся, они нужны тем записям, которые действительно получают свои отображения из weakmap_of_weakmaps.

Функция get извлекает значение поля из записи или элемент из массива. В ней также путем возвращения функции реализован вызов функции в форме вызова метода. Если по какой-либо причине что-то пойдет не так, возвращается объект null, известный JavaScript как undefined.

let weakmap_of_weakmaps = new WeakMap();

function get(container, key) {
    try {
        if (Array.isArray(container) || typeof container === "string") {
            const element_nr = big_float.number(key);
            return (
                Number.isSafeInteger(element_nr)
                    ? container[(element_nr >= 0 ? element_nr : container.length + element_nr)]
                    : undefined
            );
        }
        if (typeof container === "object") {
            if (big_float.is_big_float(key)) {
                key = big_float.string(key);
            }
            return (
                typeof key === "string"
                    ? container[key]
                    : weakmap_of_weakmaps.get(container).get(key)
            );
        }
        if (typeof container === "function") {
            return function (...rest) {
                return container(key, rest);
            };
        }
    } catch (ignore) {
    }
}

Доступ к функции get можно получить через указатель на функцию, имеющий вид f[ ].

Функция set — это способ добавления, обновления или удаления поля записи или обновления элемента массива. Если что-то пойдет не так, происходит сбой. Функция get в этом смысле не слишком взыскательна, чего нельзя сказать о функции set.

function set(container, key, value) {
    if (Object.isFrozen(container)) {
        return fail("set");
    }
    if (Array.isArray(container)) {