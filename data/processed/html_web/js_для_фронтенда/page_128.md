---
source_image: page_128.png
page_number: 128
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.40
tokens: 6193
characters: 1328
timestamp: 2025-12-24T10:05:09.496941
finish_reason: stop
---

, testSimple: function () {
    Y.Assert.areSame(sum(2, 2), 4
    , '2 + 2 не равно 4?');
}
});
// Загружаем его
Y.Test.Runner.add(testCase);
(new Y.Test.Console({
    newestOnTop: false
})).render('#log');
// Запускаем его
Y.Test.Runner.run();
});

Это самый простой тест, который только возможен. Первым делом мы создаем новый тестовый сценарий Y.Test.Case. При создании теста мы задаем его имя (name) и набор функций, которые мы будем тестировать. Каждая функция выполняется поочередно. Тестовый сценарий загружается в локальный объект Y.Test.Runner, и затем выполняются все тесты.

У нас есть код, который нужно протестировать, и мы должны написать сценарий самого теста. Далее мы должны запустить созданные тесты и просмотреть результаты. Если бы мы тестировали только код стороны сервера (например, используя платформу Vows), нам был бы нужен только код и соответствующий ему тест. Но поскольку мы тестируем клиентский код JavaScript, нам нужен еще HTML-файл, который свяжет воедино файл с исходным кодом (sum.js) и файл теста (sumTest.js):

<html>
<head>
    <title>Test Sum</title>
</head>
<body>
    <div id='log' class='yui3-skin-sam'></div>
    <script src='http://yui.yahooapis.com/3.18.1/build/yui/yui-min.js'>
    </script>
    <script src='sum.js'></script>
    <script src='sumTests.js'></script>
</body>
</html>