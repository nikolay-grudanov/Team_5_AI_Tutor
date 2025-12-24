---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.02
tokens: 6186
characters: 1565
timestamp: 2025-12-24T10:03:37.530561
finish_reason: stop
---

Эта функция разветвляется как сумасшедшая: создает пять внешних объектов и вызывает два метода двух разных объектов. Эта функция сильно связана с пятью объектами. Тестирование этой функции затруднено, поскольку вы нуждаетесь в заглушках во всех объектах и запросах. Имитация (mocking) метода mix и метода bake объекта oven будет очень сложной, поскольку оба возвращают значения. Давайте посмотрим, на что мог бы быть похож модульный тест для этой функции:

describe("test make dinner", function() {
    // Mocks
    Food = function(obj) {};
    Food.prototype.attr = {};
    MixedFood = function(args) {
        var obj = Object.create(Food.prototype);
        obj.attr.isMixed = true; return obj;
    };
    CookedFood = function(dish) {
        var obj = Object.create(Food.prototype);
        obj.attr.isCooked = true; return obj;
    };
    FDegrees = function(temp) { this.temp = temp };
    Meal = function(dish) { this.dish = dish };
    Timer = function(timeSpec) { this.timeSpec = timeSpec; };
    ChickenBreast = function() {
        var obj = Object.create(Food.prototype);
        obj.attr.isChicken = true; return obj;
    };
    ConventionalOven = function() {
        this.bake = function(dish, degrees, timer) {
            return new CookedFood(dish, degrees, timer);
        };
    };
    Mixer = function() {
        this.mix = function(chicken, ingredients) {
            return new MixedFood(chicken, ingredients);
        };
    };
    Ingredients = function(ings) { this.ings = ings; };
    // конец Mocks
    it("cooked dinner", function() {