---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.07
tokens: 6242
characters: 1637
timestamp: 2025-12-24T10:07:41.074614
finish_reason: stop
---

7.2. Отладка Node.js

Node.js поставляется вместе с отладчиком командной строки (http://nodejs.org/api/debugger.html), запустить который можно с помощью команды:

% node debug myscript.js

У отладчика есть набор небольших команд, просмотреть который можно, введя help:

    % node debug chrome.js
    < debugger listening on port 5858
    connecting... ok
    break in chrome.js:1
    1 var webdriverjs = require("webdriverjs")
    2 , fs = require('fs')
    3 , WebSocket = require('faye-websocket')
    debug> help
    Commands: run (r), cont (c), next (n), step (s), out (o),
    backtrace (bt), setBreakpoint (sb), clearBreakpoint (cb),
    watch, unwatch, watchers, repl, restart, kill, list, scripts,
    breakpoints, version
    debug>

Все эти команды тщательно документированы, но назначение базовых команд следующее: запуск, остановка, пошаговое выполнение кода, установка и удаление точек останова и просмотр переменных.

Довольно интересна команда repl. Она переключает отладчик в режим REPL (read-evaluate-print-loop), в котором вы можете выполнить с помощью eval любой JavaScript-код (в том числе и анализ переменных) в текущем контексте и области, в которой отладчик находится в тот момент. Другими словами, в этом режиме вы можете вводить любой код, например код, позволяющий выводить на консоль значение переменных, которые вы хотите просмотреть. Этот код будет передан функции eval() для выполнения. Выход из режима REPL возвратит вас в обычный режим отладчика, в котором вы можете вводить команды, перечисленные ранее.

Вы также можете использовать знакомый оператор debugger, позволяющий устанавливать точку останова.