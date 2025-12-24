---
source_image: page_091.png
page_number: 91
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.42
tokens: 5884
characters: 2363
timestamp: 2025-12-24T04:11:33.361247
finish_reason: stop
---

Таблица 4.4. Вставка в несколько строк (окончание)

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td rowspan="3">components<br><i>Режим вставки</i></td>
    <td>li.one a{ background-image: url('/ components/sprite.png'); }<br>li.two a{ background-image: url('//sprite.png'); }<br>li.three a{ background-image: url('//sprite.png'); }</td>
  </tr>
  <tr>
    <td>li.one a{ background-image: url('/component/s/sprite.png'); }<br>li.two a{ background-image: url('/components/sprite.png'); }<br>li.three a{ background-image: url('/components/sprite.png'); }</td>
  </tr>
  <tr>
    <td>li.one a{ background-image: url('/component/s/sprite.png'); }<br>li.two a{ background-image: url('/components/sprite.png'); }<br>li.three a{ background-image: url('/components/sprite.png'); }</td>
  </tr>
  <tr>
    <td><i>Командный режим</i></td>
    <td>li.one a{ background-image: url('/component/s/sprite.png'); }<br>li.two a{ background-image: url('/components/sprite.png'); }<br>li.three a{ background-image: url('/components/sprite.png'); }</td>
  </tr>
</table>

Но на конечном результате это никак не отражается. Пока вы используете режим вставки только для ввода коротких фрагментов, вы не будете замечать подобных странностей.

Рецепт 26. Добавление текста после неправильного блока

Блочный визуальный режим отлично подходит для выполнения операций с прямоугольными фрагментами текста, такими как строки и колонки, но позволяет работать и с неправильными фрагментами.

Мы уже встречались со следующим фрагментом кода на JavaScript:

the_vim_way/2_foo_bar.js
http://media.pragprog.com/titles/dnvim/code/the_vim_way/2_foo_bar.js

var foo = 1
var bar = 'a'
var foobar = foo + bar

Фрагмент состоит из трех строк разной длины. Нам требуется добавить точку с запятой в конец каждой из них. В рецепте 2 (глава 1) мы решили эту задачу с помощью команды «точка», но ее также можно решить с использованием блочного визуального режима, как показано в табл. 4.5.

После перехода в блочный визуальный режим мы расширяем область выделения до конца каждой строки, нажимая $. На первый взгляд это может показаться непросто, потому что все строки имеют разную длину. Но в данном случае Vim понимает, что мы желаем расширить область выделения до конца каждой строки. Это позволяет выделить неправильную область со ступенчатым правым краем.