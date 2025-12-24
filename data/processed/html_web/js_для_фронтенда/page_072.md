---
source_image: page_072.png
page_number: 72
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.97
tokens: 6215
characters: 1574
timestamp: 2025-12-24T10:03:58.538408
finish_reason: stop
---

Мы можем позаимствовать некоторые идеи из какого-либо статически типизированного языка и использовать инъекцию (injection) для ослабления связи:

function setTable(cloth, dishes) {
    this.placeTableCloth(cloth);
    this.placeDishes(dishes);
}

Теперь наш метод стало намного проще изолировать и поэтому его намного проще протестировать: тестовый код может быть передан в имитациях и заглушках непосредственно в метод.

Однако в некоторых случаях подобный подход просто отодвинет проблему немного дальше, не избавившись от нее. Допустим, что у нас возникла необходимость инстанцировать некоторые объекты, в которых мы нуждаемся. Не будут ли эти методы сильно связаны?

Обычно мы хотим инстанцировать объекты как можно раньше и как можно выше в последовательности вызовов методов:

function dinnerParty(guests) {
    var table = new Table()
        , invitations = new Invitations()
        , food = new Ingredients()
        , chef = new Chef()
        , staff = new Staff()
        , cloth = new FancyTableClothWithFringes()
        , dishes = new ChinaWithBlueBorders()
        , dinner;
    invitations.invite(guests);
    table.setTable(cloth, dishes);
    dinner = chef.cook(ingredients);
    staff.serve(dinner);
}

А что, если теперь мы захотим сделать обед более неформальным и использовать бумажную скатерть и бумажные тарелки?

Как уже было сказано, идеально, чтобы все наши основные объекты были созданы в начале нашего приложения, но это не всегда возможно. Для таких ситуаций мы можем позаимствовать другой шаблон из статически типизированных языков: фабрики.