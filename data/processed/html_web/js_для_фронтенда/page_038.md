---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.19
tokens: 6176
characters: 1519
timestamp: 2025-12-24T10:03:12.383501
finish_reason: stop
---

var myObject = new Obj();
myObject.docRoot = '/somewhere/wrong';
// и затем позже...
var dR = myObject.docRoot;

Конечно, ни один из методов в API не будет знать об этом ошибочно созданном пользователем поле docRoot. Что есть нехорошо. К счастью, это очень легко исправить:

var Obj = (function() {
    return function() {
        var docRoot = '/somewhere';
        this.validateDocRoot = function(val) {
            // логика проверки — исключение, если не ОК
        };
        this.setDocRoot = function(val) {
            this.validateDocRoot(val);
            docRoot = val;
        };
        this.getDocRoot = function() {
            return docRoot;
        };
        Object.preventExtensions(this)
    }
})();
Используя Object.preventExensions, мы породим исключение TypeError, если кто-то попытается добавить свойство в объект. В результате не будет никаких поддельных полей (свойств). Это очень удобно для всех ваших объектов, особенно если у вас есть непосредственный доступ к свойствам. Интерпретатор теперь будет перехватывать любые ошибочно добавленные свойства путем порождения TypeError.

Этот код также отлично инкапсулирует разделение команд и запросов с методами set/get/validator: все раздельны и каждый тестируется изолированно.

Функции проверки должны быть закрытыми, но для чего? Лучше сохранять их открытыми не только из соображений тестирования, но и чтобы производственный код мог проверить, является ли значение docRoot допустимым или нет без необходимости его явной установки на объекте.