---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.63
tokens: 7217
characters: 876
timestamp: 2025-12-24T09:23:34.617023
finish_reason: stop
---

18.5. Создание 3D-куба

Вспомним, что мы знаем о 3D-трансформациях в CSS, и создадим трехмерный куб из шести HTML-элементов. Каждый из HTML-элементов перемещен на половину своей ширины и повернут на 90 градусов во всех направлениях:

![3D-куб с видами front, left, bottom](../images/ch18_3d_cube.png)

Это просто шесть HTML-элементов, каждый из которых имеет уникальный класс и 3D-трансформации:

<div class="view">
    <div class="cube">
        <div class="face front">front</div>
        <div class="face back">back</div>
        <div class="face right">right</div>
        <div class="face left">left</div>
        <div class="face top">top</div>
        <div class="face bottom">bottom</div>
    </div>
</div>

.view{
    width: 200px;
    height: 200px;
    perspective: 300px;
}

Вращая каждую грань вокруг гипотетического центра куба, мы можем построить наш 3D-объект: