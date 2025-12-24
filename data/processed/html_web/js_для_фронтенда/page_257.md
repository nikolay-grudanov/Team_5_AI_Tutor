---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.04
tokens: 6204
characters: 1591
timestamp: 2025-12-24T10:07:50.817014
finish_reason: stop
---

startCapture для «захвата» всей информации по таймингам, которую позволяет предоставить Chrome, включая время передачи по сети, время прорисовки, время разметки и т.д.

Далее приведен код функции startCapture:

function startCapture(ready) {
    var http = require('http')
        , options = {
            host: 'localhost'
            , port: 9222
            , path: '/json'
        }
    ;
    http.get(options, function(res) {
        res.on('data', function (chunk) {
            var resObj = JSON.parse(chunk);
            connectToDebugger(resObj[0], ready);
        });
    }).on('error', function(e) {
        console.log("Got error: " + e.message);
    })
}

При посещении http://localhost:9222/json будет получен ответ JSON, который является массивом вкладок, которые могут использоваться при удаленной отладке. Так как мы открыли этот экземпляр Chrome с Selenium, у нас есть только одна вкладка, следовательно, будет только один объект в массиве. Обратите внимание на то, что webdriverjs передал функции startCapture функцию обратного вызова, которая будет вызвана, как только startCapture завершит работу. Эта функция подключится к локальному (или удаленному) экземпляру Chrome, получит JSON-данные о текущей вкладке, которую мы хотим отладить, а затем передаст эту информацию функции connectToDebugger, приведенной ниже:

function connectToDebugger(obj, ready) {
    var fs = require('fs')
        , WebSocket = require('faye-websocket')
        , ws = new WebSocket.Client(obj.webSocketDebuggerUrl)
        , msg = {
            id: 777
            , method: "Timeline.start"