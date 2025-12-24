---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.63
tokens: 7362
characters: 1546
timestamp: 2025-12-24T09:58:02.367770
finish_reason: stop
---

20.11 Как работает событийное программирование

Пример:

let getWeather = parseq.fallback([
    fetch("weather", localCache),
    fetch("weather", localDB),
    fetch("weather", remoteDB)
]);

let getAds = parseq.race([
    getAd(adnet.klikHaus),
    getAd(adnet.inUFace),
    getAd(adnet.trackPipe)
]);

let getNav = parseq.sequence([
    getUserRecord,
    getPreference,
    getCustomNav
]);

let getStuff = parseq.parallel(
    [getNav, getAds, getMessageOfTheDay],
    [getWeather, getHoroscope, getGossip],
    500,
    true
);

Исключения

Исключения слишком слабы, чтобы справляться со сбоями, происходящими на протяжении многих ходов. Исключение может опустошить стек, но от хода к ходу ничто в стеке не выживает. У исключений нет возможности сообщать будущему ходу о каком-то сбое в ранее состоявшемся ходе, и исключения не способны совершить путешествие во времени к источнику сбойного запроса.

Фабрике разрешено выдавать исключение, потому что ссылка на вызвавший ее код все еще находится в стеке. Запросчикам вообще не разрешается выдавать исключения, поскольку в стеке нет ничего, чтобы их перехватывать. Запросчики не должны допускать сброса случайных исключений. Все исключения должны быть перехвачены и переданы в функцию обратного вызова в качестве причины.

Реализация Parseq

Посмотрим на реализацию Parseq. Она не слишком большая. В ее состав входят четыре открытые и четыре закрытые функции.

Первая закрытая функция называется make_reason. Она создает объект ошибки:

function make_reason(factory_name, excuse, evidence) {