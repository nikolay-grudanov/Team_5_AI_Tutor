---
source_image: page_058.png
page_number: 58
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.42
tokens: 6219
characters: 1418
timestamp: 2025-12-24T10:03:35.519768
finish_reason: stop
---

телем высокой связанности кода, которая делает функции и модули чрезмерно хрупкими.

Стратегия разработки с учетом разветвления на выходе заключается в создании объекта/модуля, который инкапсулирует в себе некоторые разветвленные модули, выставляя наружу только одну функцию.

Рассмотрим следующий код, разветвление на выходе для которого как минимум 8:

YUI.use('myModule', function(Y) {
    var myModule = function() {
        this.a = new Y.A();
        this.b = new Y.B();
        this.c = new Y.C();
        this.d = new Y.D();
        this.e = new Y.E();
        this.f = new Y.F();
        this.g = new Y.G();
        this.h = new Y.H();
    };
    Y.MyModule = myModule;
}, { requires: [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ] });

Поддержка и тестирование этого кода будет проблематичным, он нуждается в рефакторинге. Идея заключается в вынесении связанных модулей в отдельный модуль:

YUI.use('mySubModule', function(Y) {
    var mySubModule = function() {
        this.a = new Y.A();
        this.b = new Y.B();
        this.c = new Y.C();
        this.d = new Y.D();
    };
    mySubModule.prototype.getA = function() { return this.a; };
    mySubModule.prototype.getB = function() { return this.b; };
    mySubModule.prototype.getC = function() { return this.c; };
    mySubModule.prototype.getD = function() { return this.d; };
    Y.MySubModule = mySubModule;
}, { requires: [ 'a', 'b', 'c', 'd' ] });