---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.24
tokens: 6278
characters: 1600
timestamp: 2025-12-24T10:05:37.396697
finish_reason: stop
---

Все довольно просто. Данный сценарий PhantomJS в качестве параметра принимает URL, указывающий на HTML-файл «связующего звена», загружает его и, в случае успеха, ожидает консольного вывода для захвата.

Наш сценарий просто выводит «захваченный» вывод, но вы можете перенаправить вывод этого сценария в файл, или же сценарий PhantomJS может сам записать вывод в файл при необходимости.

У PhantomJS нет доступа к JavaScript, работающему на самой загруженной странице, таким образом, мы используем консоль для передачи тестового вывода страницы, загружаемой в PhantomJS, где вывод может быть сохранен.

Запустить наш тест можно командой:

% phantomjs ~/phantomOutput.js sumTests.html

Первый параметр — это JavaScript-файл теста, а второй — «связующее звено» (HTML-файл). Вывод будет примерно таким (хотя и не так хорошо отформатированным):

<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
    <testsuite name="simple test" tests="2" failures="0" time="0.005">
        <testcase name="testIsObject" time="0"></testcase>
        <testcase name="testMessage" time="0.001"></testcase>
    </testsuite>
</testsuites>

Это и есть вывод в формате JUnit XML для двух созданных нами тестов.

Для полноты картины вы можете добавить сюда еще снимки экрана, причем сделать это довольно просто. Ниже приведен полный код тестового сценария с добавленной поддержкой снимков экрана. По сути, отличие только в том, что мы «прорисовываем» вывод после любого вывода на консоль.

var page = new WebPage();
page.viewportSize = { width: 1024, height: 768 };
page.onConsoleMessage = function(msg) {
    console.log(msg);