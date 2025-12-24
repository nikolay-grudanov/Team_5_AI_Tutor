---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.43
tokens: 6180
characters: 1379
timestamp: 2025-12-24T10:06:39.572462
finish_reason: stop
---

;
browser
    .testMode()
    .init()
    .url("http://search.yahoo.com")
    .setValue("#yschsp", "JavaScript")
    .submitForm("#sf")
    .tests.visible('#resultCount', true, 'Got result count')
    .end();

На фоне запущенного локально сервера Selenium Server вышеприведенный код запустит браузер Firefox и откроет в нем страницу поисковика Yahoo (http://search.yahoo.com) с поисковым запросом «JavaScript», и обеспечит, что элемент с id равным resultCount будет видимым.

Создать скриншот средствами Selenium очень легко. Просто добавьте вызов saveScreenshot:

var webdriverjs = require("webdriverjs")
    , browser = webdriverjs.remote({
        host: 'localhost'
        , port: 4444
        , desiredCapabilities: { browserName: 'firefox' }
    })
;
browser
    .testMode()
    .init()
    .url("http://search.yahoo.com")
    .setValue("#yschsp", "javascript")
    .submitForm("#sf")
    .tests.visible('#resultCount', true, 'Got result count')
    .saveScreenshot('results.png')
    .end();

И теперь у вас есть прекрасный скриншот, показанный на рис. 6.1. Обратите внимание, что реклама Yahoo! Axis отображается посредине рис. 6.1. По идее она должна быть внизу видимой области страницы, но Selenium делает снимок всей страницы, независимо от того, поместились она целиком на экране или нет. Поэтому и получилось, что в данном случае видимая область закончилаась посере-