---
source_image: page_214.png
page_number: 214
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.60
tokens: 6203
characters: 1453
timestamp: 2025-12-24T10:06:57.956045
finish_reason: stop
---

NPM-модуль browsermob-proxy может генерировать HAR двумя способами:

• Простой способ.

• Расширенный способ.

Давайте начнем с простого способа, который предпочтителен, если у вас есть один URL, водопадный график которого нужно просмотреть. Следующий код генерирует HAR-файл для Yahoo.com:

var Proxy = require('browsermob-proxy').Proxy
    , fs = require('fs')
    , proxy = new Proxy()
;
proxy.doHAR('http://yahoo.com', function(err, data) {
    if (err) {
        console.error('ERROR: ' + err);
    } else {
        fs.writeFileSync('yahoo.com.har', data, 'utf8');
    }
});
);

В приведенном коде мы загружаем модуль browsermob-proxy и создаем новый объект Proxy. Поскольку у этого объекта нет параметров, считается, что прокси browsermob-proxy запущен на localhost (порт 8080). Далее мы просто передаем URL и обратный вызов. Если нет ошибок, второй параметр нашего обратного вызова и будет HAR-данными для этого сайта. Нам остается только записать эти данные в файл.

Если ваш прокси не работает на localhost или вы используете другой порт, просто укажите это в конструкторе:

, proxy = new Proxy( { host: 'some.other.host', port: 9999 } )

Помните, что вам нужна версия 2.x сервера Selenium. При этом по умолчанию подразумевается, что Selenium Server работает на localhost и использует порт 4444. Если вам требуется задать другой порт, это можно сделать в конструкторе Proxy:

, proxy = new Proxy( { selHost: 'some.other.host', selPort: 6666 } )