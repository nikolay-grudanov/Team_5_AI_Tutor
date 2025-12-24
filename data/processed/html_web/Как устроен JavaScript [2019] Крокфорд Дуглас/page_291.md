---
source_image: page_291.png
page_number: 291
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.23
tokens: 7136
characters: 830
timestamp: 2025-12-24T10:01:11.311940
finish_reason: stop
---

zeroth === ""
    ? wunth
    : (
        wunth === ""
        ? zeroth
        : zeroth + " " + wunth
    )
};

Далее следуют разнородные функции:

function char(any) {
    return String.fromCharCode(big_float.number(any));
}

function code(any) {
    return big_float.make(any.codePointAt(0));
}

function length(linear) {
    return (
        (Array.isArray(linear) || typeof linear === "string")
        ? big_float.make(linear.length)
        : undefined
    );
}

Все эти ценности упаковываются в объект среды выполнения:

export default stone({
    abs,
    add,
    and,
    array,
    assert_boolean,
    bitand,
    bitdown,
    bitmask,
    bitor,
    bitup,
    bitxor,
    boolean_,
    cat,
    cats,
    char,
    code,
    default: default_function,
    div,
    fail,
    fraction,
    function_,
    ge,
    get,