---
source_image: page_287.png
page_number: 287
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.86
tokens: 7228
characters: 1208
timestamp: 2025-12-24T10:01:11.909601
finish_reason: stop
---

А это группа операторов отношений:

function eq(zeroth, wunth) {
    return zeroth === wunth || (
        big_float.is_big_float(zeroth)
        && big_float.is_big_float(wunth)
        && big_float.eq(zeroth, wunth)
    );
}

function lt(zeroth, wunth) {
    return (
        zeroth === undefined
        ? false
        : (
            wunth === undefined
            ? true
            : (
                (
                    big_float.is_big_float(zeroth)
                    && big_float.is_big_float(wunth)
                )
                ? big_float.lt(zeroth, wunth)
                : (
                    (typeof zeroth === typeof wunth &&
                        typeof zeroth === "string"
                        || typeof zeroth === "number")
                    ? zeroth < wunth
                    : fail("lt")
                )
            )
        )
    );
}

function ge(zeroth, wunth) {
    return !lt(zeroth, wunth);
}

function gt(zeroth, wunth) {
    return lt(wunth, zeroth);
}

function le(zeroth, wunth) {
    return !lt(wunth, zeroth);
}

function ne(zeroth, wunth) {
    return !eq(wunth, zeroth);
}

Теперь группа арифметических операторов:

function add(a, b) {
    return (