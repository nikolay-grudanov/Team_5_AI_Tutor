---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.97
tokens: 7302
characters: 1255
timestamp: 2025-12-24T09:25:19.515256
finish_reason: stop
---

&-fender {
    position: absolute;
    top: -2px;
    left: -100px;
    width: 260px;
    height: 65px;
    border-radius: 30px 20px 40px 20px;
    background-color: #ce4038;
    border: 4px solid;
    border-color: $border;
    z-index: $car-rear;
    overflow: hidden;
    box-shadow: inset 0 4px 0 rgba(#fff, 0.17),
        inset -5px -4px 0 rgba(#333, 0.2);
}

&-tire {
    .front, .rear {
        width: 60px;
        height: 60px;
        background: $border;
        position: absolute;
        border-radius: 50%;
        top: 22px;
        z-index: $tire;
        display: flex;
        justify-content: center;
        align-items: center;
        &:before {
            position: absolute;
            width: 60px;
            height: 60px;
            content: "";
            border: 5px solid #333;
            opacity: 0.2;
            border-radius: 50%;
        }
    }
}

Здесь символ & означает ключевое слово this (концептуально похожее на объект this в JavaScript), то есть... элемент ссылается сам на себя. Как уже было показано в одной из глав, псевдоселекторы :before (а также :after) фактически содержатся в одном и том же HTML-элементе. Их можно применять для создания дополнительных фигур без необходимости добавления элементов.