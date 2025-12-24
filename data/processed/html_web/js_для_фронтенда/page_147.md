---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.93
tokens: 6137
characters: 1137
timestamp: 2025-12-24T10:05:27.271216
finish_reason: stop
---

setTimeout(function() {
    page.render('output.png');
    phantom.exit();
}, 500);
};
page.open(phantom.args[0], function (status) {
    // Проверяем, успешно ли загрузилась страница
    if (status !== "success") {
        console.log("Невозможно загрузить файл");
        phantom.exit(1);
    }
});
Первым делом я установил размер виртуального окна, затем получил результаты прорисовки страницы в PNG-файл. Данный сценарий генерирует снимки экрана после каждого теста. Помимо PNG-формата PhantomJS также может создавать снимки экрана в форматах PDF и JPG. На рис. 4.2 вы можете увидеть наш снимок экрана.

Toolbar Tests

![Снимок экрана PhantomJS](../images/chapter4/phantomjs_screenshot.png)

Рис. 4.2. Снимок экрана PhantomJS

Превосходно! По умолчанию фон создаваемого изображения прозрачный, но мы можем нормально просмотреть вывод YUI Test, поместив его в HTML-элемент <div id="log">.

Постойте! А что насчет некоторых сообщений, отправляемых YUI службе протоколирования? Мы тоже хотим их захватить! Для этого нам нужно снова посетить YUI-модуль phantomjs:

YUI().add('phantomjs', function(Y) {
    var yconsole = new Y.Console();