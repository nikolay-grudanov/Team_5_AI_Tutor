---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.21
tokens: 5928
characters: 2547
timestamp: 2025-12-24T04:11:36.982049
finish_reason: stop
---

Рецепт 25. Изменение колонок текста

visual_mode/sprite.css
http://media.pragprog.com/titles/dnvim/code/visual_mode/sprite.css

li.one    a{ background-image: url('/images/sprite.png'); }
li.two    a{ background-image: url('/images/sprite.png'); }
li.three  a{ background-image: url('/images/sprite.png'); }

Допустим, что файл sprite.png был перемещен из каталога images/ в каталог components/. Нам необходимо изменить все ссылки на этот файл, указав новое его местоположение. Мы могли бы сделать это в блочном визуальном режиме, как показано в табл. 4.4.

Эта процедура не должна вызвать осложнений. Сначала следует выделить требуемый фрагмент текста в блочном визуальном режиме, который как раз имеет прямоугольную форму. Затем нажать клавишу C, в результате чего выделенный текст будет удален и редактор перейдет в режим вставки.

При вводе слова «components» в режиме вставки оно будет появляться только в верхней строке. В остальных строках ничего происходить не будет. Мы увидим введенный текст в этих строках, только когда нажмем клавишу <Esc>, чтобы вернуться в командный режим.

Поведение команды изменения текста в блочном визуальном режиме может показаться странным. Кажется непоследовательным, что удаление воздействует на все выделенные строки сразу, а вставка — только на самую верхнюю строку (по крайней мере, пока редактор находится в режиме вставки). Некоторые текстовые редакторы, поддерживающие похожую функциональность, изменяют сразу все выбранные строки. Если вы привыкли к такому поведению (как и я в былые времена), вам может показаться, что реализация Vim недостаточно хорошо продумана.

Таблица 4.4. Вставка в несколько строк

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}<br>Командный режим</td>
    <td>li.one    a{ background-image: url('/images/sprite.png'); }<br>
        li.two     a{ background-image: url('/images/sprite.png'); }<br>
        li.three   a{ background-image: url('/images/sprite.png'); }</td>
  </tr>
  <tr>
    <td>&lt;C-v&gt;jje<br>Визуальный режим</td>
    <td>li.one    a{ background-image: url('/images/sprite.png'); }<br>
        li.two     a{ background-image: url('/images/sprite.png'); }<br>
        li.three   a{ background-image: url('/images/sprite.png'); }</td>
  </tr>
  <tr>
    <td>c<br>Режим вставки</td>
    <td>li.one    a{ background-image: url('/sprite.png'); }<br>
        li.two     a{ background-image: url('//sprite.png'); }<br>
        li.three   a{ background-image: url('//sprite.png'); }</td>
  </tr>
</table>