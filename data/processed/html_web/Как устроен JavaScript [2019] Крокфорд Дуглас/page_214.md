---
source_image: page_214.png
page_number: 214
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.12
tokens: 7441
characters: 1693
timestamp: 2025-12-24T09:59:21.096244
finish_reason: stop
---

23.13 Как работает тестирование

Он также принимает значения и генераторы, объединяя результаты.

let my_little_3_letter_word_specifier = jsc.string(
    jsc.sequence(["c", "d", "f"]),
    jsc.sequence(["a", "o", "i", "e"]),
    jsc.sequence(["t", "g", "n", "s", "l"])
]);

my_little_3_letter_word_specifier()    // "cat"
my_little_3_letter_word_specifier()    // "dog"
my_little_3_letter_word_specifier()    // "fin"
my_little_3_letter_word_specifier()    // "ces"

Если параметр создает целое число, за которым следует строковое значение, он может использоваться в качестве длины.

let my_little_ssn_specifier = jsc.string(
    3, jsc.character("0", "9"),
    "-",
    2, jsc.character("0", "9"),
    "-",
    4, jsc.character("0", "9")
);

my_little_ssn_specifier()    // "231-89-2167"
my_little_ssn_specifier()    // "706-32-0392"
my_little_ssn_specifier()    // "931-89-4315"
my_little_ssn_specifier()    // "636-20-3790"

Спецификатор any возвращает генератор, выдающий случайные значения различных типов.

const misc = [
    true, Infinity, -Infinity, falsy(), Math.PI, Math.E, Number.EPSILON
];

function any() {
    return wun_of([integer(), number(), string(), wun_of(misc)]);
}

Спецификатор object возвращает генератор, выдающий объекты. По умолчанию создаются небольшие объекты со случайными ключами и случайными значениями.

function object(subject, value) {
    if (subject === undefined) {
        subject = integer(1, 4);
    }
    return function () {
        let result = {};
        const keys = resolve(subject);
        if (typeof keys === "number") {
            const text = string();
            const gen = any();
            let i = 0;
            while (i < keys) {