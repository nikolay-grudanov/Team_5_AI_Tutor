---
source_image: page_148.png
page_number: 148
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.50
tokens: 11711
characters: 1832
timestamp: 2025-12-24T09:33:19.400284
finish_reason: stop
---

Текстовые элементы

СОВЕТ
В современных редакторах Web-страниц есть очень удобные инструменты списков, поэтому вы можете быстро создать списки разных типов. В Dreamweaver ищите пиктограммы "ul" и "ol" на вкладке Text (Текст) панели инструментов Insert (Вставка).

Списки определений

Списки определений очень удобны для создания вашего собственного словаря терминов. У каждого пункта списка есть две части: термин (для которого браузер не создает отступа) и определение (которое браузер с отступом помещает под термином). В списках определений применяется несколько иная система разметки, чем в нумерованных и маркированных списках. Во-первых, вы помещаете весь список в элемент <dl> (словарный список). Затем вы помещаете каждый термин в элемент <dt> (словарный термин), а каждое определение — в элемент <dd> (словарное определение). Далее приведен пример.

<dl>
<dt>eat</dt>
<dd>To perform successively (and successfully) the functions of mastication, humectation, and deglutition.</dd>
<dt>eavesdrop</dt>
<dd>Secretly to overhear a catalogue of the crimes and vices of another or yourself.</dd>
<dt>economy</dt>
<dd>Purchasing the barrel of whiskey that you do not need for the price of the cow that you cannot afford.</dd>
</dl>

В браузере вы увидите следующее:

eat
    To perform successively (and successfully) the functions of mastication, humectation, and deglutition.
eavesdrop
    Secretly to overhear a catalogue of the crimes and vices of another or yourself.
economy
    Purchasing the barrel of whiskey that you do not need for the price of the cow that you cannot afford.

Вложенные списки

Списки и сами по себе очень полезны, но можно добиться большего, поместив целиком один список в другой. Этот прием называется вложением списков, и он позволяет создать многоуровневые оглавления и подробные наборы инструкций.