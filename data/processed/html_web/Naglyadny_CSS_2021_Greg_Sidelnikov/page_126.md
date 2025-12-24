---
source_image: page_126.png
page_number: 126
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.07
tokens: 7184
characters: 836
timestamp: 2025-12-24T09:23:30.104208
finish_reason: stop
---

Обратите внимание: свойству backface-visibility присвоено значение hidden, чтобы скрыть элементы, направленные в сторону от камеры. Благодаря этому наш куб кажется твердым.

.cube{
    width: 100%;
    height: 100%;
    position: relative;
    transform-style: preserve-3d;
    transform: translateX(50px) translateY(50px);
}

.face{
    position: absolute;
    width: 100px;
    height: 100px;
    background: transparent;
    border: 2px solid red;
    text-align: center;
    line-height: 100px;
}

.front { transform: rotateY(0deg) translateZ(50px); }
.right { transform: rotateY(90deg) translateZ(50px); }
.back   { transform: rotateY(180deg) translateZ(50px); }
.left   { transform: rotateY(-90deg) translateZ(50px); }
.top    { transform: rotateX(90deg) translateZ(50px); }
.bottom{ transform: rotateX(-90deg) translateZ(50px); }