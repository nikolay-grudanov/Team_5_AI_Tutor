---
source_image: page_228.png
page_number: 228
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.97
tokens: 5947
characters: 511
timestamp: 2025-12-24T10:06:58.163315
finish_reason: stop
---

Рис. 6.6. График производительности сервера, созданный nodeload

информацию об использовании памяти и процессора) каждые пять секунд:

var myLoop = new loop.Loop(
    function(linished, args) {
        getMemory();
        getCPU();
        finished();
    }
    , [] // Без аргументов
    , [] // Без условий
    , .2 // Каждые 5 секунд
);
myLoop.start();

Последний параметр в предыдущем коде — это максимальное число итераций цикла в секунду.

Заголовок следующего сценария устанавливает все наши переменные: