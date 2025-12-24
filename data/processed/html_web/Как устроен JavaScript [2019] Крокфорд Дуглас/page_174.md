---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.05
tokens: 7397
characters: 1859
timestamp: 2025-12-24T09:58:19.808115
finish_reason: stop
---

20.15 Как работает событийное программирование

Запросчики должны сообщать о своем сбое через обратный вызов. Им не разрешено выдавать исключения. Если будет перехвачено исключение, это будет считаться сбоем:

    } catch (exception) {
        action(undefined, exception, number);
        number = undefined;
        start_requestor(value);
    }
}

Теперь, располагая функциями cancel и start_requestor, можно приступать к работе.

Если запрошено отслеживание превышения лимита времени, запускаем таймер:

    if (time_limit !== undefined) {
        if (typeof time_limit === "number" && time_limit >= 0) {
            if (time_limit > 0) {
                timer_id = setTimeout(timeout, time_limit);
            }
        } else {
            throw make_reason(factory_name, "Bad time limit.", time_limit);
        }
    }

Если есть намерение запустить параллельный или состязательный режим, нужно запустить все запросчики одновременно. Но если установлен регулятор, запускается разрешенное им количество запросчиков, а когда завершит работу каждый запросчик, запускается следующий.

Фабрики sequence и fallback устанавливают регулятор throttle равным 1, поскольку они обрабатывают запросчики поочередно и всегда запускают другой запросчик, когда завершает работу его предшественник:

    if (!Number.isSafeInteger(throttle) || throttle < 0) {
        throw make_reason(factory_name, "Bad throttle.", throttle);
    }
    let repeat = Math.min(throttle || Infinity, requestor_array.length);
    while (repeat > 0) {
        setTimeout(start_requestor, 0, initial_value);
        repeat -= 1;
    }

Возвращаем cancel, что позволяет запросчику завершить работу:

    return cancel;
}

Теперь рассмотрим четыре открытые функции.

Функция parallel самая сложная из них из-за массива необязательных запросчиков:

    function parallel(
        required_array,