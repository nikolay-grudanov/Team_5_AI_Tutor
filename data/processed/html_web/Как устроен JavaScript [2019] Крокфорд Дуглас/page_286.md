---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.98
tokens: 7214
characters: 1115
timestamp: 2025-12-24T10:01:11.176447
finish_reason: stop
---

29.6 Как работает среда выполнения

return big_float.is_big_float(any);
}

function record_(any) {
    return (
        any !== null
        && typeof any === "object"
        && !big_float.is_big_float(any)
    );
}

function text_(any) {
    return typeof any === "string";
}

Далее следует группа логических функций. Есть и functino-версии. Они не выполняют короткозамкнутые вычисления. На «ленивое» вычисление своих операндов способны только версии в форме операторов.

function assert_boolean(boolean) {
    return (
        typeof boolean === "boolean"
        ? boolean
        : fail("boolean")
    );
}

function and(zeroth, wunth) {
    return assert_boolean(zeroth) && assert_boolean(wunth);
}

function or(zeroth, wunth) {
    return assert_boolean(zeroth) || assert_boolean(wunth);
}

function not(boolean) {
    return !assert_boolean(boolean);
}

function ternary(zeroth, wunth, twoth) {
    return (
        assert_boolean(zeroth)
        ? wunth
        : twoth
    );
}

function default_function(zeroth, wunth) {
    return (
        zeroth === undefined
        ? wunth
        : zeroth
    );
}