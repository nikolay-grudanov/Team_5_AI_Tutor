---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.40
tokens: 6269
characters: 1782
timestamp: 2025-12-24T10:04:07.518451
finish_reason: stop
---

JavaScript тоже есть оператор instanceof, но у него нет ни проверки типа, ни понятия реализации интерфейса. Так можем мы использовать внедрение зависимости в JavaScript или нет? Конечно, да!

Давайте вкратце рассмотрим knit, инжектор в стиле Google Guice для JavaScript. Рассмотрим следующий исходный код:

```javascript
var SpaceShuttle = function() {
    this.mainEngine = new SpaceShuttleMainEngine();
    this.boosterEngine1 = new SpaceShuttleSolidRocketBooster();
    this.boosterEngine2 = new SpaceShuttleSolidRocketBooster();
    this.arm = new ShuttleRemoteManipulatorSystem();
};
```

Со всеми объектами, инстанцируемыми в конструкторе, как мы можем протестировать SpaceShuttle без его «двигателей» и «пушки»? Инстанцирование зависимых объектов в конструкторах (или в другом месте в объекте) сильно связывает зависимость, которая делает тестирование более трудным, а значит нужно поручить это инжектору.

Первым делом нужно сделать конструктор инъектируемым:

```javascript
var SpaceShuttle = function(mainEngine, b1, b2, arm) {
    this.mainEngine = mainEngine;
    this.boosterEngine1 = b1;
    this.boosterEngine2 = b2;
    this.arm = arm;
};
```

Теперь мы можем использовать knit для определения того, как мы хотим, чтобы создавались наши объекты:

```javascript
knit = require('knit');
knit.config(function (bind) {
    bind('MainEngine').to(SpaceShuttleMainEngine).is("constructor");
    bind('BoosterEngine1').to(SpaceShuttleSolidRocketBooster)
        .is("constructor");
    bind('BoosterEngine2').to(SpaceShuttleSolidRocketBooster)
        .is("constructor");
    bind('Arm').to(ShuttleRemoteManipulatorSystem).is("constructor");
    bind('ShuttleDiscovery').to(SpaceShuttle).is("constructor");
    bind('ShuttleEndeavor').to(SpaceShuttle).is("constructor");
});