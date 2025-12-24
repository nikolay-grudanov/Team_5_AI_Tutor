---
source_image: page_212.png
page_number: 212
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.83
tokens: 7333
characters: 1663
timestamp: 2025-12-24T09:59:13.625781
finish_reason: stop
---

23.11 Как работает тестирование

Спецификатор character возвращает генератор, выдающий символы. Если ему передается целое число или два числа, генератор создает символы, чьи кодовые точки входят в указанный диапазон. Если ему передаются две строки, он возвращает символы в диапазоне, составленном из первой кодовой точки каждой строки. Если передается одна строка, он возвращает символы из нее. По умолчанию возвращаются ASCII-символы:

function character(i, j) {
    if (i === undefined) {
        return character(32, 126);
    }
    if (typeof i === "string") {
        return (
            j === undefined
                ? wun_of(i.split(""))
                : character(i.codePointAt(0), j.codePointAt(0))
        );
    }
    const ji = integer(i, j);
    return function () {
        return String.fromCodePoint(ji());
    };
}

Спецификатор array возвращает генератор, выдающий массивы:

function array(first, value) {
    if (Array.isArray(first)) {
        return function () {
            return first.map(resolve);
        };
    }
    if (first === undefined) {
        first = integer(4);
    }
    if (value === undefined) {
        value = integer();
    }
    return function () {
        const dimension = resolve(first);
        const result = new Array(dimension).fill(value);
        return (
            typeof value === "function"
                ? result.map(resolve)
                : result
        );
    };
}

Если аргументом является массив значений и генераторов, результатом становится массив, содержащий значения и результаты работы генераторов:

let my_little_array_specifier = jsc.array([
    jsc.integer(),
    jsc.number(100),