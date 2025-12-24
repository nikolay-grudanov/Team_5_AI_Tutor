---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.20
tokens: 7139
characters: 599
timestamp: 2025-12-24T09:23:42.377674
finish_reason: stop
---

строку, где каждый из них наследует свою ширину от элемента grid-контейнера.

Автоматическое размещение:
по строкам (по умолчанию)

grid-auto-flow: row

<div style = "display: grid">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
</div>

Автоматическое размещение:
по столбцам

grid-auto-flow: column

Как и flex-макет, grid-разметка может выравнивать элементы в одном из двух направлений: по строкам или столбцам, заданных свойством grid-auto-flow.

Элементы: <div>1</div> <div>2</div> <div>3</div>

grid-template-columns: 25px 25px 25px 25px 25px 25px 25px

grid-template-rows: 25px 25px 25px