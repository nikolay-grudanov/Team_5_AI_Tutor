---
source_image: page_062.png
page_number: 62
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.83
tokens: 6190
characters: 1469
timestamp: 2025-12-24T10:03:44.634049
finish_reason: stop
---

(temperature) и "таймер" (timer). Затем мы выполняем инъекцию фасада для уменьшения связанности:

function Cooker(oven) {
    this.oven = oven;
}
Cooke.prototype.bake = function(dish, deg, timer) {
    return this.oven.bake(dish, deg, timer);
};
Cooke.prototype.degrees_f = function(deg) {
    return new FDegrees(deg);
};
Cooke.prototype.timer = function(time) {
    return new Timer(time);
};
function makeChickenDinner(ingredients, cooker) {
    var chicken = new ChickenBreast()
        , mixer = new Mixer()
        , dish = mixer.mix(chicken, ingredients)
    return cooker.bake(dish
        , cooker.degrees_f(350)
        , cooker.timer("50 minutes")
    );
}
var cooker = new Cooke(new ConventionalOven())
    , dinner = makeChickenDinner(ingredients, cooker);

У makeChickenDinner теперь есть две сильно связанных зависимостей: ChickenBreast и Mixer. Фасад обрабатывает "всю работу по кухне". Причем он не использует весь API, предоставляемый "духовкой", "градусником" и "таймером", а использует только то, что необходимо для выполнения задания. Мы распределили зависимости более равномерно, что упрощает поддержку кода функции, ее тестирование и уменьшает число разветвлений на выходе. Наш новый код (после рефакторинга) модульного теста будет таким:

describe("test make dinner refactored", function() {
    // Имитации
    Food = function() {};
    Food.prototype.attr = {};
    MixedFood = function(args) {
        var obj = Object.create(Food.prototype);