---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.61
tokens: 6234
characters: 1574
timestamp: 2025-12-24T10:05:54.743284
finish_reason: stop
---

var fs = require('fs');
return fs.readFileSync(file, 'utf8');
};
exports.getByParam = function(a, b) {
    return JSON.stringify({a: a, b: b});
};

Мы обобщили ввод данных, и теперь операция суммирования у нас по факту присутствует только в одном месте. Во-первых, мы разделили операции получения данных и операции обработки данных. Во-вторых, благодаря этому мы можем удобно добавлять новые операции (вычитание, умножение и т.д.) над введенными данными.

Наш срес-файл для этого кода (без Mockegу-содержимого для ясности) будет выглядеть примерно так:

mySum = require('./mySumFunc');
describe("Sum suite Functions", function() {
    it("Adds By Param!", function() {
        var sum = mySum.sum(mySum.getByParam, [6,6]);
        expect(sum).toEqual(12);
    });
    it("Adds By File!", function() {
        var sum = mySum.sum(mySum.getByFile, ["strings"]));
        expect(sum).toEqual("testableJavaScript");
    });
});
И конечно же, файл со строками будет содержать следующее:

('a': "testable", 'b': "JavaScript")

Что-то здесь не совсем правильно. У нас нет хорошей изоляции функции mySum. Конечно, нам нужны отдельные тесты для разных способов ввода функции mySum: getByParam и getByFile. Но для тестирования самой функции Sum нам нужно имитировать и заглушить эти функции, чтобы функция суммы тестировалась в изоляции.

Такая ситуация — отличное место для применения шпионов Jasmine. Используя шпионы, мы можем протестировать две вспомогательные функции, чтобы убедиться, что они будут вызываться с корректными параметрами, а также позволить тестовому коду или вер-