---
source_image: page_148.png
page_number: 148
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.21
tokens: 6212
characters: 1392
timestamp: 2025-12-24T10:05:34.741895
finish_reason: stop
---

yconsole.on('entry',
    function(obj) {
        console.log(JSON.stringify(obj.message));
    }
);
if (typeof(console) !== 'undefined') {
    var TR = Y.Test.Runner;
    TR.subscribe(TR.COMPLETE_EVENT, function(obj) {
        console.log(JSON.stringify(
            { results: Y.Test.Format.JUnitXML(obj.results) }));
    });
}
}, '1.0', { requires: [ 'console' ] });

Самое большое дополнение — объект Y.Console, который мы создали исключительно для захвата сообщений протоколирования YUI Test. Прослушка события entry даст нам все сообщения объекта, которые мы строколизировали с использованием JSON (обратите внимание, что объект JSON включен в WebKit, а наш JavaScript-код выполняет браузер PhantomJS/WebKit).

Теперь у нас два типа сообщений, выведенных на консоль, передаются «обратно» нашему сценарию PhantomJS: сообщения протоколирования и окончательные результаты JUnit XML. Код PhantomJS на стороне сервера должен отслеживать оба типа сообщений.

Вот первое сообщение:

{
    "time":"2015-02-23T02:38:03.222Z",
    "message":"Testing began at Wed Feb 22 2015 18:38:03 GMT-0800 (PST).",
    "category":"info",
    "sourceAndDetail":"TestRunner",
    "source":"TestRunner",
    "localTime":"18:38:03",
    "elapsedTime":24,
    "totalTime":24
}

Информацию о том, что означает то или иное поле сообщения, можно найти на веб-сайте YUI: http://yuilibrary.com/yui/docs/console/#anatomy.