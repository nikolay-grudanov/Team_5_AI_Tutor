---
source_image: page_144.png
page_number: 144
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.57
tokens: 6202
characters: 1411
timestamp: 2025-12-24T10:05:25.095486
finish_reason: stop
---

Как только вы все установите, выполнение ваших YUI-тестов через PhantomJS превратится в довольно простое занятие, но есть один нюанс. Наше связующее звено в виде HTML-файла требует небольших изменений:

<html>
<head>
    <title>Тест суммы</title>
</head>
<body class="yui3-skin-sam">
    <div id="log"></div>
    <script src="http://yui.yahooapis.com/3.18.1/build/yui/yui-min.js"></script>
    <script src="sum.js"></script>
    <script src="phantomOutput.js"></script>
    <script src="sumTests.js"></script>
</body>
</html>

Обратите внимание, что в этом случае загружается другой JavaScript-файл — phantomOutput.js, который определяет небольшой YUI-модуль phantomjs:

YUI().add('phantomjs', function(Y) {
    var TR;
    if (typeof(console) !== 'undefined') {
        TR = Y.Test.Runner;
        TR.subscribe(TR.COMPLETE_EVENT, function(obj) {
            console.log(Y.Test.Format.JUnitXML(obj.results));
        });
    }
});

Единственная цель этого модуля заключается в выводе на консоль результатов теста в формате XML JUnit после завершения тестов (YUI поддерживает и другие форматы вывода, которые можно использовать вместо формата XML JUnit). Вы вольны использовать тот формат, который понимает ваш инструмент сборки. Мой, например, Hudson/Jenkins понимает формат XML JUnit, поэтому я и использую его. Эта зависимость должна быть задекларирована в вашем тестовом файле. Рассмотрим sumTests.js:

YUI({