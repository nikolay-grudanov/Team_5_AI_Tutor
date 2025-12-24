---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.72
tokens: 6212
characters: 1560
timestamp: 2025-12-24T10:06:58.117917
finish_reason: stop
---

Теперь давайте рассмотрим расширенный способ создания HAR-файлов. Данный подход нужно использовать, если требуется создать HAR-файл для более сложного веб-взаимодействия, чем просто загрузка страницы. Используя этот метод, вы можете установить прокси, он начнет захват данных, а модуль browsermob-proxy будет связующим звеном между кодом Selenium и прокси.

Для этого примера мы будем использовать ранее приведенный пример использования Selenium webdriverjs загрузки страницы Yahoo! и поиска строки "JavaScript". Сначала мы создадим HAR для всего этого взаимодействия:

var Proxy = require('browsermob-proxy').Proxy
    , webdriverjs = require("webdriverjs")
    , fs = require('fs')
    , proxy = new Proxy();
/*
* Прокси вызывается с "именем" для этого сеанса, функцией Selenium
* для захвата и обратным вызовом, который запишет HAR-данные
* в файл или выведет на консоль сообщение об ошибке
*/
proxy.cbHAR('search.yahoo.com', doSeleniumStuff, function(err, data) {
    if (err) {
        console.error('Ошибка захвата HAR: ' + err);
    } else {
        fs.writeFileSync('search.yahoo.com.har', data, 'utf8');
    }
});
/*
* Это функция Selenium, которой передается прокси webdriverjs и обратный вызов,
* который должен быть вызван, как только взаимодействие будет завершено.
*/
function doSeleniumStuff(proxy, cb) {
    var browser = webdriverjs.remote({
        host: 'localhost'
        , port: 4444
        , desiredCapabilities: {
            browserName: 'firefox'
            , seleniumProtocol: 'WebDriver'
            , proxy: { httpProxy: proxy }
