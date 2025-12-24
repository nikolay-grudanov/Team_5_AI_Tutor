---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.38
tokens: 6303
characters: 1664
timestamp: 2025-12-24T10:07:09.798125
finish_reason: stop
---

} else {
    fs.writeFileSync('casper.har', data, 'utf8');
}
});
function doCasperJSStuff(proxy, cb) {
    casperjs = spawn('bin/casperjs'
        , [ '--proxy=' + proxy, process.argv[2] ]);
    casperjs.on('exit', cb);
}

Мы используем proxy.selHAR, как и в предыдущем примере, но вместо Selenium-функции мы используем функцию CasperJS. При этом прокси установлен в browsermob. Как только процесс CasperJS завершает работу, мы получаем HAR-файл. Использовать же этот сценарий нужно так:

% node casperHAR.js casperScript.js

Где casperHAR.js — это файл, содержащий предыдущий код, а casperScript.js — любой сценарий CasperJS (например, приведенный ранее сценарий для поиска в Yahoo!). Как и в случае с Selenium, вы можете указать имя компьютера и порт, где запущен прокси browsermob, а также ограничить пропускную способность.

Просмотр HAR-файлов

Визуализация данных в HAR-файлах очень проста. Самый легкий способ — использовать онлайн средство просмотра: http://www.softwareishard.com/har/viewer/. Просто перетягните HAR-файл на эту страницу (для этого нужно использовать современный браузер, поддерживающий HTML5), и вы увидите водопадный график HAR-данных. Только перед загрузкой вашего HAR-файла убедитесь, что вы выключили переключатель Validate data before processing?3.

Рис. 6.3 показывает HAR-файл для нашего примера search.yahoo.com.

Из графика видно, что мы сделали 10 запросов, а полная загрузка страницы заняла целых 8.25 с. Если подвести мышь к каждому запросу, вы увидите, сколько времени занял этот конкретный запрос в следующем порядке: Разрешение DNS (DNS Lookup), Подключа-

3 Я еще ни разу не сталкивался с корректной валидацией HAR-файлов.