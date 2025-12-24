---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.57
tokens: 6154
characters: 1365
timestamp: 2025-12-24T10:06:39.377143
finish_reason: stop
---

Вторая и третья версия, конечно же, лучше, функциональнее и позволяет более эффективно управлять браузерами, но достоинство Selenium 1, из-за которого еще не забыли окончательно, состоит в том, что его в принципе поддерживает большее количество браузеров, так как практически каждый браузер может понять и исполнить JavaScript-код. Вот в таком контексте вам и может пригодиться Selenium RT.

Аналогом webdriverjs под Selenium Remote Control является отличный npm-модуль soda (https://github.com/LearnBoost/soda). И ниже приведен тот же пример, что и раньше, но с использованием модуля soda и браузера Safari:

var soda = require('soda')
    , browser = soda.createClient({
        url: 'http://search.yahoo.com'
        , host: 'localhost'
        , browser: 'safari'
    })
    ;
browser
    .chain
    .session()
    .open('/')
    .type('yschsp', 'JavaScript')
    .submit('sf')
    .waitForPageToLoad(5000)
    .assertElementPresent('resultCount')
    .end(function(err) {
        browser.testComplete(function() {
            if (err) {
                console.log('Test failures: ' + err);
            } else {
                console.log('success!');
            }
        });
    });
Модуль soda подобен модулю webdriverjs, но теперь вместо Selenium-команд вы используете Selenium1-команды (http://release.seleniumhq.org/selenium-core/1.0.1/reference.html).