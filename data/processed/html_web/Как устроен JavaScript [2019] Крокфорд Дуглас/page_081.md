---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.80
tokens: 7341
characters: 1597
timestamp: 2025-12-24T09:55:36.271755
finish_reason: stop
---

Преобразование каждого ключа в массив строк:

    const paths = keys.map(function (element) {
        return element.toString().split(".");
    });

Сравнение каждой пары значений, пока не будет найдено несоответствие — если несоответствия не будет, значит, два значения равны:

    return function compare(first, second) {
        let first_value;
        let second_value;
        if (paths.every(function (path) {
            first_value = refine(first, path);
            second_value = refine(second, path);
            return first_value === second_value;
        })) {
            return 0;
        }
    }

Если два значения относятся к одному и тому же типу, мы сможем сравнить их. Если типы разные, то нужна некая политика, позволяющая справиться со странностями. Нашей простой политикой будет сравнение имен типов по принципу boolean < number < string < undefined. (Возможно, было бы лучше отказаться от сортировки элементов, не совпадающих по типу.)

    return (
        (
            typeof first_value === typeof second_value
            ? first_value < second_value
            : typeof first_value < typeof second_value
        )
        ? -1
        : 1
    );
}

Пример:

let people = [
    {first: "Frank", last: "Farkel"},
    {first: "Fanny", last: "Farkel"},
    {first: "Sparkle", last: "Farkel"},
    {first: "Charcoal", last: "Farkel"},
    {first: "Mark", last: "Farkel"},
    {first: "Simon", last: "Farkel"},
    {first: "Gar", last: "Farkel"},
    {first: "Ferd", last: "Berfel"}
];

people.sort(by("last", "first"));

// [
//     {"first": "Ferd", "last": "Berfel"},