---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.42
tokens: 7218
characters: 898
timestamp: 2025-12-24T09:25:18.620738
finish_reason: stop
---

Все зависит от того, насколько творчески вы подходите к свойствам CSS: hidden, transform:rotate, box-shadow и border-radius.

Если сделать все фоны прозрачными, то можно ясно видеть композицию Tesla, состоящую из нескольких HTML-элементов div:

Далее мы разберем каждый значимый элемент автомобиля, чтобы продемонстрировать, как он был создан.

.face {
    position: absolute;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #f2f2f2;
    top: -60px;
    left: -10px;
    border: 4px solid $border;
    overflow: hidden;
    box-shadow: inset -4px -4px 0 rgba(#333, 0.2);
}

&:before {
    position: absolute;
    content: "";
    width: 17px;
    height: 17px;
    border-radius: 3px;
    background: #f7ac76;
    transform: rotate(-45deg);
    left: -7px;
    top: 7px;
    border: 2px solid $border;
    box-shadow:
        inset -5px 5px 3px 0 rgba(#fff, 0.4);
}