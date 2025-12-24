---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.16
tokens: 6136
characters: 1254
timestamp: 2025-12-24T10:05:24.955924
finish_reason: stop
---

logInclude: { TestRunner: true },
}).use('test', 'sum', 'console', 'phantomjs', function(Y) {
    var suite = new Y.Test.Suite('sum');
    suite.add(new Y.Test.Case({
        name:'simple test',
        testIntAdd : function () {
            Y.log('testIntAdd');
            Y.Assert.areEqual(Y.MySum(2,2), 4);
        },
        testStringAdd : function () {
            Y.log('testStringAdd');
            Y.Assert.areEqual(Y.MySum('my', 'sum'), 'mysum');
        }
    }));
    Y.Test.Runner.add(suite);
    // Инициализируем консоль
    var yconsole = new Y.Console({
        newestOnTop: false
    });
    yconsole.render('#log');
    Y.Test.Runner.run();
});
PhantomJS захватит консольный вывод и сохранит его в файле для дальнейшей обработки. К сожалению, включение модуля phantomjs в наши тесты сейчас не идеально. В главе 8 мы сделаем этот процесс более динамичным.

Далее приведен сценарий PhantomJS для захвата вывода теста:

var page = new WebPage();
page.onConsoleMessage = function(msg) {
    console.log(msg);
    phantom.exit(0);
};
page.open(phantom.args[0], function (status) {
    // Проверяем, успешно ли загружена страница
    if (status !== "success") {
        console.log("Unable to load file");
        phantom.exit(1);
    }
});