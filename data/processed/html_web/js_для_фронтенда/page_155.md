---
source_image: page_155.png
page_number: 155
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.09
tokens: 6096
characters: 1522
timestamp: 2025-12-24T10:05:41.749381
finish_reason: stop
---

, port: 4444
    , desiredCapabilities: { browserName: 'firefox' }
});
;
browser.init().url(url).waitFor('#testresults', 10000, function(found) {
    if (found) {
        var res = browser.getText('#testresults'
            ,function(text) {
                // Получаем сообщения журнала и результаты JUnit XML
                console.log(JSON.parse(unescape(text.value)));
                // Получаем снимок экрана
                browser.screenshot(
                    function(screenshot) {
                        var fs = require('fs')
                            , filename = 'snapshot.png'
                            , imageData
                        ;
                        try {
                            imageData =
                                new Buffer(screenshot.value
                                    , 'base64');
                            fs.writeFileSync(filename, imageData);
                        } catch(e) {
                            console.log('Ошибка получения снимка: '
                                + e);
                        }
                    }
                );
            }
        );
    } else {
        console.log('РЕЗУЛЬТАТЫ ТЕСТА НЕ НАЙДЕНЫ!');
    }
}).end();

Во время сборки вы будете использовать более интеллектуальный способ передачи всех ваших тестов драйверам вместо указания имени файла или URL непосредственно в самом коде.

Основная проблема Selenium заключается в его медлительности: запуск сеанса браузера для каждого теста или набора тестов —