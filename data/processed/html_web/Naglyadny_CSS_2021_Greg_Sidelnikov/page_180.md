---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.65
tokens: 7172
characters: 749
timestamp: 2025-12-24T09:24:36.561238
finish_reason: stop
---

Чтобы назвать первую линию grid-макета, можно использовать свойство grid-template-column: [left] 100px. Для строк подойдет свойство grid-template-row: [top] 100px.

Можно присвоить имена нескольким линиям grid-макета. Скобки [] вставляются в интуитивно понятное место в коде. Именно там, где должна появиться линия (промежуток) grid-макета:

grid-template-columns:[left] 5px 5px [middle] 5px 5px [right]

Теперь можно использовать имена left, middle и right для ссылки на линии grid-макета при создании столбцов и строк, которые должны достичь данной области.

![Схема grid-макета с названиями линий](../images/grid-maketa.png)

Наименование линий промежутков создает более значимый навык. Целесообразно рассматривать среднюю линию в качестве центра