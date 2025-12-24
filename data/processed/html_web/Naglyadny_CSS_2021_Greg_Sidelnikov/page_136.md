---
source_image: page_136.png
page_number: 136
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.48
tokens: 7129
characters: 527
timestamp: 2025-12-24T09:23:36.594422
finish_reason: stop
---

В каждом примере здесь значение элемента flex-grow было установлено как 1, 7, а в последнем из них — 3 и 5.

19.10. Свойство order

С помощью свойства order можно изменить порядок элементов:

.item {order: 0} (по умолчанию) для всех элементов

0
1
2
3
-1
-2, -1

order: 0   order: 0   order: 0   order: 0   order: 0
order: 1   order: 0   order: 0   order: 0   order: 0
order: 1   order: 0   order: 3   order: 0   order: 0
order: -1  order: 0   order: 0   order: 0   order: 0
order: -2  order: -1  order: 0   order: 0   order: 0