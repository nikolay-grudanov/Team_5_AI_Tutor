---
source_image: page_247.png
page_number: 247
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.33
tokens: 7428
characters: 1792
timestamp: 2025-12-24T10:00:23.079350
finish_reason: stop
---

valueOf, но я не хочу его наследовать, поскольку может создаться видимость добавления к языку исходного метода valueOf.

const primordial = (function (ids) {
    const result = Object.create(null);
    ids.forEach(function (id) {
        result[id] = Object.freeze({
            id,
            alphameric: true,
            readonly: true
        });
    });
    return Object.freeze(result);
}([
    "abs", "array", "array?", "bit and", "bit mask", "bit or", "bit shift own",
    "bit shift up", "bit xor", "boolean?", "char", "code", "false", "fraction",
    "function?", "integer", "integer?", "length", "neg", "not", "number",
    "number?", "null", "record", "record?", "stone", "stone?", "text", "text?",
    "true"
]));

Свойство readonly блокирует инструкцию let.

По мере продвижения по потоку всегда будут видны три лексемы.

Поток объектов-лексем предоставляется функцией-генератором. Три лексемы видны как prev_token, token и next_token. Функция advance использует генератор для циклического прохождения через все объекты-лексемы, пропуская комментарии.

let the_token_generator;
let prev_token;
let token;
let next_token;

let now_function;      // Текущая обрабатываемая функция.
let loop;              // Массив состояния выхода из цикла.

const the_end = Object.freeze({
    id: "(end)",
    precedence: 0,
    column_nr: 0,
    column_to: 0,
    line_nr: 0
});

Функция advance выполняет переход к следующей лексеме. Ее партнерская функция prelude пытается разделить текущую лексему на две лексемы:

function advance(id) {

Переход к следующей лексеме с помощью генератора лексем. Если предоставлен идентификатор id, нужно убедиться, что текущая лексема соответствует ему:

    if (id !== undefined && id !== token.id) {
        return error(token, "expected '" + id + "'");