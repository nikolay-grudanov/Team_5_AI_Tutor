---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.34
tokens: 6169
characters: 1565
timestamp: 2025-12-24T10:05:47.322139
finish_reason: stop
---

Ниже приведен простой Jasmine-тест для нашей функции:

    var mySum = require('./mySumFS');
    describe("Sum suite File", function() {
        it("Adds Integers!", function() {
            expect(mySum.sum("numbers")).toEqual(12);
        });
    });
Сама JSON-строка находится в файле numbers:

    {"a":5,"b":7}

Jasmine запустит тест, он будет пройден, и все будет хорошо. Но мы слишком много одновременно тестируем, а именно мы вовлекаем и используем зависимость fs, но суть модульного тестирования — в изолировании testируемого кода. Мы не хотим, чтобы данная зависимость fs влияла на наши тесты. Конечно, это крайний случай, но давайте проследуем за логикой.

Используя Mockery как часть нашего Jasmine-теста, мы можем обработать вызов require и заменить модуль fs его имитированной версией. Рассмотрим наш новый Jasmine-сценарий:

    var mockery = require('mockery');
    mockery.enable();
    describe("Sum suite File", function() {
        beforeEach(function() {
            mockery.registerAllowable('./mySumFS', true);
        });
        afterEach(function() {
            mockery.deregisterAllowable('./mySumFS');
        });
        it("Adds Integers!", function() {
            var filename = "numbers"
                , fsMock = {
                    readFileSync: function (path, encoding) {
                        expect(path).toEqual(filename);
                        expect(encoding).toEqual('utf8');
                        return JSON.stringify({ a: 9, b: 3 });
                    }
                }
            ...
        });
    });