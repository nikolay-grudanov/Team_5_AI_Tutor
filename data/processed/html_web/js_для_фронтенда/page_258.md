---
source_image: page_258.png
page_number: 258
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.85
tokens: 6164
characters: 1289
timestamp: 2025-12-24T10:07:46.759151
finish_reason: stop
---

, params: {
    maxCallStackDepth: 10
}
}
, messages = ''
;
ws.onopen = function(event) {
    ws.send(JSON.stringify(msg));
    ready();
};
ws.onmessage = function(event) {
    var obj = JSON.parse(event.data);
    if (obj.method && obj.method === 'Timeline.eventRecorded') {
        obj.record = obj.params.record; // Небольшой трюк
        messages += JSON.stringify(obj) + '\n';
    }
};
ws.onclose = function(event) {
    var header = '<html isdump="true">\n<body><span id="info">'
        + '</span>\n<div id="traceData" isRaw="true" version="0.26">'
        , footer = '</div></body></html>'
    ;
    ws = null;
    fs.writeFileSync('DUMP.speedtracer.html', header + messages
        + footer, 'utf8');
};

Помним, что протокол отладчика работает по веб-сокетному соединению. При этом в рамках вышеприведенного примера мы используем модуль faye-websocket, который обеспечивает превосходную клиентскую реализацию веб-сокетов.

Объект, предоставляемый startCapture, содержит свойство webSocketDebuggerUrl, являющееся веб-адресом сокета. После соединения с указанным адресом веб-сокета, модуль faye-websocket выпустит обратный вызов к функции onopen. А наша функция onopen отправит одно JSON-закодированное сообщение:

msg = {
    id: 777
    , method: "Timeline.start"
    , params: {