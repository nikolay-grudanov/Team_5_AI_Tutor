---
source_image: page_072.png
page_number: 72
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.00
tokens: 5900
characters: 2383
timestamp: 2025-12-24T04:11:12.370674
finish_reason: stop
---

Рецепт 15. Вставка из регистра, не покидая режима вставки

Нам нужно дополнить последнюю строку, вставив название этой книги. Так как этот текст уже присутствует в начале первой строки, мы скопируем его в регистр и затем вставим в конец последней строки в режиме вставки:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td><span style="background-color:#e0e0e0">yt,</span></td>
    <td>Practical Vim, by Drew Neil<br>Read Drew Neil’s</td>
  </tr>
  <tr>
    <td><span style="background-color:#e0e0e0">jA</span></td>
    <td>Practical Vim, by Drew Neil<br>Read Drew Neil’s</td>
  </tr>
  <tr>
    <td><span style="background-color:#e0e0e0">&lt;C-r&gt;0</span></td>
    <td>Practical Vim, by Drew Neil<br>Read Drew Neil’s Practical Vim</td>
  </tr>
  <tr>
    <td>.<span style="background-color:#e0e0e0">Esc</span></td>
    <td>Practical Vim, by Drew Neil<br>Read Drew Neil’s Practical Vim.</td>
  </tr>
</table>

Команда yt, копирует слова Practical Vim в регистр (в рецепте 49 (глава 8) мы познакомимся с командой t{char}). Вставить текст из регистра в позицию курсора, находясь в режиме вставки, можно нажатием клавиш <C-r>0. Регистры и операции копирования мы достаточно подробно рассмотрим в главе 10 «Копирование и вставка».

В общем случае команда имеет вид <C-r>{register}, где {register} — это адрес регистра (см. :h i_CTRL-R http://vimdoc.sourceforge.net/htmldoc/insert.html#i_CTRL-R).

Используйте <C-r>{register} для доступа к регистрам

Команду <C-r>{register} удобно использовать для копирования нескольких слов в режиме вставки. Если регистр содержит достаточно большой фрагмент текста, вы можете заметить небольшую задержку перед тем, как текст на экране обновится. Это объясняется тем, что Vim вставляет текст из регистра, как если бы он вводился по одному символу. Если включена настройка textwidth или autoindent, в тексте могут появиться нежелательные разрывы строк или дополнительные отступы.

Команда <C-r><C-p>{register} действует более интеллектуально. Она вставляет текст буквально и исправляет все непредусмотренные отступы (см. :h i_CTRL-R_CTRL-P http://vimdoc.sourceforge.net/htmldoc/insert.html#i_CTRL-R_CTRL-P). Но она так утомительна! Если мне требуется вставить из регистра многострочный текст, я предпочитаю переключиться в командный режим и использовать одну из команд вставки (см. рецепт 62 в главе 10).