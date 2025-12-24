---
source_image: page_213.png
page_number: 213
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.41
tokens: 7235
characters: 895
timestamp: 2025-12-24T09:25:17.448354
finish_reason: stop
---

015    &:nth-child(#{$i}) {
016        animation-delay: ( #{sin(.4) * ($i)}s );
017    }
018    }
019 }
020
021 @keyframes oscillate {
022    0% { transform: translateY(0px); }
023    50% { transform: translateY(200px); }
024 }

А это HTML-часть, сокращенный вариант примера. Убедитесь, что у вас есть 15 реальных HTML-элементов с классом class = "atom".

001 <!-- повторять данный элемент 15 раз //-->>
002 <div class = "atom"></div>

В результате будет создана следующая анимированная синусоида.

![Синусоида из 15 кругов](../images/sinusoid.png)

Весь код занял менее 24 строк!

ПРИМЕЧАНИЕ
Если вы используете инфраструктуру Vue, то можете визуализировать все 15 элементов, задействуя этот простой цикл for, с помощью директивы v-for, вместо того чтобы вводить все 15 HTML-элементов вручную.

Настройка для отображения 15 HTML-элементов с помощью всего лишь нескольких строк кода в среде Vue: