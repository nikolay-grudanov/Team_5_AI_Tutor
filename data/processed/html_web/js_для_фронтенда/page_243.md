---
source_image: page_243.png
page_number: 243
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.13
tokens: 6114
characters: 990
timestamp: 2025-12-24T10:07:32.883127
finish_reason: stop
---

function getIterator(countBy, startAt, upTill) {
    countBy = countBy || 1;
    startAt = startAt || 0;
    upTill = upTill || 100;
    var current = startAt;
    return function() {
        current += countBy;
        return (current > upTill) ? NaN : current;
    };
}

Данная простая функция создает итератор. Следующий код демонстрирует его использование:

var q = getIterator(10, 0, 200);
console.log(q());

Теперь отладим эту функцию в Firebug и взглянем на стек, как показано на рис. 7.4. На панели Стек вызовов появится функция с именем (?), то есть по сути анонимная. Так вот, чтобы задать имя для анонимной функции, вы можете использовать свойство displayName анонимной функции:

function getIterator(countBy, startAt, upTill) {
    countBy = countBy || 1;
    startAt = startAt || 0;
    upTill = upTill || 100;
    var current = startAt
        , ret = function() {

![Скриншот Firebug с отображением анонимных функций](../images/7_4.png)

Рис. 7.4. Анонимные функции в Firebug