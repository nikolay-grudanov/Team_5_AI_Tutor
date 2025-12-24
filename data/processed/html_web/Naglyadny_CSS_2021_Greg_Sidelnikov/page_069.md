---
source_image: page_069.png
page_number: 69
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.00
tokens: 7061
characters: 548
timestamp: 2025-12-24T09:21:58.970435
finish_reason: stop
---

С помощью свойства text-anchor можно установить центральную точку, вокруг которой текст будет вращаться:

text-anchor: middle

![Пример текста с центром поворота в середину](../images/text-anchor-middle.png)

Чтобы установить центр поворота в самый конец текстового блока, свойству text-anchor следует задать значение end. Мы увидим похожее поведение в свойстве transform, которое можно использовать для поворота целых HTML-элементов и текста внутри них:

text-anchor: end

![Пример текста с центром поворота в конец](../images/text-anchor-end.png)