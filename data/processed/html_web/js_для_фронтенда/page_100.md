---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.37
tokens: 6178
characters: 1468
timestamp: 2025-12-24T10:04:33.865932
finish_reason: stop
---

Y.one('#password').set('value', password);
    Y.one('#submitButton').simulate('click');
});
});

Вышеприведенный код тестирует успешную попытку входа. Мы настраиваем наш поддельный объект Y.io и тестируем различные функции входа. Затем мы настраиваем HTML-элементы: заполняем их известными значениями, которые могут быть переданы при нажатии кнопки Submit (Отправить). Отметим функцию teardown, позволяющую восстановить объект Y.io в его исходное значение. Имитация Y.io немного неуклюжая, поскольку Ajax имеет дело только со строками, и мы должны контролировать HTTP-статус от сервера. Для полноты картины рассмотрим остальную часть нашего теста:

var suite = new Y.Test.Suite('login');
suite.add(testCase);
Y.Test.Runner.add(suite);
// Инициализируем консоль
new Y.Console({
    newestOnTop: false
}).render('#log');
Y.Test.Runner.run();
});

Теперь давайте посмотрим на модульный тест для событийно-ориентированного кода. Начальный фрагмент теста выглядит так:
YUI().use('test', 'console', 'node-event-simulate'
    , 'login', function(Y) {
    // Фабрика для имитации EH
    var getFakeEH = function(args) {
        return {
            fire: function(event, eventArgs, cb) {
                Y.Assert.areEqual(event, args.event);
                Y.Assert.areEqual(JSON.stringify(eventArgs),
                    JSON.stringify(args.data));
                Y.Assert.isFunction(cb);
                cb(args.err, args.responseArg);
            }
        };
    };
});