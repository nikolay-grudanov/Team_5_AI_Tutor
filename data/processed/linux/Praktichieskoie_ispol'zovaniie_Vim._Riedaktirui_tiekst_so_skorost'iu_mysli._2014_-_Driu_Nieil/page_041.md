---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.19
tokens: 5638
characters: 1518
timestamp: 2025-12-24T04:10:20.095568
finish_reason: stop
---

vimdoc.sourceforge.net/htmldoc/repeat.html#). Вроде бы ничего особенного, но за этим простым определением скрывается мощная основа, делающая модель модального редактирования в Vim такой эффективной. Для начала выясним, что это за «последнее изменение».

Чтобы осознать всю мощь команды «точка», нужно понимать, что под «последним изменением» может скрываться все, что угодно. Изменением могут быть действия над отдельными символами, строками или даже над целым файлом.

Для демонстрации воспользуемся следующим фрагментом текста:

the_vim_way/0_mechanics.txt
http://media.pragprog.com/titles/dnvim/code/the_vim_way/0_mechanics.txt

Line one
Line two
Line three
Line four

Команда x удаляет символ под курсором. Когда команда «точка» используется в этом контексте, под «последним изменением» Vim будет понимать удаление символа под курсором:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Line one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>x</td>
    <td>ine one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>.</td>
    <td>ne one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>..</td>
    <td>one<br>Line two<br>Line three<br>Line four</td>
  </tr>
</table>

Вернуть файл в исходное состояние можно, нажав клавишу u несколько раз, чтобы отменить изменения.

Команда dd тоже выполняет удаление, но она удаляет текущую строку целиком. Если использовать команду «точка» после команды