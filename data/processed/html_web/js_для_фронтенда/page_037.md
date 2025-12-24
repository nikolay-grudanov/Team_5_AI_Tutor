---
source_image: page_037.png
page_number: 37
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.03
tokens: 6136
characters: 1298
timestamp: 2025-12-24T10:03:10.122070
finish_reason: stop
---

К тому же сбивает с толку странность внутренних и внешних имен docRoot и realRoot.

Лучшее решение — использовать закрытые (private) свойства с методами установки и получения значений. В этом случае свойства будут закрытыми, но все остальное будет открытым (public), в том числе функция проверки — для лучшей тестируемости:

var Obj = (function() {
    return function() {
        var docRoot = '/somewhere';
        this.validateDocRoot = function(val) {
            // логика проверки — вызвать исключение, если не OK
        };
        this.setDocRoot = function(val) {
            this.validateDocRoot(val);
            docRoot = val;
        };
        this.getDocRoot = function() {
            return docRoot;
        };
    };
})();
Теперь доступ к свойству docRoot возможен только через ваш API, что приводит к проверке при записи. Используйте его примерно так:

var myObject = new Obj();
try {
    myObject.setDocRoot('/somewhere/else');
} catch(e) {
    // что-то не так с новым значением docRoot
    // старое значение docRoot все еще здесь
}
// все ОК
console.log(myObject.getDocRoot());

Метод set теперь заключен в блок try/catch, что более ожидаемо, чем заключение в блок try/catch оператора присваивания.

Но осталась еще одна проблема, которую мы можем решить, — что насчет этого: