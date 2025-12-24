---
source_image: page_261.png
page_number: 261
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.23
tokens: 6233
characters: 1575
timestamp: 2025-12-24T10:07:57.279794
finish_reason: stop
---

Таким образом, мы теперь с вами научились полностью управлять отладчиком Chrome из удаленного расположения, приостанавливать и возобновлять сценарии, получать консольный вывод и делать многие другие полезные вещи.

Отладка в PhantomJS

Аналогично Chrome, PhantomJS тоже может использоваться для удаленной отладки. Но в этом случае удаленная машина может быть бездисплейной или вы можете запустить PhantomJS локально без необходимости запускать отдельный экземпляр браузера с его собственным отдельным профилем.

К сожалению, вы не сможете непосредственно взаимодействовать с веб-приложением, запущенным в браузере PhantomJS. Однако, вы сможете перемещаться по коду приложения и взаимодействовать с ним программно с помощью PhantomJS-сценария. Таким образом, удаленная отладка с использованием PhantomJS наиболее полезна для программируемой отладки.

Ниже приведена команда для настройки последней версии PhantomJS (2.0 на момент написания этих строк):

% phantomjs -remote-debugger-port=9000 ./loader.js <webapp URL>

В данной команде loader.js — это сценарий PhantomJS, который просто загружает ваш URL и ждет:

// Открываем страницу из командной строки PhantomJS
var page = new WebPage();
page.onError = function (msg, trace) {
    console.log(msg);
    trace.forEach(function(item) {
        console.log(' ', item.file, ':', item.line);
    })
}
page.open(phantom.args[0], function (status) {
    // Проверяем, успешно ли загружена страница
    if (status !== "success") {
        console.log("Нет доступа к сети");
    } else {
        setInterval(function() {}, 200000);