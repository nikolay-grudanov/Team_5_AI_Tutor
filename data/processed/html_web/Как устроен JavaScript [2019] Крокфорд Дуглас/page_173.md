---
source_image: page_173.png
page_number: 173
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.96
tokens: 7310
characters: 1657
timestamp: 2025-12-24T09:58:07.898403
finish_reason: stop
---

Запуск выполнения запросчика, если таковой его еще ожидает:

    if (
        cancel_array !== undefined
        && next_number < requestor_array.length
    ) {

У каждого запросчика есть номер:

    let number = next_number;
    next_number += 1;

Вызов следующего запросчика, передача функции обратного вызова, сохранение функции отмены, которую может возвратить запросчик:

    const requestor = requestor_array[number];
    try {
        cancel_array[number] = requestor(
            function start_requestor_callback(value, reason) {

Функция обратного вызова вызывается запросчиком, когда он завершает свою работу. Если работы больше нет, вызов игнорируется. Например, это может быть результат, отправленный назад по истечении лимита времени. Данная функция обратного вызова может быть вызвана только один раз:

        if (
            cancel_array !== undefined
            && number !== undefined
        ) {

Больше нам не нужна отмена, связанная с этим запросчиком:

        cancel_array[number] = undefined;

Вызов функции action для информирования запросчика о случившемся:

        action(value, reason, number);

Очистка номера, чтобы этот обратный вызов не мог быть использован еще раз:

        number = undefined;

Если есть еще какие-нибудь запросчики, ожидающие запуска, то происходит запуск следующего запросчика. Если следующий запросчик встроен в последовательность, осуществляется передача ему самого последнего значения. Другие запросчики получают исходное значение initial_value:

        return start_requestor(
            factory_name === "sequence"
            ? value
            : initial_value
        );
    },
    value
);