---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.71
tokens: 6252
characters: 1632
timestamp: 2025-12-24T10:07:03.206664
finish_reason: stop
---

});
// Далее все, как обычно. Вы можете запустить обычный
// тестовый код или какой-то специальный, HAR которого
// вам нужно получить
// Просто установите обратный вызов browsermob-proxy в 'end()'
browser
    .testMode()
    .init()
    .url("http://search.yahoo.com")
    .setValue("#yschsp", "JavaScript")
    .submitForm("#sf")
    .tests.visible('#resultCount', true, 'Got result count')
    .saveScreenshot('results.png')
    .end(cb);
}

Этот метод подразумевает, что browsermob-proxy запущен на том же хосте (localhost) и порту (8080), что и сценарий. Как уже было сказано, вы можете изменить данные значения в конструкторе Proxy. Этот метод также позволяет вам управлять взаимодействием Selenium, поэтому вы больше не нуждаетесь в параметрах selHost и selPort конструктора Proxy, если автономный сервер (selenium-server-standalone-2.x.x.x.jar) или сетка не работают на 4444 порте узла localhost.

Кроме того, не забывайте, что динамическая инъекция прокси Selenium работает только в Firefox и в Internet Explorer с использованием WebDriver (но не в Selenium1/Remote Control), таким образом, получается, что ваш объект webdriverjs должен использовать один из этих двух браузеров.

NPM-пакет browsermob-proxy также позволяет вам указать пропускную способность и задержку. Это полезно не только для генерации HAR, но и для тестирования медленного соединения, например, вы можете узнать, как будет загружаться ваш сайт с модема 56К и с задержкой 200 мс. Задать параметры пропускной полосы можно с помощью ключей downloadKbps и uploadKbps, а задержку — с помощью ключа latency:

    .proxy = new Proxy({
        downloadKbps: 56