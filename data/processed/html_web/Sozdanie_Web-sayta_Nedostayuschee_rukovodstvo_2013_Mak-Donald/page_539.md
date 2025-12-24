---
source_image: page_539.png
page_number: 539
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.46
tokens: 11752
characters: 1786
timestamp: 2025-12-24T09:50:15.981966
finish_reason: stop
---

.Tab {
    font-weight: bold;
    padding: 5px;
    border-style: solid;
    border-width: 1px;
    cursor: hand;
}

В это правило включено кое-что, чего вы еще не видели — свойство cursor. Оно задает стиль указателя мыши, появляющегося, когда гость наводит мышь на ссылку. В данном случае указатель мыши меняется на пиктограмму кисти руки (рис. 16.7, посередине).

Вы заключаете все вкладки в элемент <div>, использующий класс TabGroup. Это позволит поместить TabGroup в определенное место на странице.

.TabGroup
{
    position: absolute;
    top: 16px;
    left: 10px;
}

После того как вкладки определены, имеет смысл вставить плавающие подменю. Каждое подменю — это просто окно с границами и фоном желтого цвета. Внутри вы найдете группу ссылок. Здесь подходит элемент <div>, т. к. вы хотите, чтобы каждое подменю отображалось на странице независимо (вместо соединения всех подменю в одной строке). Кроме того, необходимо присвоить каждому элементу <div> уникальный ID, чтобы можно было менять видимость элемента, основываясь на вкладке, которую посетитель щелкнул мышью.

Далее приведены элементы <div> для трех групп ссылок.

<div id="AboutMe" class="Links">
    <a href="...">My Traumatic Childhood</a>
    <a href="...">My Education</a>
    <a href="...">Painful Episodes</a>
</div>
<div id="MyStore" class="Links">
    <a href="...">Buy Something</a>
    <a href="...">Request a Refund</a>
    <a href="...">File a Complaint</a>
</div>
<div id="ReallyCoolStuff" class="Links">
    <a href="...">Pie Eating</a>
    <a href="...">Harvesting Bananas</a>
    <a href="...">Blindfolded Heart Surgery</a>
</div>

Элементы <div> отображаются поверх страницы, а это значит, что вы должны применить абсолютное позиционирование для них. Далее приведено соответствующее стилевое правило.