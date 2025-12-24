---
source_image: page_140.png
page_number: 140
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.84
tokens: 7408
characters: 1943
timestamp: 2025-12-24T09:57:20.143037
finish_reason: stop
---

16.2 Как работает this

Привязка this характерна тем, что имеет динамическую природу. Все остальные переменные имеют статическую привязку. И это создает путаницу.

function pubsub() {

    // Фабрика pubsub создает объект публикации-подписки. Код, который
    // получает доступ к объекту, может подписаться на функцию, получающую
    // публикации, и опубликовать материал, который будет доставлен всем
    // подписчикам.

    // Для содержания функции subscriber используется массив подписчиков. Он
    // скрыт от внешнего мира, поскольку находится в области видимости функции
    // pubsub.

    const subscribers = [];
    return {
        subscribe: function (subscriber) {
            subscribers.push(subscriber);
        },
        publish: function (publication) {
            const length = subscribers.length;
            for (let i = 0; i < length; i += 1) {
                subscribers[i](publication);
            }
        }
    };
}

Функция subscriber получает привязку this к массиву subscribers, потому что:

    subscribers[i](publication);

является вызовом метода. Он не обязательно похож на вызов метода, но суть от этого не меняется. Это дает каждой функции subscriber доступ к массиву subscribers, что может позволить subscriber нанести вред, например удалить всех остальных подписчиков или перехватить и изменить их сообщения.

my_pubsub.subscribe(function (publication) {
    this.length = 0;
});

Привязка this способна угрожать безопасности и надежности. Когда функция сохраняется в массиве, а позже вызывается, ей дается this, привязанная к массиву. Если наличие доступа к массиву для функций не предполагалось, как обычно и бывает, возникает вероятность неблагоприятного развития событий.

Функция publish может быть исправлена путем замены цикла for циклом forEach:

    publish: function (publication) {
        subscribers.forEach(function (subscriber) {
            subscriber(publication);
        }
    }