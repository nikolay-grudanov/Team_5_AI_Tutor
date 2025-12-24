---
source_image: page_211.png
page_number: 211
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.59
tokens: 6212
characters: 1526
timestamp: 2025-12-24T10:06:53.487601
finish_reason: stop
---

Код-«захватчик экрана» может захватить не только весь экран, но и только заданный CSS-селектор вместо захвата всей страницы.

Этот снимок экрана подобен тому, который мы получили с использованием Selenium. Наибольшее отличие заключается в размере снимка экрана: CasperJS не «снимает» всю веб-страницу, как это делает Selenium, а только «видимую» ее часть.

У CasperJS есть много разных полезных приемов. Например, давайте рассмотрим автоматический экспорт результатов тестов в файл, отформатированный как JUnit XML. Полный сценарий наш будет таким:

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
        this.test.renderResults(true, 0, 'test-results.xml');
    });

Файл test-results.xml теперь будет содержать вывод теста в формате JUnit XML. Как уже неоднократно упоминалось, этот формат хорош тем, что его понимают множество утилит сборки, включая Hudson/Jenkins. Далее приводится содержимое файла test-results.xml после запуска данного теста:

    <testsuite>
        <testcase classname="ss" name="Got result count">
            <testcase>
        </testsuite>

Вывод на консоль будет таким: