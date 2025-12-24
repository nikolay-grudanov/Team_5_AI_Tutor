---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.34
tokens: 6260
characters: 1654
timestamp: 2025-12-24T10:08:15.134602
finish_reason: stop
---

Использование карт кода позволяет отобразить производственный код обратно в исходный код в отладчике. В Beta-ветке браузер Chrome поддерживает карты кода "из коробки", чего не скажешь о других браузерах. Компилятор Google Closure Compiler объединяет и минимизирует код, он же может помочь с выводом карты кода для этого кода. Google также предоставляет расширение Closure Inspector, которое позволяет "научить" расширение Firebug понимать карты кода, что позволяет использовать браузер для работы и Firefox.

Давайте на примере рассмотрим процесс использования карт кода. Для этого примера мы будем использовать функцию getIterator(), с которой мы уже знакомы. Представим, что она сохранена в файле с именем iterator.js:

function getIterator(countBy, startAt, upTill) {
    countBy = countBy || 1;
    startAt = startAt || 0;
    upTill = upTill || 100;
    var current = startAt
        , ret = function() {
            current += countBy;
            return (current > upTill) ? NaN : current;
        }
    ;
    ret.displayName = "Iterator from " + startAt + " until "
        + upTill + " by " + countBy;
    return ret;
}

Как видите, здесь нет ничего необычного. Данная функция «весит» всего 406 байтов. Теперь получите последнюю версию компилятора compiler.jar с домашней страницы компилятора Google Closure Compiler. Запустите Closure Compiler, «скормив» ему наш iterator.js:

% java -jar compiler.jar --js iterator.js --js_output_file it-comp.js

Он создаст новый файл, it-comp.js:

function getIterator(a,b,c){var a=a||1,b=b||0,c=c||100,d=b,e=function(){d+=a;return d>c?NaN:d};
e.displayName="Iterator from "+b+" until "+c+" by "+a;return e;}