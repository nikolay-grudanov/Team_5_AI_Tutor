---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.70
tokens: 6222
characters: 1584
timestamp: 2025-12-24T10:05:53.200520
finish_reason: stop
---

нуть вызываемые значения, или передать вызов низлежащей функции.

Рассмотрим модифицированную версию функции со шпионом для getByParam:

it("Adds By Param!", function() {
    var params = [8, 4]
    , expected = 12
    ;
    spyOn(mySum, 'getByParam').andCallThrough();
    expect(mySum.sum(mySum.getByParam, params)).toEqual(expected);
    expect(mySum.getByParam).toHaveBeenCalled();
    expect(mySum.getByParam.mostRecentCall.args).toEqual(params);
});
После установки шпиона на mySum.getByParam и перенаправления его на вызов к актуальной реализации, мы можем проверить, что вспомогательная функция вызвана с корректными параметрами.

Замена строки andCallThrough следующей строкой:

spyOn(mySum, 'getByParam').andReturn('{"a":8,"b":4}');

позволит нашему тестовому сценарию вернуть фиксированные данные и пропустить вызов getByParam. Вы также можете предоставить альтернативную функцию, возвращаемое значение которой будет передано обратно вызывающей стороне. Это очень удобно, если нужно вычислить возвращаемое шпионом значение.

У Jasmine есть большое количество трюков, в том числе простое отключение теста, имитация setTimer и setInterval для более простого тестирования, поддержка асинхронного тестирования. Со всем этим вы можете познакомиться, перейдя на домашнюю страницу Jasmine. Кроме того, Jasmine может использоваться не только для тестирования серверной части JavaScript, этот фреймворк можно применять для модульного тестирования и клиентского JavaScript. В то же время извлечение вывода теста при выполнении Jasmine в браузере не так просто, как в случае YUI Test.