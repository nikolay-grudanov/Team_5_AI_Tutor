---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.48
tokens: 5834
characters: 2075
timestamp: 2025-12-24T04:10:37.165538
finish_reason: stop
---

Рецепт 3. Шаг назад, три вперед

Мы можем дополнить единственный символ пробелами (один слева, другой справа), используя идиоматическое для Vim решение. Сначала оно будет казаться странным, но это решение дает возможность повторения, что позволяет выполнить задание с минимумом усилий.

Представьте, что имеется такая строка кода:

the_vim_way/3_concat.js
http://media.pragprog.com/titles/dnvim/code/the_vim_way/3_concat.js

var foo = "method("+argument1+","+argument2+)";

Конкатенация строк в JavaScript никогда не выглядела особенно удобочитаемо, тем не менее мы могли бы повысить удобочитаемость, окружая каждый знак + пробелами, чтобы строка кода выглядела, как показано ниже:

var foo = "method(" + argument1 + "," + argument2 + ")";

Делайте изменения повторяемыми

Описываемая задача имеет следующее идиоматическое решение:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>var foo = "method("+argument1+","+argument2+)";</td>
  </tr>
  <tr>
    <td>f+</td>
    <td>var foo = "method("+argument1+","+argument2+)";</td>
  </tr>
  <tr>
    <td>S+<Esc></td>
    <td>var foo = "method(" +argument1+","+argument2+)";</td>
  </tr>
  <tr>
    <td>;</td>
    <td>var foo = "method(" + argument1+","+argument2+)";</td>
  </tr>
  <tr>
    <td>.</td>
    <td>var foo = "method(" + argument1 + ","+argument2+)";</td>
  </tr>
  <tr>
    <td>;</td>
    <td>var foo = "method(" + argument1 + "," +argument2+")";</td>
  </tr>
  <tr>
    <td>;</td>
    <td>var foo = "method(" + argument1 + "," + argument2 +")";</td>
  </tr>
</table>

Команда S объединяет два шага в один: она удаляет символ под курсором и переходит в режим вставки. После удаления символа + мы вводим + и покидаем режим вставки.

Один шаг назад и затем три вперед. Этот странный танец на клавиатуре сначала выглядит малопонятным, но он дает нам большой выигрыш: мы можем повторять изменения с помощью команды «точка»: все, что для этого нужно, — переместить курсор к следующему символу +, после чего команда «точка» повторит этот маленький танец.