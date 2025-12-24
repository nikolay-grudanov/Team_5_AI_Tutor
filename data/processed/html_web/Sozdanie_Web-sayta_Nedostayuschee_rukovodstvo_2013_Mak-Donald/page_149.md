---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.18
tokens: 11599
characters: 1352
timestamp: 2025-12-24T09:33:15.502962
finish_reason: stop
---

![Weekly Schedule](../images/ch5_12.png)

Рис. 5.12. Когда списки вкладывают друг в друга, браузеры создают отступы для списков каждого уровня. Хотя количество уровней не ограничено, в конечном счете вы займете все пространство окна вашего браузера и ваш текст упрется в правый край страницы

Для вложения списка опишите новый список внутри элемента <li> уже имеющегося списка. Например, в следующем списке повседневных дел три уровня.

<ul>
<li>Monday
<ol>
<li>Plan schedule for week</li>
<li>Complete Project X
<ul style="square">
<li>Preliminary Interview</li>
<li>Wild Hypothesis</li>
<li>Final Report</li>
</ul>
</li>
<li>Abuse underlings</li>
</ol>
</li>
<li>Tuesday
<ol>
<li>Revise schedule</li>
<li>Procrastinate (time permitting). If necessary, put off procrastination until another day.</li>
</ol>
</li>
<li>Wednesday
<ol>
<li>Try to complete Monday tasks</li>
<li>Write progress report. Consider ways to pad progress port.
<ul>
<li>"Intentionally left blank" sections</li>
<li>Font sizes above 20pt</li>
<li>Risqué pictures</li>
</ul>
</li>
</ol>
</li>
<li>Thursday
<ol>
<li>Determine why Project X isn't complete</li>
<li>Research scapegoat possibilities
<ul>
<li>Boss</li>
<li>Co-workers</li>
<li>One-armed man</li>
</ul>
</li>
</ol>
</li>
<li>Friday
<ol>
<li>Defer tasks to next week</li>
<li>Disrupt weekly meeting</li>
</ol>
</li>
</ul>