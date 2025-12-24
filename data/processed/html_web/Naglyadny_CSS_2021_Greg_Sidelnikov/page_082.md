---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.71
tokens: 7041
characters: 466
timestamp: 2025-12-24T09:22:18.124806
finish_reason: stop
---

10 Свойство visibility

Свойство visibility скрывает или показывает элемент без изменения разметки документа.

Далее показан результат присвоения свойству visibility элемента b значения hidden. По умолчанию установлено значение visible (аналогично unset, или auto, или none).

.b {visibility: visible}
.a   .b   .c

.b {visibility: hidden}
.a   .c

Здесь свойство display: none полностью удаляет элемент.

.b {display: block}
.a   .b   .c

.b {display: none}
.a   .c