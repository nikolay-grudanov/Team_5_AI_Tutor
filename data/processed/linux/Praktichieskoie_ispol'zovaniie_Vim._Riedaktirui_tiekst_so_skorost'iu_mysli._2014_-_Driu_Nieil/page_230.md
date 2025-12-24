---
source_image: page_230.png
page_number: 230
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.59
tokens: 5731
characters: 1749
timestamp: 2025-12-24T04:14:29.872175
finish_reason: stop
---

использовался регистр выражений. Затем перед остановкой записи макроса мы увеличили значение, хранящееся в переменной, которое теперь должно быть равно 2.

Выполнение макроса

Сейчас можно применить макрос к остальным строкам, как показано в табл. 11.4.
Команда :normal @a применит макрос к каждой строке, попавшей в выделенный фрагмент (см. раздел «Параллельное выполнение макроса» в рецепте 67). В начале процесса переменная i имеет значение 2, но оно увеличивается с каждым вызовом макроса. В конечном итоге к каждой выделенной строке будет добавлен ее порядковый номер.

Таблица 11.4. Нумерация элементов списка с помощью макроса

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>1) partridge in a pear tree<br>turtle doves<br>French hens<br>calling birds<br>golden rings</td>
  </tr>
  <tr>
    <td>jVG</td>
    <td>1) partridge in a pear tree<br><span style="background-color: #e0e0e0;">turtle doves</span><br><span style="background-color: #e0e0e0;">French hens</span><br><span style="background-color: #e0e0e0;">calling birds</span><br><span style="background-color: #e0e0e0;">golden rings</span></td>
  </tr>
  <tr>
    <td>:'<,'>normal @a</td>
    <td>1) partridge in a pear tree<br>2) turtle doves<br>3) French hens<br>4) calling birds<br>5) <span style="background-color: #e0e0e0;">golden rings</span></td>
  </tr>
</table>

Для решения этой задачи также можно было бы использовать команды копирования, вставки и <C-a>. Опробовать такую возможность я оставляю вам в качестве самостоятельного упражнения!

Рецепт 71. Правка содержимого макроса

В рецепте 68 было показано, как добавлять новые команды в конец макроса. Но как быть, если потребуется удалить последнюю ко-