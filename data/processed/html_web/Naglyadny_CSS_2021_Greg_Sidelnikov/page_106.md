---
source_image: page_106.png
page_number: 106
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.86
tokens: 7130
characters: 781
timestamp: 2025-12-24T09:22:58.985856
finish_reason: stop
---

Получаем следующий результат.

![Повторяющийся фон с изображением собаки](../images/ch12-03.png)

Существуют и другие свойства фона, которые также принимают списки, разделенные запятыми. Это почти все остальные свойства, связанные с фоном, кроме background-color.

Таким же образом можно присвоить иные параметры для каждого отдельного фона с помощью других свойств фона, показанных ниже:

001 background
002 background-attachment
003 background-clip
004 background-image
005 background-origin
006 background-position
007 background-repeat
008 background-size

Следующее свойство нельзя использовать со списком по очевидным причинам:

001 background-color

Что бы это значило — обеспечить несколько значений цвета для фона? Всякий раз, когда задается свойство background-color, оно