---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.15
tokens: 7129
characters: 580
timestamp: 2025-12-24T09:22:19.862923
finish_reason: stop
---

8 Логотип Nike

Комбинируя приемы из предыдущей главы со свойством transform: rotate (далее будет рассматриваться более подробно) и наши знания псевдоселекторов :before и :after, можно создать логотип Nike из одного HTML-элемента.

![Логотип Nike](../images/nike_logo.png)

Определим наш основной контейнер:

1 #nike {
2   position: absolute;
3   top: 300px; left: 300px;
4   width: 470px; height: 200px;
5   border: 1px solid gray;
6   overflow: hidden;
7   font-family: Arial, sans-serif;
8   font-size: 40px;
9   line-height: 300px;
10  text-indent: 350px;
11  z-index: 3;
12 }