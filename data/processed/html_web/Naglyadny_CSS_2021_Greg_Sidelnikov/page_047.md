---
source_image: page_047.png
page_number: 47
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.57
tokens: 7127
characters: 715
timestamp: 2025-12-24T09:21:30.562883
finish_reason: stop
---

В CSS нет margin-box, поскольку внешние отступы по определению всегда относятся к пространству, окружающему содержимое:

![CSS Is Awesome](../images/ch02-01.png)

HTML-элемент сложнее, чем кажется на первый взгляд:

![Схема HTML-элемента с :after и :before](../images/ch02-02.png)

Элементы :before и :after являются частью одного HTML-элемента. Вы даже можете применить к ним position: absolute и организовать их вокруг без создания каких-либо новых элементов!

:before
#container2:before {
    content: ":before";
    background: white;
    border: 10px solid #3586FF;
    width: 130px;
}

:after
#container2:after {
    content: ":after";
    background: yellow;
    border: 10px solid orange;
    left: 150px;
}