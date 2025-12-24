---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.34
tokens: 6283
characters: 1700
timestamp: 2025-12-24T10:03:40.142517
finish_reason: stop
---

YUI.use('myModule', function(Y) {
    var myModule = function() {
        var sub = new Y.MySubModule();
        this.a = sub.getA();
        this.b = sub.getB();
        this.c = sub.getC();
        this.d = sub.getD();
        this.e = new Y.E();
        this.f = new Y.F();
        this.g = new Y.G();
        this.h = new Y.H();
    };
    Y.MyModule = myModule;
}, { requires: [ 'mySubModule', 'e', 'f', 'g', 'h' ] });
Здесь мы создали уровень абстракции между MyModule и модулями a, b, c, и d и уменьшили на три разветвление на выходе, но помогло ли это? Помогло, хотя и незначительно. Но даже этот топорный рефакторинг сделал MyModule легче в поддержке. Общее количество тестов, однако, немного увеличилось, поскольку теперь нужно протестировать MySubModule, но наша цель — не уменьшить общее число тестов, а сделать проще тестирование каждого отдельного модуля или функции.

Наш рефакторинг MyModule, призванный уменьшить разветвление на выходе, не идеален. Модули и объекты, рефакторинг которых нужно произвести, должны быть в некотором роде связаны, и новый модуль должен обеспечить более интеллектуальный интерфейс для базовых объектов. То есть подмодули будут предоставлены новому модулю с более простым и объединенным интерфейсом. Снова общее число тестов увеличится, но каждую отдельную часть по отдельности будет проще тестировать и поддерживать. Вот небольшой пример:

function makeChickenDinner(ingredients) {
    var chicken = new ChickenBreast()
        , oven = new ConventionalOven()
        , mixer = new Mixer()
        , dish = mixer.mix(chicken, ingredients)
    return oven.bake(dish, new FDegrees(350), new Timer("50 минут"));
}
var dinner = makeChickenDinner(ingredients);