---
source_image: page_538.png
page_number: 538
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.68
tokens: 11392
characters: 658
timestamp: 2025-12-24T09:49:44.091832
finish_reason: stop
---

Рис. 16.7. Вверху: когда эта страница загружается в первый раз, она представляет посетителям всего три вкладки.
Посередине и внизу: когда посетитель наводит указатель мыши на заголовок вкладки, под вкладкой появляется набор связанных ссылок. Эти ссылки "наплывают" на контент страницы

Далее приведен HTML-код, представляющий три вкладки.

<div class="TabGroup">
    <span class="Tab">About Me</span>
    <span class="Tab">My Store</span>
    <span class="Tab">Really Cool Stuff</span>
</div>

У этих элементов <span> описательное имя класса — Tab. Оно связывает элементы со следующим правилом таблицы стилей, задающим для вкладок подходящий шрифт и границы.