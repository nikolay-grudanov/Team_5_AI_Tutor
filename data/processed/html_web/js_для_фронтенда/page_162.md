---
source_image: page_162.png
page_number: 162
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.90
tokens: 6158
characters: 1433
timestamp: 2025-12-24T10:05:47.212975
finish_reason: stop
---

mockery.registerMock('fs', fsMock);
var mySum = require('./mySumFS');
expect(mySum.sum(filename)).toEqual(12);
mockery.deregisterMock('fs');
});

Мы добавили и включили объект mockery, после чего мы указали Mockery игнорировать вызовы require. По умолчанию Mockery выведет ошибку, если какой-то требуемый модуль не будет известен ему (через registerAllowable или registerMock); но так как мы не хотим имитировать объект по ходу теста, то мы говорим Mockery замолчать.

Поскольку мы создаем новые имитации для модуля fs для каждого теста (скоро будет показано, зачем мы это делаем), нам нужно передать true в качестве второго параметра методу registerAllowable, чтобы метод deregisterAllowable работал надлежащим образом.

Наконец, давайте рассмотрим сам тест. В рамках него мы тестируем, что метод fs.readFileSync был вызван правильно и возвращает некоторые фиксированные данные обратно в функцию sum.

Вот тест для сложения строк:

it("Adds Strings!", function() {
    var filename = "strings"
    .fsMock = {
        readFileSync: function (path, encoding) {
            expect(path).toEqual(filename);
            expect(encoding).toEqual('utf8');
            return JSON.stringify({ a: 'testable'
                , b: 'JavaScript' });
        }
    }
    mockery.registerMock('fs', fsMock);
    var mySum = require('./mySumFS');
    expect(mySum.sum(filename)).toEqual('testableJavaScript');
    mockery.deregisterMock('fs');
});