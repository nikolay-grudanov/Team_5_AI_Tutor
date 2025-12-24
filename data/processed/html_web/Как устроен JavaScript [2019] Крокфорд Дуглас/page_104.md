---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.72
tokens: 7326
characters: 1585
timestamp: 2025-12-24T09:56:12.885120
finish_reason: stop
---

9.12 Как работают строки

Функция fulfill не очень большая:

const rx_delete_default = /[ < > & % " \\ ]/g;
const rx_syntactic_variable = /
    \{
        (
            [^ { } : \s ]+
        )
        (?:
            :
            (
                [^ { } : \s ]+
            )
        )?
    \}
/g;

// Определение групп:
//    [0] исходник (символическая переменная, заключенная в фигурные скобки)
//    [1] путь
//    [2] система кодирования

function default_encoder(replacement) {
    return String(replacement).replace(rx_delete_default, "");
}

export default Object.freeze(function fulfill(
    string,
    container,
    encoder = default_encoder
) {

Функция fulfill получает строку, содержащую символические переменные, функцию-генератор, или объект, или массив со значениями для замены символических переменных, и необязательную функцию кодировщика или объект, содержащий функции-кодировщики. Кодировщик, используемый по умолчанию, убирает все угловые скобки.

Основную часть работы выполняет принадлежащий string метод replace, который находит символические переменные, представляя их в виде исходной подстроки, строки пути и необязательной строки системы кодирования:

return string.replace(
    rx_syntactic_variable,
    function (original, path, encoding = "") {
        try {

Он использует путь для получения одиночной замены из контейнера значений. Путь содержит одно или несколько имен (или чисел), разделенных точками:

let replacement = (
    typeof container === "function"
    ? container
    : path.split(".").reduce(
        function (refinement, element) {