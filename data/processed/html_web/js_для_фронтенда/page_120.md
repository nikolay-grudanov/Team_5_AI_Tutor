---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.82
tokens: 6224
characters: 1542
timestamp: 2025-12-24T10:05:01.516576
finish_reason: stop
---

работает на той же машине, что и клиент, но, конечно же, может работать и на другом узле). Просто запустите данный файл:

% node client.js

Теперь любое событие ADD_USER, сгенерированное любым клиентом, будет перенаправлено этой функции. Рассмотрим клиент, выполняющийся в браузере с использованием YUI3:

<script src="http://yui.yahooapis.com/3.18.1/build/yui/yui-min.js">
</script>
<script src="/socket.io/socket.io.js"></script>
<script src="/clients/browser/yui3.js"></script>
<script>
    YUI().use('node', 'EventHub', function(Y) {
        var hub = new Y.EventHub(io, 'http://myhost:5883');
        hub.on('eventHubReady', function() {
            hub.on('ADD_USER_DONE', function(data) { });
            ... спустя некоторое время ...
            hub.fire('ADD_USER', user);
        });
    });
</script>

После загрузки YUI3, библиотеки socket.io и YUI3-клиента EventHub будет инстанцирован новый экземпляр коммутатора EventHub. Когда все будет готово, мы начинаем прослушивать события и порождаем событие ADD_USER. Все просто.

Далее приведен тот же пример с использованием jQuery:

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js">
</script>
<script src="/socket.io/socket.io.js"></script>
<script src="/clients/browser/jquery.js"></script>
<script>
    var hub = new $.fn.eventHub(io, 'http://myhost:5883');
    hub.bind('eventHubReady', function() {
        hub.bind('ADD_USER_DONE', function(data) { });
        ... Спустя некоторое время ...
        hub.trigger('ADD_USER', user);
    });
</script>