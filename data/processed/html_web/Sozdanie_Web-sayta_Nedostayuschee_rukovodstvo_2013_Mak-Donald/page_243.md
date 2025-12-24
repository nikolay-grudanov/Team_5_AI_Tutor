---
source_image: page_243.png
page_number: 243
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.28
tokens: 11642
characters: 1558
timestamp: 2025-12-24T09:37:26.374397
finish_reason: stop
---

margin-left: 70px;
margin-right: 70px;
padding: 10px;
border-style: double;
border-width: 3px;
color: white;
background-color: black;
font-size: large;
font-weight: bold;
font-family: Verdana, sans-serif;
}

В этом стиле задается фоновое изображение, устанавливаются поля и границы и выбираются согласующиеся цвета фона и переднего плана.

Далее приведен элемент <div>, использующий данный стиль.

<div class="pie">
    <p>Hungry for some pie?</p>
</div>

На рис. 7.15 показан результат.

Графические маркеры в списке

В главе 5 вы узнали, как применять элемент <ul> для создания маркированного списка. Но вы были ограничены маленьким набором стандартных стилей маркеров. Если же заглянуть в Интернет, можно найти более интересные примеры маркированных списков, включая списки с пользовательскими маркерами в виде крошечных картинок.

С помощью элемента <img> вы можете вставить свои маркеры вручную, но есть более удобный вариант. Для установки изображения в качестве маркера можно применить свойство list-style-image. Далее приведен пример, в котором используется картинка, названная 3Dball.gif.

ul {
    list-style-image: url('3Dball.gif');
}

После того как вы создали это стилевое правило и поместили его в свою таблицу стилей, ваш браузер автоматически применит его к стандартному маркированному списку, например, следующему.

<ul>
    <li>Are hard to miss</li>
    <li>Help compensate for feelings of inadequacy</li>
    <li>Look so darned cool</li>
    <li>Remind people of boring PowerPoint presentations</li>
</ul>

На рис. 7.16 показан результат.