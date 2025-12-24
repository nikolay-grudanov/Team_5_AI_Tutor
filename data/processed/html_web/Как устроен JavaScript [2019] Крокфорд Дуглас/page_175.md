---
source_image: page_175.png
page_number: 175
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.24
tokens: 7259
characters: 1458
timestamp: 2025-12-24T09:58:14.511338
finish_reason: stop
---

optional_array,
time_limit,
time_option,
throttle,
factory_name = "parallel"
}

Фабрика parallel самая сложная из этих фабрик. Она может принимать второй массив запросчиков, получающих более щадящую политику сбоев. И возвращает запросчик, создающий массив значений:

let number_of_required;
let requestor_array;

Возможны четыре варианта, поскольку как массив required_array, так и массив optional_array может быть пустым:

if (required_array === undefined || required_array.length === 0) {
    number_of_required = 0;
    if (optional_array === undefined || optional_array.length === 0) {
Если оба массива пустые, то это, вероятно, ошибка:

throw make_reason(
    factory_name,
    "Missing requestor array.",
    required_array
);
}
}
Если присутствует только optional_array, то он становится requestor_array:

requestor_array = optional_array;
time_option = true;
} else {

Если имеется только required_array, то этот массив становится requestor_array:

number_of_required = required_array.length;
if (optional_array === undefined || optional_array.length === 0) {
    requestor_array = required_array;
    time_option = undefined;
}
Если предоставлены оба массива, мы их объединяем:

} else {
    requestor_array = required_array.concat(optional_array);
    if (time_option !== undefined && typeof time_option !== "boolean") {
        throw make_reason(
            factory_name,
            "Bad time_option.",
            time_option
        );
    }
}