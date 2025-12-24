---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.16
tokens: 7346
characters: 1777
timestamp: 2025-12-24T09:57:53.513910
finish_reason: stop
---

20.7 Как работает событийное программирование

Функция обратного вызова принимает два аргумента — значение и причину. Значение — это результат работы запросчика или undefined, если запросчик дал сбой. Необязательный аргумент причина может использоваться для документирования сбоев:

function my_little_callback(значение, причина)

Функция запросчика способна дополнительно возвратить функцию отмены. Она может быть вызвана для отмены работы по любой причине. Это не отмена сделанного. Функция отмены предназначена только для прекращения ненужной работы. Таким образом, если запросчик запускает весьма затратную операцию на другом сервере и операция больше не требуется, то вызов принадлежащей запросчику функции отмены может отправить сообщение о прекращении на сервер.

function my_little_cancel(причина)

Фабрики запросчиков

Основная часть вашей работы заключается в создании фабрик, принимающих аргументы и возвращающих запросчики.

Эта фабрика служит простой оболочкой, которая может принять любую функцию с одним аргументом и возвратить запросчик.

function requestorize(unary) {
    return function requestor(callback, value) {
        try {
            return callback(unary(value));
        } catch (exception) {
            return callback(undefined, exception);
        }
    };
}

Следующая фабрика создает запросчик, способный читать файл на Node.js:

function read_file(directory, encoding = "utf-8") {
    return function read_file_requestor(callback, value) {
        return fs.readFile(
            directory + value,
            encoding,
            function (err, data) {
                return (
                    err
                    ? callback(undefined, err)
                    : callback(data)
                );
            }
        );
    };
}