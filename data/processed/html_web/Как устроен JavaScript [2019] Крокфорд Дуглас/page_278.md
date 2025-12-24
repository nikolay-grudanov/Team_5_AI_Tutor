---
source_image: page_278.png
page_number: 278
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.65
tokens: 7269
characters: 1471
timestamp: 2025-12-24T10:00:52.084881
finish_reason: stop
---

28.10 Как работает генерация кода

Пример

Эта функция аналогична методу map, но работает и с несколькими массивами, скалярами и генераторами.

export f function, arguments... {
    if length(arguments) = 0
        return null
    var index: 0
    def result: []
    var stop: false

    def prepare arguments: f argument {
        def candidate: (
            array?(argument)
            ? argument[index]
            ! (
                function?(argument)
                ? argument(index)
                ! argument
            )
        )
        if candidate = null
            let stop: true
        return candidate
    }
    loop
        var processed: array(arguments, prepare arguments)
        if stop
            break
        let result[]: function(processed...)
        let index: index + 1
        return result
    }

А это содержимое файла с расширением .js, произведенного с использованием codegen(parse(tokenize(neo_source))):

import $NEO from "./neo.runtime.js";
const $0 = $NEO.number("0");
const $1 = $NEO.number("1");

export default $NEO.stone(function ($function, ...$arguments) {
    if ($NEO.eq($NEO.length($arguments), $0)) {
        return undefined;
    }
    var index = $0;
    var result = [];
    var stop = false;
    var prepare_arguments = $NEO.stone(function (argument) {
        var candidate = (
            Array.isArray(argument)
            ? $NEO.get(argument, index)
            : (
                $NEO.function_(argument)