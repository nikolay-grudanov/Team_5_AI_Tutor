---
source_image: page_242.png
page_number: 242
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.91
tokens: 5880
characters: 2220
timestamp: 2025-12-24T04:14:44.983068
finish_reason: stop
---

Рецепт 74. Ключ \V включает режим поиска точного совпадения

мощью переключателя самого простого режима (very nomagic) можно выключить интерпретацию большинства специальных символов, таких как ., * и ?.

Возьмем для демонстрации следующий фрагмент текста:

patterns/excerpt-also-known-as.txt
http://media.pragprog.com/titles/dnvim/code/patterns/excerpt-also-known-as.txt

The N key searches backward...
...the \v pattern switch (a.k.a. very magic search)...

Допустим, что нам нужно перейти к вхождению подстроки «а.к.а.» (от англ. «also known as» — «известный также как»), выполнив ее поиск. Самой первой мыслью будет воспользоваться командой

⇒ /а.к.а.

Но, нажав клавишу Enter, мы обнаружим, что в этом фрагменте было найдено несколько совпадений. Символ «.» имеет специальное значение: ему соответствует любой символ. Например, слово «backward» содержит фрагмент, соответствующий нашему шаблону. Следующая таблица иллюстрирует наши попытки найти совпадение с требуемым фрагментом с первой попытки.

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>The N key searches backward...<br>...the \v pattern switch (a.k.a. very magic search)...</td>
  </tr>
  <tr>
    <td>/а.к.а.<CR></td>
    <td>The N key searches backward...<br>...the \v pattern switch (а.к.а. very magic search)...</td>
  </tr>
  <tr>
    <td>/а\.к\.а\.<CR></td>
    <td>The N key searches backward...<br>...the \v pattern switch (а.к.а. very magic search)...</td>
  </tr>
  <tr>
    <td>/\Va.k.a.<CR></td>
    <td>The N key searches backward...<br>...the \v pattern switch (а.к.а. very magic search)...</td>
  </tr>
</table>

Попытки найти совпадение в примере выше всего лишь вызывают раздражение из-за задержки. Мы можем перейти к следующему совпадению, надеясь, что это и будет конечная цель, просто нажимая клавишу n. Но в некоторых ситуациях ошибочное совпадение может иметь гораздо более разрушительные последствия. Представьте, что мы собрались выполнить команду подстановки, такую как :%s// also known as/g, упустив из виду, что наш шаблон имеет гораздо более широкое толкование, чем мы подразумеваем (пустое поле шаблона в команде :substitute сообщает редактору Vim, что он