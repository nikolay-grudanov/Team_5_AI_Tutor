---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.80
tokens: 7277
characters: 1319
timestamp: 2025-12-24T09:22:15.533077
finish_reason: stop
---

6.4. Свойство text-decoration-skip-ink

Свойство text-decoration-skip-ink отвечает за отображение линий под/над текстом, когда они пересекают глифы. Это на самом деле полезно для улучшения визуальной целостности заголовков страниц или любого подчеркнутого текста, в котором используются большие буквы.

You should go and grab a cup of coffee.
text-decoration: underline solid blue
text-decoration-skip-ink: none

You should go and grab a cup of coffee.
text-decoration: underline solid blue
text-decoration-skip-ink: auto

6.5. Свойство text-rendering

Данное свойство, возможно, не вызовет заметных различий в четырех его проявлениях (auto, optimizeSpeed, optimizeLegibility и geometryPrecision). Но считается, что в некоторых браузерах, использующих значение optimizeSpeed этого свойства, улучшается скорость рендеринга больших блоков текста. Значение optimizeLegibility — единственное, на самом деле создававшее физическое различие в отображении текста в наших экспериментах с браузером Chrome, смещающая слова ближе друг к другу в отдельных комбинациях символов.

Названия четырех использованных значений отражают их суть:

CSS Is Awesome.
text-rendering: auto;

CSS Is Awesome.
text-rendering: optimizeSpeed;

CSS Is Awesome.
text-rendering: optimizeLegibility;

CSS Is Awesome.
text-rendering: geometricPrecision;