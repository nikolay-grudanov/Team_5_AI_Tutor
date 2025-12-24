---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.92
tokens: 6095
characters: 1250
timestamp: 2025-12-24T10:03:37.894607
finish_reason: stop
---

obj.attr.isMixed = true;
return obj;
};
CookedFood = function(dish) {
    var obj = Object.create(Food.prototype);
    obj.attr.isCooked = true;
    return obj;
};
ChickenBreast = function() {
    var obj = Object.create(Food.prototype);
    obj.attr.isChicken = true;
    return obj;
};
Meal = function(dish) { this.dish = dish };
Mixer = function() {
    this.mix = function(chicken, ingredients) {
        return new MixedFood(chicken, ingredients);
    };
};
Ingredients = function(ings) { this.ings = ings; };
// конец имитаций
it("cooked dinner", function() {
    this.addMatchers({
        toBeYummy: function(expected) {
            return this.actual.attr.isCooked &&
                this.actual.attr.isMixed;
        }
    });
    var ingredients = new Ingredients('parsley', 'salt')
        , MockedCooker = function() {};
    // Локальный (для этого теста) имитированный объект Cooker,
    // который фактически может сделать тестирование
    MockedCooker.prototype = {
        bake: function(food, deg, timer) {
            expect(food.attr.isMixed).toBeTruthy();
            food.attr.isCooked = true;
            return food
        }
        , degrees_f: function(temp) { expect(temp).toEqual(350); }
        , timer: function(time) {