---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.65
tokens: 7137
characters: 880
timestamp: 2025-12-24T09:59:22.904705
finish_reason: stop
---

Модуль экспортирует конструктор, возвращающий jsc-объект. Этот объект обладает состоянием, так как содержит утверждения, которые нужно тестировать, поэтому каждый пользователь должен получать свежий экземпляр.

Значение reject используется для идентификации попыток, которые следует отбросить:

const reject = Object.freeze({});

Мы экспортируем функцию jsc_constructor. Функции check и claim обладают состоянием, поэтому они здесь и создаются. Я замораживаю конструктор, поскольку мне нравится все замораживать:

export default Object.freeze(function jsc_constructor() {
    let all_claims = [];
    let nr_trials = (
        configuration.nr_trials === undefined
        ? 100

Работу выполняет функция check:

function check(configuration) {
    let the_claims = all_claims;
    all_claims = [];
    let nr_trials = (
        configuration.nr_trials === undefined
        ? 100