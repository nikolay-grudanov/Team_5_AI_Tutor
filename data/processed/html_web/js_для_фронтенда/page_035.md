---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.75
tokens: 6131
characters: 1351
timestamp: 2025-12-24T10:03:07.642203
finish_reason: stop
---

хотим обезопасить себя от побочных эффектов установки значений без их одновременной проверки. Поэтому, хотя разделение функций — отличный прием для повышения тестируемости кода и снижения его сложности, нам нужно убедиться, что оно будет реализовано корректно.

Следующая итерация будет примерно такой:

function configure(values) {
    var config = { docRoot: '/somewhere' };
    for (var key in values) {
        config[key] = values[key];
    }
    validateDocRoot(config);
    validateSomethingElse(config);
    ...
    return config;
}

Данная новая конфигурационная функция или возвращает допустимый объект config, или порождает ошибку. Все функции проверки (validateDocRoot, validateSomethingElse,...) могут быть протестированы отдельно из самой функции configure.

Последний штрих — мы должны соединить каждый ключ объекта config с его функцией проверки и хранить весь хэш в одном централизованном месте:

var fields {
    docRoot: { validator: validateDocRoot, default: '/somewhere' }
    , somethingElse: { validator: validateSomethingElse }
};
function configure(values) {
    for (var key in fields) {
        if (typeof values[key] !== 'undefined') {
            fields[key].validator(values[key]);
            config[key] = values[key];
        } else {
            config[key] = fields[key].default;
        }
    }
    return config;
}