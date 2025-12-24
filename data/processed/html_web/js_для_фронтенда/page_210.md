---
source_image: page_210.png
page_number: 210
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.03
tokens: 5990
characters: 686
timestamp: 2025-12-24T10:06:34.459074
finish_reason: stop
---

Глава 6. Интеграционное, нагрузочное и тестирование производительности

А что насчет скриншота?

var casper = require('casper').create();
casper.start('http://search.yahoo.com/', function() {
    this.fill('form#sf', { "p": 'JavaScript' }, false);
    this.click('#yschbt');
});
casper.then(function() {
    this.capture('results.png', {
        top: 0,
        left: 0,
        width: 1024,
        height: 768
    });
    this.test.assertExists('#resultCount', 'Got result count');
});
casper.run(function() {
    this.exit();
});

![Скриншот страницы Yahoo! с результатами поиска по запросу "javascript"](../images/chapter6_2.png)

Рис. 6.2. Создание снимка экрана с помощью CasperJS