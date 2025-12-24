---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.60
tokens: 7275
characters: 1447
timestamp: 2025-12-24T09:58:24.150913
finish_reason: stop
---

callback = undefined;
}
},
function parallel_timeout() {

Когда срабатывает таймер, работа прекращается, если только она не велась под параметром времени со значением false. Это значение не накладывает лимит времени на работу обязательных запросчиков, позволяя необязательным работать до тех пор, пока не завершится работа обязательных запросчиков или не истечет лимит времени в зависимости от того, что наступит позже.

const reason = make_reason(
    factory_name,
    "Timeout.",
    time_limit
);
if (time_option === false) {
    time_option = undefined;
    if (number_of_pending_required < 1) {
        cancel(reason);
        callback(results);
    }
} else {

Время истекло. Если все запросчики завершили свою работу успешно, то параллельная операция будет считаться успешно завершенной.

    cancel(reason);
    if (number_of_pending_required < 1) {
        callback(results);
    } else {
        callback(undefined, reason);
    }
    callback = undefined;
}
},
time_limit,
throttle
);
return cancel;
};

Функция race намного проще, чем parallel, поскольку она не нуждается в аккумулировании всех результатов. Ей нужен всего лишь один результат.

function race(requestor_array, time_limit, throttle) {

Фабрика race возвращает запросчик, запускающий одновременно все запросчики, имеющиеся в массиве requestor_array. Первый же успешно завершивший работу запросчик считается победителем.

    const factory_name = (
        throttle === 1