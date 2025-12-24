---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.21
tokens: 6141
characters: 1311
timestamp: 2025-12-24T10:03:59.741505
finish_reason: stop
---

bind('Pad').to(new LaunchPad()).is("singleton");
});
Здесь объекты SpaceShuttleMainEngine, SpaceShuttleSolidRocketBooster и ShuttleRemoteManipulatorSystem определены в другом месте:

var SpaceShuttleMainEngine = function() {
    ...
};

Теперь каждый раз, когда потребуется MainEngine, инжектор knit заполнит его:

var SpaceShuttle = function(MainEngine
    , BoosterEngine1
    , BoosterEngine2
    , Arm) {
    this.mainEngine = MainEngine;
}

Таким образом, весь объект SpaceShuttle со всеми его зависимостями доступен в методе knit.inject:

knit.inject(function(ShuttleDiscovery, ShuttleEndeavor, Pad) {
    ShuttleDiscovery.blastOff(Pad);
    ShuttleEndeavor.blastOff(Pad);
});

Инжектор knit рекурсивно выясняет все зависимости SpaceShuttle и создает объекты SpaceShuttle для нас. Определение Pad как синглетона (одиночного элемента, singleton) гарантирует, что любой запрос объекта Pad будет всегда возвращать одно инстанцирование.

Предположим, со временем «Мексика» создает еще более совершенный объект ShuttleRemoteManipulatorSystem, чем «Канада». Переключение на этот тип «оружия» происходит очень просто:

bind('Arm').to(MexicanShuttleRemoteManipulatorSystem).is("constructor");

Теперь все объекты, требующие Arm, получат мексиканскую версию вместо канадской без каких-либо других изменений в коде.