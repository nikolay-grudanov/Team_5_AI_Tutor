---
source_image: page_253.png
page_number: 253
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.69
tokens: 6231
characters: 1517
timestamp: 2025-12-24T10:07:47.102608
finish_reason: stop
---

debug.connect(function() {
    var msg = { command: 'continue' };
    debug.send(msg, function(req, resp) {
        console.log('REQ: ');
        console.log(req);
        console.log('RES: ');
        console.log(resp);
    });
});
});
Вы также можете запустить вашу программу и присоединиться к ней позже, используя следующую команду:

% node -debug myProgram.js

Используя API, предоставляемый движком V8, вы можете программно отправлять запросы и получать ответы от локального или удаленного отладчика.

Используя npm-модуль node-inspector(), вы можете использовать отладчик WebKit и средства разработчика для отладки ваших Node.js приложений:

% npm install node-inspector -g

Теперь вы можете загрузить ваше Node.js-приложение в отладчике:

% node -debug-brk myProgram.js

Запустите инспектор в фоновом режиме:

% node-inspector &

После этого откройте Chrome или Safari и откройте следующий URL: http://localhost:8080/debug?port=5858. Как будто по волшебству откроется отладчик и вы сможете отладить свое Node.js-приложение! Очень, очень удобно! Поскольку PhantomJS основан на WebKit, вы можете передать ему этот URL и открыть консоль отладчика в PhantomJS. На рис. 7.14 изображен снимок экрана PhantomJS, в котором выполняется отладчик WebKit.

Но и это еще не все. Вы можете управлять отладчиком удаленно! Об этом мы и поговорим в следующем разделе. А в завершении этого раздела еще раз подчеркнем важность и удобство использования браузеров Chrome или Safari для визуальной отладки ваших Node.js-приложений.