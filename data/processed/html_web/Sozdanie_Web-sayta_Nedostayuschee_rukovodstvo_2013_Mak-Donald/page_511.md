---
source_image: page_511.png
page_number: 511
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.68
tokens: 11731
characters: 2041
timestamp: 2025-12-24T09:49:02.083837
finish_reason: stop
---

element.style.display = "block"
image.src = "open.png"

С другой стороны, если браузер выводит изображение в данный момент, код получает шанс проверить себя:

element.style.display = "none"
image.src = "closed.png

Для применения этой функции вам потребуется вставить элемент <img>, выполняющий переключение вашей Web-страницы. Вам также нужно добавить HTML-раздел, содержащий скрываемый контент. Вы можете показывать и скрывать практически любой HTML-элемент, но удачный универсальный вариант — элемент <div>, потому что в него можно вставить все, что вы захотите спрятать. Далее приведен пример.

<p>
    <img id="Question1Image" src="closed.png" alt="" onclick="ToggleVisibility('Question1Image','HiddenAnswer1')" />
    <b>Where has all the information gone?</b>
</p>

<div id="HiddenAnswer1">
    <p>Now you've found it. We've decided to hide parts of the page in these neat little collapsible sections. That way you won't see everything at once, panic, and do something drastic.</p>
</div>

В первой части разметки (между первыми тегами <p>) задан заголовок, который посетители видят всегда. Он содержит изображение стрелки и вопрос (выводимый жирным шрифтом). Вторая часть (в элементе <div>) — ответ, который ваш код то показывает, то скрывает.

Самое замечательное то, что вы можете многократно применять функцию для создания новых сворачиваемых разделов, потому что поместили в нее всю сложную обработку. Вновь создаваемые разделы будут иметь ту же структуру, но другое содержимое.

<p>
    <img id="Question2Image" src="closed.png" alt="" onclick="ToggleVisibility('Question2Image','HiddenAnswer2')" />
    <b>Can I read more than one answer at a time?</b>
</p>

<div id="HiddenAnswer2" style="display:none">
    <p>You can expand as many or as few sections as you want. Once you've expanded a section, just click again to collapse it back up out of sight. The only rule is that when you leave this page and come back later, everything will be hidden all over again. That's just the way JavaScript and Dynamic HTML work.</p>
</div>