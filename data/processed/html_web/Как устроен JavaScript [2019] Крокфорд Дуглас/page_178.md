---
source_image: page_178.png
page_number: 178
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.09
tokens: 7209
characters: 1289
timestamp: 2025-12-24T09:58:18.703226
finish_reason: stop
---

20.19 Как работает событийное программирование

    ? "fallback"
    : "race"
);

check_requestor_array(requestor_array, factory_name);
return function race_requestor(callback, initial_value) {
    check_callback(callback, factory_name);
    let number_of_pending = requestor_array.length;
    let cancel = run(
        factory_name,
        requestor_array,
        initial_value,
        function race_action(value, reason, number) {
            number_of_pending -= 1;

У нас есть победитель. Отменяем работу проигравших и передаем значение обратному вызову.

    if (value !== undefined) {
        cancel(make_reason(factory_name, "Loser.", number));
        callback(value);
        callback = undefined;
    }
Победителя нет. Сигнализируем о сбое.

    if (number_of_pending < 1) {
        cancel(reason);
        callback(undefined, reason);
        callback = undefined;
    }
},
function race_timeout() {
    let reason = make_reason(
        factory_name,
        "Timeout.",
        time_limit
    );
    cancel(reason);
    callback(undefined, reason);
    callback = undefined;
},
    time_limit,
    throttle
);
return cancel;
};

Альтернативный режим (fallback) — это всего лишь регулируемый состязательный режим (race):

    function fallback(requestor_array, time_limit) {