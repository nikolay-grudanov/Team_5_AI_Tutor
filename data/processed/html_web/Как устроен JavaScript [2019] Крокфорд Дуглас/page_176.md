---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.46
tokens: 7304
characters: 1757
timestamp: 2025-12-24T09:58:20.019964
finish_reason: stop
---

20.17    Как работает событийное программирование

Проверяем массив и возвращаем запросчик:

    check_requestor_array(requestor_array, factory_name);
    return function parallel_requestor(callback, initial_value) {
        check_callback(callback, factory_name);
        let number_of_pending = requestor_array.length;
        let number_of_pending_required = number_of_required;
        let results = [];

run его запускает:

    let cancel = run(
        factory_name,
        requestor_array,
        initial_value,
        function parallel_action(value, reason, number) {

Функция действия получает результат работы каждого запросчика, имеющегося в массиве. Функции parallel требуется возвращение массива всех видимых ему значений:

    results[number] = value;
    number_of_pending -= 1;

Если запросчик был одним из обязательных, нужно убедиться, что он завершил свою работу успешно. Если же выдал сбой, параллельная операция считается сбойной. Если выдал сбой необязательный запросчик, можно продолжить работу:

    if (number < number_of_required) {
        number_of_pending_required -= 1;
        if (value === undefined) {
            cancel(reason);
            callback(undefined, reason);
            callback = undefined;
            return;
        }
    }

Если все было обработано или все обязательные запросчики завершили работу успешно и у нас не было time_option, значит, мы справились с задачей:

    if (
        number_of_pending < 1
        || (
            time_option === undefined
            && number_of_pending_required < 1
        )
    ) {
        cancel(make_reason(factory_name, "Optional."));
        callback(
            factory_name === "sequence"
            ? results.pop()
            : results
        );
    }