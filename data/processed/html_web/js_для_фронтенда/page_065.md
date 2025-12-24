---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.33
tokens: 6100
characters: 1099
timestamp: 2025-12-24T10:03:47.881705
finish_reason: stop
---

, chicken = {}
, mixer = {
    mix: function(chick, ings) {
        expect(ingredients).toBe(ings);
        expect(chicken).toBe(chick);
        return { attr: { isMixed: true } };
    }
}
, MockedCooker = function() {}
;
MockedCooker.prototype = {
    bake: function(food, deg, timer) {
        expect(food.attr.isMixed).toBeTruthy();
        food.attr.isCooked = true;
        return food
    }
    , degrees_f: function(temp) { expect(temp).toEqual(350); }
    , timer: function(time) {
        expect(time).toEqual('50 minutes');
    }
};
var cooker = new MockedCooker()
    , dinner = makeChickenDinner(ingredients, cooker
        , chicken, mixer)
    ;
    expect(dinner).toBeYummy();
});
});
Тестовый код получил полный контроль над имитациями, переданными в него, позволяя производить обширное и гибкое тестирование. Вау!

2.6. Разветвление на входе

Разветвление на входе — это мера числа модулей или объектов, от которых прямо или косвенно зависит ваша функция.

Большинство из того, что мы говорили о разветвлении на выходе, также применимо и к разветвлению на входе (fan-in), но не все.