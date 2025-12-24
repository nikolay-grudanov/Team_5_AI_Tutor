---
source_image: page_285.png
page_number: 285
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.73
tokens: 7225
characters: 1291
timestamp: 2025-12-24T10:01:05.451026
finish_reason: stop
---

return (zeroth.slice(big_float.number(wunth), big_float.number(twoth)));
}
if (big_float.is_big_float(zeroth)) {
    return big_float.string(zeroth, wunth);
}
if (Array.isArray(zeroth)) {
    let separator = wunth;
    if (typeof wunth !== "string") {
        if (wunth !== undefined) {
            return fail("string");
        }
        separator = "";
    }
    return zeroth.join(separator);
}
if (typeof zeroth === "boolean") {
    return String(zeroth);
}
}

Функция stone выполняет глубокую заморозку:

function stone(object) {
    if (!Object.isFrozen(object)) {
        object = Object.freeze(object);
        if (typeof object === "object") {
            if (Array.isArray(object)) {
                object.forEach(stone);
            } else {
                Object.keys(object).forEach(function (key) {
                    stone(object[key]);
                });
            }
        }
    }
    return object;
}

Теперь группа функций-предикатов, используемых для идентификации типов:

function boolean_(any) {
    return typeof any === "boolean";
}

function function_(any) {
    return typeof any === "function";
}

function integer_(any) {
    return (
        big_float.is_big_float(any)
        && big_float.normalize(any).exponent === 0
    );
}

function number_(any) {