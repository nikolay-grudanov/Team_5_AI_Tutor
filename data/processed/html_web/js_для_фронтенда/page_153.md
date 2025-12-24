---
source_image: page_153.png
page_number: 153
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.59
tokens: 6229
characters: 1537
timestamp: 2025-12-24T10:05:45.585384
finish_reason: stop
---

}
});
// Создаем новый узел
var item = Y.Node.create('<div id="testresults"></div>');
item.setContent(data);
// Добавляем к документу
Y.one('body').append(item);
});
}, '1.0', { requires: [ 'console', 'node' ] });
Вы поняли, в чем фокус? Вместо того чтобы записывать все данные в console.log, мы сохраняем все сообщения, полученные от YUI Test, в массив. По завершении тестов мы создаем <div> с определенным ID и выводим JSON-версию всех сообщений и результатов. Наконец, мы добавляем этот новый элемент к текущему документу. Отметим два наиболее важных момента: во-первых, <div> должен быть видимым, а во-вторых, мы должны экранировать все содержимое результирующей JSON-строки, так как вывод в формате JUnit XML — это непривычно, непривычен XML. При этом мы не хотим, чтобы браузер анализировал такое содержимое, иначе оно будет потеряно как недопустимый HTML.

Теперь давайте посмотрим на другую половину, чтобы понять, как все это совместить воедино. Рассмотрим клиентскую часть Selenium:

var webdriverjs = require("webdriverjs")
    , url = '...'
    , browser = webdriverjs.remote({
        host: 'localhost'
        , port: 4444
        , desiredCapabilities: { browserName: 'firefox' }
    })
;
browser.init().url(url).waitFor('#testresults', 10000, function(found) {
    var res;
    if (found) {
        res = browser.getText('#testresults',
            function(text) {
                // Сделаем что-то большее, нежели console.log
                console.log(JSON.parse(unescape(text.value)));
            }
        );
    }