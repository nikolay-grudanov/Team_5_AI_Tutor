---
source_image: page_270.png
page_number: 270
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.16
tokens: 7389
characters: 1628
timestamp: 2025-12-24T10:00:52.039144
finish_reason: stop
---

28.2 Как работает генерация кода

    indentation += 4;
}
function outdent() {
    indentation -= 4;
}
function begin() {
В начале каждой строки вставляются перевод строки и пробельное заполнение.
    return "\n" + " ".repeat(indentation);
}
let front_matter;
let operator_transform;
let statement_transform;
let unique;

Соглашения относительно использования имен в Neo и JavaScript не полностью совместимы. В Neo, в отличие от JavaScript, разрешены пробелы и вопросительные знаки. Поэтому при необходимости имена Neo коверкают, превращая в допустимые имена JavaScript. Neo допускает любые слова, но JavaScript некоторые из них резервирует. Когда в Neo применяется слово, зарезервированное в JavaScript, к этому слову при перемещении его в пространство JavaScript добавляется знак доллара. Чтобы программы легче читались, большие десятичные числа с плавающей запятой преобразуют в форму, напоминающую числовые литералы.

const rx_space_question = / [ \u0020 ? ]/g;

function mangle(name) {
В идентификаторах JavaScript не разрешены пробел или знак вопроса (?), поэтому их заменяют символом подчеркивания (_). Зарезервированным словам дается префикс в виде знака доллара ($).

Таким образом, what me worry? превращается в what_me_worry_, а class — в $class.

return (
    reserved[name] === true
    ? "$" + name
    : name.replace(rx_space_question, "_")
);
}

const rx_minus_point = / [ \- . ] /g;

function numgle(number) {

Литералам больших десятичных чисел придают как можно более естественный вид путем превращения их в константы. Имя константы начинается с символа $. Символы - или . заменяют символом подчеркивания (_).