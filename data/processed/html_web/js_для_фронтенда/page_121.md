---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.44
tokens: 6217
characters: 1689
timestamp: 2025-12-24T10:05:01.502173
finish_reason: stop
---

Процесс тот же: загружается jQuery, библиотека socket.io и jQuery-клиент EventHub. Коммутатор событий EventHub представлен как jQuery-плагин и использует jQuery-синтаксис событий bind и trigger.

Любое событие, отправленное клиентом, может иметь необязательную функцию обратного вызова, которая указывается как последний параметр:

hub.fire('CHECK_USER', 'mark',
    function(result) { console.log('exists: ' + result.exists); });

Любой ответчик на это событие задается соответствующей функцией как последний параметр в списке аргументов события для передачи произвольных данных:

hub.on('CHECK_USER', function(username, callback) {
    callback({ exists: DB.exists(username) });
});

Обратный вызов (callback) вызывает удаленную функцию из пространства вызывающей стороны с предоставленными ей данными вызывающего. Данные сериализуются как JSON, поэтому при желании вы можете получить целевой ответ на произошедшее (сгенерированное) событие (в данном случае речь идет о событии 'CHECK_USER').

Вы также можете использовать метод addEvent для проверки имен событий во время компиляции с использованием YUI3:

var clickEvent = hub.addEvent('click');
clickEvent.on(function(data) { /* получаем событие click! */ });
clickEvent.fire({ button: 'clicked' }); // отправляем событие click!

В случае с jQuery вы будете использовать вместо методов on и fire методы bind и trigger:

var clickEvent = hub.addEvent('click');
clickEvent.bind(function(data) { /*получаем событие click! */ });
clickEvent.trigger({ button: 'clicked' }); // отправляем событие click!

Вы также можете использовать функции коммутатора событий для одноадресных событий:

hub.on('CHECK_USER', function(username, callback) {