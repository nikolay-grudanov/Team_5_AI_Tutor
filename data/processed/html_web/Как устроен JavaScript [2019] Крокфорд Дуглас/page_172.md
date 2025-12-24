---
source_image: page_172.png
page_number: 172
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.67
tokens: 7383
characters: 1751
timestamp: 2025-12-24T09:58:11.231266
finish_reason: stop
---

20.13 Как работает событийное программирование

    initial_value,
    action,
    timeout,
    time_limit,
    throttle = 0
    )
{
Функция run выполняет работу, общую для всех фабрик Parseq. Она принимает имя фабрики, массив запросчиков, исходное значение, то или иное действие обратного вызова, функцию обратного вызова по истечении лимита времени, лимит времени в миллисекундах и регулятор.

Если все получается, вызываются все функции-запросчики, содержащиеся в массиве. Каждая из них может возвратить функцию отмены, хранящуюся в cancel_array:

let cancel_array = new Array(requestor_array.length);
let next_number = 0;
let timer_id;

Нам нужны функции cancel и start_requestor:

function cancel(reason = make_reason(factory_name, "Cancel.")) {
Остановка всех незавершенных дел — эта функция может быть вызвана, когда запросчик дает сбой. Ее также вызывают, когда запросчик завершает свою работу успешно, например, когда в состязательном режиме останавливается работа всех, кто проиграл, или в параллельном режиме останавливается работа тех необязательных запросчиков, которые еще не завершили работу.

Если таймер запущен, его следует остановить.

if (timer_id !== undefined) {
    clearTimeout(timer_id);
    timer_id = undefined;
}

Если происходит что-то еще, это действие нужно отменить.

if (cancel_array !== undefined) {
    cancel_array.forEach(function (cancel) {
        try {
            if (typeof cancel === "function") {
                return cancel(reason);
            }
        } catch (ignore) {}
    });
    cancel_array = undefined;
}
}

function start_requestor(value) {

Теперь функция start_requestor совсем не рекурсивная. Она не вызывает сама себя напрямую, но возвращает функцию, которая может вызвать start_requestor.