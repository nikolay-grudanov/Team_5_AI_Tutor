---
source_image: page_068.png
page_number: 68
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.58
tokens: 7085
characters: 603
timestamp: 2025-12-24T09:21:59.541261
finish_reason: stop
---

Можно добавить тень к тексту с помощью свойства text-shadow. Это свойство задает смещение вдоль осей X и Y, можно также настроить радиус размытия и цвет тени:

![Схема свойств text-shadow](../images/text-shadow.png)

Мы не станем глубоко вдаваться в SVG-контент, который тоже форматируется свойствами CSS. На эту тему можно написать целую книгу. Но в качестве краткой вставки — повернутый текст SVG создается следующим образом.

<svg>
    <text>
        CSS Is Awesome, that much we know. However, we need to write a bit more text here, in order to demonstrate how SVG rotations work.
    </text>
</svg>