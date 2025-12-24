---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.22
tokens: 7314
characters: 1317
timestamp: 2025-12-24T09:25:19.591702
finish_reason: stop
---

Шлем состоит из круга и оранжевого лицевого щитка, который представляет собой просто вложенный повернутый квадрат с тенью box-shadow, отрезаемый по линии радиуса, так как для .face установлено значение overflow: hidden.

Обратите внимание, как псевдоэлемент &:before вкладывается внутрь .face с помощью {скобок}. Это достигается с помощью расширения SASS (Syntactically Awesome Style Sheets). Более подробную информацию можно посмотреть, перейдя по ссылке SASS-lang.com. Кроме того, кратко SASS обсуждается в самом начале книги.

Конечно, вы все еще можете переписать код в стандартном виде CSS, заменив &:before и скобки отдельным элементом с собственным идентификатором или классом.

&-bumper-top {
    width: 135px;
    height: 23px;
    position: absolute;
    background-color: $car-body;
    border: 4px solid;
    border-radius: 50%;
    top: -8px;
    left: -235px;
    transform: rotate(1deg);
    border-color: $border transparent transparent $border;
    overflow: hidden;
    z-index: 99;
    box-shadow: inset 0 3px 0 rgba(#fff, 0.17);

    .front-light-bulb {
        position: absolute;
        width: 33px;
        height: 10px;
        background:
            rgba(#fff, 0.5);
        transform:
            rotate(-10deg);
        border-radius: 50px 0;
        left: -4px;
        top: 1px;
    }
}