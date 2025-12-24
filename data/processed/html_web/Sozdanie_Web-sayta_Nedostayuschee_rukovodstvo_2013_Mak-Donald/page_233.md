---
source_image: page_233.png
page_number: 233
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.49
tokens: 11433
characters: 868
timestamp: 2025-12-24T09:36:26.224651
finish_reason: stop
---

<div class="Box">
    <p>
        <img src="food.jpg" alt="A Meal" class="FloatLeft" />
        <b>But Wait!</b> A tip box can interrupt the discussion to let you know just how good mixed veggies can taste.
        Of course, this tip box is really just an ordinary paragraph with the right border and margin style properties.
    </p>
</div>

Затем с помощью стилевого правила можно задать изящную рамку для элемента <div>.

div.Box {
    margin-top: 20px;
    margin-bottom: 10px;
    margin-left: 70px;
    margin-right: 70px;
    padding: 5px;
    border-style: dotted;
    border-width: 2px
}

На рис. 7.10 показан результат.

![Пример использования стилей для размещения картинок и текста](./images/chapter7/wrappedBox.png)

Рис. 7.10. Искусно применяя стили, можно размещать картинки на странице с той же ловкостью, какую обеспечивают стили при работе с текстом