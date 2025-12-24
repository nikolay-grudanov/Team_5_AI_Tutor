---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.80
tokens: 7167
characters: 817
timestamp: 2025-12-24T09:22:46.001961
finish_reason: stop
---

Посмотрим на тот же фон котенка... только с установленным значением background-repeat: no-repeat:

Далее показаны результаты, созданные с помощью свойства background-size. Слева направо приведены следующие примеры: (unset — none — initial — auto), которые приводят к значению по умолчанию.

background-size: unset;
background-size: none;
background-size: initial;
background-size: auto;

background-size: 100%;
background-size: 100% 100%; background-size: cover; background-size: contain;

background-size: 50%; (ось X)
background-size: 50% 50%; (ось X)(ось Y)

Значение 100% растянет изображения по горизонтали, но не по вертикали. Значение 100% 100% растянет изображение по всему доступному пространству. Значение cover растянет изображение по всему вертикальному пространству элемента, обрежет все в горизонтальном