---
source_image: page_209.png
page_number: 209
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.05
tokens: 6270
characters: 1710
timestamp: 2025-12-24T10:06:50.153764
finish_reason: stop
---

Конечно, если вы захотите протестировать ваш код в Internet Explorer, вам придется использовать Selenium. Но CasperJS — хорошее дополнение в вашем наборе инструментов «полировки» вашего кода для быстрого тестирования в бездисплейной среде.

Чтобы использовать CasperJS, сначала нужно установить последнюю версию PhantomJS, которую можно получить с сайта https://code.google.com/p/phantomjs/downloads/list. Проще всего загрузить уже откомпилированную бинарную версию для вашей операционной системы. Самостоятельная компиляция из исходного кода довольно трудна и нужна в редких случаях (например, если у вас старая версия Linux или же вам нужно отключить SSE-оптимизацию и т.д.).

Получить последнюю версию CasperJS (1.1 на данный момент) можно с сайта http://casperjs.org/.

Далее приводится CasperJS-версия приведенного ранее теста для поисковика Yahoo!:

    var casper = require('casper').create();
    casper.start('http://search.yahoo.com/', function() {
        this.fill('form#sf', { "p": 'JavaScript' }, false);
        this.click('#yschbt');
    });
    casper.then(function() {
        this.test.assertExists('#resultCount', 'Got result count');
    });
    casper.run(function() {
        this.exit();
    });

Теперь давайте разберемся, как запустит этот сценарий CasperJS:

    % bin/casperjs yahooSearch.js
    PASS Got result count
    %

Как видите, все очень просто. И это значительно быстрее соединения с удаленным сервером Selenium, с его порождением и уничтожением браузера. Все это работает в реальном WebKit-браузере, но учтите, что версия WebKit, используемая Apple в Safari, и версия WebKit, которая используется Google в Chrome, отличаются от той, которая запускается здесь в PhantomJS.