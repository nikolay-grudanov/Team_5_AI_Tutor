---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.47
tokens: 7385
characters: 1691
timestamp: 2025-12-24T09:59:18.662127
finish_reason: stop
---

23.15 Как работает тестирование

    color: jsc.wun_of(["black", "white", "red", "blue", "green", "gray"])
});

my_little_other_constructor() // {"left": 305, "top": 360, "color": "gray"}
my_little_other_constructor() // {"left": 162, "top": 366, "color": "blue"}
my_little_other_constructor() // {"left": 110, "top": 5, "color": "blue"}
my_little_other_constructor() // {"left": 610, "top": 61, "color": "green"}

Можно составить множество тестовых данных. Но если есть некая форма данных, которую трудно создать путем составления этих спецификаторов, можно легко создать собственные спецификаторы. Спецификатор — просто функция, которая возвращает функцию.

А теперь приступим к работе с JSCheck.

Функция crunch перемалывает числа и подготавливает отчеты:

const ctp = "{name}: {class}{cases} cases tested, {pass} pass{fail}{lost}\n";

function crunch(detail, cases, serials) {

Прохождение через все примеры; сбор всех неудачных примеров; создание подробного отчета и сводных данных:

let class_fail;
let class_pass;
let class_lost;
let case_nr = 0;
let lines = "";
let losses = [];
let next_case;
let now_claim;
let nr_class = 0;
let nr_fail;
let nr_lost;
let nr_pass;
let report = "";
let the_case;
let the_class;
let total_fail = 0;
let total_lost = 0;
let total_pass = 0;

function generate_line(type, level) {
    if (detail >= level) {
        lines += fulfill(
            " {type} [{serial}] {classification}{args}\n",
            {
                type,
                serial: the_case.serial,
                classification: the_case.classification,
                args: JSON.stringify(
                    the_case.args
                ).replace(
                    /^\\[/,