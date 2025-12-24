---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.42
tokens: 6057
characters: 826
timestamp: 2025-12-24T10:08:02.312837
finish_reason: stop
---

Рис. 7.28. Расширенный код в инструментах разработчика Chrome

заменяются короткими (что сокращает код), но абстрактными и непонятными именами компилятором Closure Compiler (https://developers.google.com/closure/compiler/), поэтому у нас нет доступа к исходным именам переменных. На помощь приходят так называемые карты кода (source maps).

Карта кода — это один файл, содержащий один большой JSON-объект, который дает точное соответствие элементов готового рабочего кода проекта (после всех оптимизаций, минификаций и проч.) и вашего кода разработки.

Скажем больше: исходный код не обязательно должен быть JavaScript. Это очень приятный бонус!

Примечание.

Спецификации карт кода можно почитать по следующему адресу: https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRIpiOFzeOb-_2gc6fAHOKYOk/edit?hl=en_US&pli=1&pli=1.