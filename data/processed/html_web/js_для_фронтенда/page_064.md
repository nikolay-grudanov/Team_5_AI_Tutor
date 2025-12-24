---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.07
tokens: 6164
characters: 1452
timestamp: 2025-12-24T10:03:49.279140
finish_reason: stop
---

expect(time).toEqual('50 minutes');
    });
});
var cooker = new MockedCooker()
    , dinner = makeChickenDinner(ingredients, cooker)
;
expect(dinner).toBeYummy();
});
});

Этот новый тестовый код избавился от нескольких симитированных объектов и заменил их локальным «поддельным» объектом, специфичным для этого теста, и сам может выполнить некоторое реальное тестирование, используя expects внутри себя.

Теперь намного проще тестировать объект Cooker, поскольку функциональность его совсем невелика. Мы можем пойти дальше и выполнить инъекцию FDegrees и Таймер вместо того, чтобы убрать тесную связность с ними. И, конечно же, мы также можем ввести или создать другой фасад для Chicken и, возможно, для Mixer. Вот окончательный код метода-инъекции:

function makeChickenDinner(ingredients, cooker, chicken, mixer) {
    var dish = mixer.mix(chicken, ingredients);
    return cooker.bake(dish
        , cooker.degrees_f(350)
        , cooker.timer('50 minutes')
    );
}

Здесь были выполнены инъекции зависимостей (о том, что такое зависимости, мы вскоре поговорим) и приводится соответствующий код для их тестирования:

describe("test make dinner injected", function() {
    it("cooked dinner", function() {
        this.addMatchers({
            toBeYummy: function(expected) {
                return this.actual.attr.isCooked
                    && this.actual.attr.isMixed;
            }
        });
        var ingredients = ['parsley', 'salt']