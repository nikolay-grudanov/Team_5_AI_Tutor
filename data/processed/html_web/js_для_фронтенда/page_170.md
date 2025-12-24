---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.51
tokens: 6223
characters: 1512
timestamp: 2025-12-24T10:06:02.946096
finish_reason: stop
---

Ниже приведена простая функция Node.js, возвращающая текущую цену акции для заданного символа (тикера):

```
/**
 * Возвращает текущую цену акции для заданного символа (тикера)
 * при обратном вызове
 *
 * @method getPrice
 * @param symbol <String> тикер
 * @param cb <Function> обратный вызов с результатами cb(error, value)
 * @param httpObj <HTTP> Необязательный HTTP-объект для введения
 * @return ничего
 */
function getPrice(symbol, cb, httpObj) {
    var http = httpObj || require('http')
    , options = {
        host: 'download.finance.yahoo.com' // Спасибо Yahoo!
        , path: '/d/quotes.csv?s=' + symbol + '&f=l1'
    }
    ;
    http.get(options, function(res) {
        res.on('data', function(d) {
            cb(null, d);
        });
    }).on('error', function(e) {
        cb(e.message);
    });
}
```

Дан тикер и обратный вызов. Данная функция получит текущую цену тикера. Она следует стандартному соглашению для обратных вызовов, согласно которому параметр ошибки задается первым. Также обратите внимание, что эта функция позволяет внедрять (заглушать) объект http для более простого тестирования, что уменьшает связывание между этой функцией и объектом http, улучшая тестируемость (вы также можете использовать Mockegy для этого, см. гл. 4).

Внедрение зависимостей мы уже рассмотрели в главе 2, и здесь мы рассмотрим еще один пример, где введение зависимости сделает проще сопровождение кода. Что если хост, предоставляющий сервис курса акций, требует протокол HTTPS? Или HTTPS требует-