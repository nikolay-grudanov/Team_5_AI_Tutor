---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.44
tokens: 7349
characters: 1399
timestamp: 2025-12-24T09:25:19.967133
finish_reason: stop
---

Капот представляет собой длинный овальный элемент, повернутый всего на 1 градус. Как и лицевой щиток шлема, лампочка скрывается внутри родительского элемента с помощью свойства overflow: hidden. Сокрытие потока — то, что помогает создавать более сложные неправильные формы, точно описывающие реальные объекты.

Важность свойства overflow: hidden в создании стилей CSS невозможно переоценить. Подсветка использует абсолютно ту же технику, что и в предыдущих двух примерах. Задняя часть автомобиля представляет собой повернутый прямоугольник с одним из закругленных углов. Здесь вы просто должны следовать своему внутреннему чутью для создания форм, соответствующих вашим предпочтениям и стилю.

```css
&-rear-top {
    position: absolute;
    width: 113px;
    height: 33px;
    background-color: $car-body;
    top: -25px;
    left: 50px;
    border-radius: 0 70% 0 0;
    transform: rotate(9.2deg);
    border: 4px solid;
    border-color: $border transparent transparent;
    z-index: $hand;
    box-shadow: inset 0 4px 0 rgba(#ff0, 0.17);
}
.back-light {
    position: absolute;
    width: 23px;
    height: 10px;
    background-color: $border;
    top: 27px;
    left: 94px;
    z-index: 0;
    border-radius: 0px 0 0 50px;
}
```

Основание автомобиля, которое тянется к его задней части, представляет собой большой прямоугольный div-элемент с закругленными углами и внутренней тенью box-shadow.