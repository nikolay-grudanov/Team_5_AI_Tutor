---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.43
tokens: 6251
characters: 1630
timestamp: 2025-12-24T10:07:05.090110
finish_reason: stop
---

, uploadKbps: 56
    , latency: 200
})
Таким образом вы сможете протестировать низкоскоростное соединение.

Нужно отметить, что browsermob-proxy — не единственное прокси-решение. Вы можете использовать и альтернативные инструменты, такие как Fiddler (http://fiddler2.com/home) и Charles (http://www.charlesproxy.com/), но, на мой взгляд, browsermob-proxy является оптимальным решением: бесплатным и отлично работающим.

Это мы рассмотрели, как прикрутить прокси к Selenium для генерации HAR-файлов. То же самое можно сделать и для PhantomJS и CasperJS, они также могут генерировать HAR-файлы. Все что вам нужно, это также установить прокси.

Модуль browsermob-proxy изначально написан для Node.js, а PhantomJS/CasperJS очень отличаются от Node.js, хоть на первый взгляд все они выглядят похоже. Поэтому сначала нужно установить прокси, используя Node.js, затем использовать CasperJS для создания HAR.

В целом, данный процесс подобен расширенному методу, описанному ранее, за исключением того, что передаваемый обратный вызов (callback) для Selenium-части будет порожден сценарием CasperJs для осуществления управления. Как только он будет закончен, мы сможем получить HAR. Когда-нибудь, возможно, PhantomJS и Node.js будут тесно взаимодействовать или же PhantomJS получит код запроса HTTP. А пока мы нуждаемся в Node.js.

Вот как это выглядит со стороны Node.js:

var Proxy = require('browsermob-proxy').Proxy
    , spawn = require('child_process').spawn
    , fs = require('fs')
;
var proxy = new Proxy();
proxy.selHAR('MyCoolHARFile', doCasperJSStuff, function(err, data) {
    if (err) {
        console.error('ERR: ' + err);
