---
source_image: page_152.png
page_number: 152
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.68
tokens: 6218
characters: 1557
timestamp: 2025-12-24T10:05:41.886690
finish_reason: stop
---

В этом HTML используются относительные пути для указания тестируемого файла/модуля: user_view.js. При открытии этого HTML на веб-сервере будут найдены все необходимые файлы. Используя npm-пакет webdriverjs, мы можем легко отправить URL на сервер Selenium для выполнения:

var webdriverjs = require("webdriverjs")
, url = '...';
browser = webdriverjs.remote({
    host: 'localhost'
    , port: 4444
    , desiredCapabilities: { browserName: 'firefox' }
});
browser.init().url(url).end();

Данный код свяжется с сервером Selenium, запущенным на 4444-ом порту узла localhost, и попросит его запустить Firefox и загрузить указанный URL. Половина дела сделана! Теперь нам нужно захватить вывод теста — те самые полезные сообщения, выводимые YUI Test. Кроме того, мы хотим захватить снимок экрана и сохранить его локально.

Как и в случае с PhantomJS, мы должны так или иначе передать весь вывод (результаты теста, сообщения журнала, снимки экрана) обратно драйверу Selenium. В отличие от PhantomJS, Selenium не может удаленно считать консоль, поэтому нам нужно действовать иначе. Рассмотрим эквивалент модулю phantomjs для Selenium:

YUI().add('selenium', function(Y) {
    var messages = [];
    , yconsole = new Y.Console();
    yconsole.on('entry', function(obj) { messages.push(obj.message); });
    var TR = Y.Test.Runner;
    TR.subscribe(TR.COMPLETE_EVENT, function(obj) {
        // Данные для дампа
        var data = escape(JSON.stringify(
            {
                messages: messages
                , results: Y.Test.Format.JUnitXML(obj.results)
