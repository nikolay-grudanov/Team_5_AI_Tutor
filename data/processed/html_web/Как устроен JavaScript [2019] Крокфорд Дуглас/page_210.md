---
source_image: page_210.png
page_number: 210
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.77
tokens: 7244
characters: 1326
timestamp: 2025-12-24T09:59:04.228170
finish_reason: stop
---

23.9 Как работает тестирование

if (
    !Array.isArray(array)
    || array.length < 1
    || (
        weights !== undefined
        && (!Array.isArray(weights) || array.length !== weights.length)
    )
) {
    throw new Error("JSCheck wun_of");
}
if (weights === undefined) {
    return function () {
        return resolve(array[Math.floor(Math.random() * array.length)]);
    };
}
const total = weights.reduce(function (a, b) {
    return a + b;
});
let base = 0;
const list = weights.map(function (value) {
    base += value;
    return base / total;
});
return function () {
    let x = Math.random();
    return resolve(array[list.findIndex(function (element) {
        return element >= x;
    })]);
};

Спецификатор sequence принимает массив значений и генераторов и возвращает генератор, выдающий эти значения по порядку:

function sequence(seq) {
    seq = resolve(seq);
    if (!Array.isArray(seq)) {
        throw "JSCheck sequence";
    }
    let element_nr = -1;
    return function () {
        element_nr += 1;
        if (element_nr >= seq.length) {
            element_nr = 0;
        }
        return resolve(seq[element_nr]);
    };
}

Спецификатор falsy возвращает генератор, выдающий лживые значения:

const bottom = [false, null, undefined, "", 0, NaN];

function falsy() {
    return wun_of(bottom);
}