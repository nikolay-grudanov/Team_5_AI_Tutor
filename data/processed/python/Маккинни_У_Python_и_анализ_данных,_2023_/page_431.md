---
source_image: page_431.png
page_number: 431
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.55
tokens: 7069
characters: 286
timestamp: 2025-12-24T02:51:50.323468
finish_reason: stop
---

Далее вызов movies.explode("genre") генерирует новый объект DataFrame, содержащий по одной строке для каждого «внутреннего» элемента в каждом списке жанров. Например, если фильм классифицирован как комедия и мелодрама, то в результирующем объекте будет две строки: "Comedy" и "Romance":