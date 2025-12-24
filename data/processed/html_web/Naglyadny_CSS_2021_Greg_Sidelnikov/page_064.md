---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.35
tokens: 7190
characters: 922
timestamp: 2025-12-24T09:22:10.153501
finish_reason: stop
---

6.6. Свойство text-indent

Данное свойство отвечает за выравнивание текста. Применяется редко, но в некоторых случаях, например на новостных сайтах или в текстовых редакторах, может оказаться полезным.

100px
You should go and grab a cup of coffee.
text-indent: 100px

-100px
You should go and grab a cup of coffee.
text-indent: -100px

6.7. Свойство text-orientation

Данное свойство определяет направление текста. Может быть полезно для рендеринга разных языков, в которых поток текста проходит справа налево или сверху вниз. Часто применяется вместе со свойством writing-mode.

You should go and grab a cup of coffee.
text-orientation: mixed

You should go and grab a cup of coffee.
text-orientation: upright

Вместе со свойством writing-mode: vertical-rl (справа налево) или writing-mode: vertical-lr (слева направо) свойство text-orientation можно использовать для выравнивания текста практически в любом направлении.