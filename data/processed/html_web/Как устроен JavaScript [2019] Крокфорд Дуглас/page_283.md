---
source_image: page_283.png
page_number: 283
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.44
tokens: 7267
characters: 1516
timestamp: 2025-12-24T10:01:08.604209
finish_reason: stop
---

Обновление weakmap-коллекции:

    if (value === undefined) {
        weakmap.delete(key);
    } else {
        weakmap.set(key, value);
    }
}

Далее следует группа функций, создающих массивы, числовые значения, записи и тексты:

function array(zeroth, wunth, ...rest) {

Функция array выполняет работу new Array, array.fill, array.slice, Object.keys, string.split и многих других:

    if (big_float.is_big_float(zeroth)) {
        const dimension = big_float.number(zeroth);
        if (!Number.isSafeInteger(dimension) || dimension < 0) {
            return fail("array");
        }
        let newness = new Array(dimension);
        return (
            (wunth === undefined || dimension === 0)
                ? newness
                : (
                    typeof wunth === "function"
                        ? newness.map(wunth)
                        : newness.fill(wunth)
                )
        );
    }
    if (Array.isArray(zeroth)) {
        return zeroth.slice(big_float.number(wunth), big_float.number(rest[0]));
    }
    if (typeof zeroth === "object") {
        return Object.keys(zeroth);
    }
    if (typeof zeroth === "string") {
        return zeroth.split(wunth || "");
    }
    return fail("array");
}

function number(a, b) {
    return (
        typeof a === "string"
            ? big_float.make(a, b)
            : (
                typeof a === "boolean"
                    ? big_float.make(Number(a))
                    : (
                        big_float.is_big_float(a)
