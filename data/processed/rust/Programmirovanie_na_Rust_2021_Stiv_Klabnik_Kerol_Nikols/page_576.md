---
source_image: page_576.png
page_number: 576
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.01
tokens: 8247
characters: 3095
timestamp: 2025-12-24T11:01:04.481942
finish_reason: stop
---

<table>
  <tr>
    <th>Оператор</th>
    <th>Пример</th>
    <th>Объяснение</th>
    <th>Перегружаемый?</th>
  </tr>
  <tr>
    <td>:</td>
    <td>ident: expr</td>
    <td>Инициализатор поля структуры</td>
    <td></td>
  </tr>
  <tr>
    <td>:</td>
    <td>'a: loop {...}</td>
    <td>Метка цикла</td>
    <td></td>
  </tr>
  <tr>
    <td>;</td>
    <td>expr;</td>
    <td>Инструкция либо терминатор элемента</td>
    <td></td>
  </tr>
  <tr>
    <td>;</td>
    <td>[...; len]</td>
    <td>Часть синтаксиса массива с фиксированным размером</td>
    <td></td>
  </tr>
  <tr>
    <td>&lt;&lt;</td>
    <td>expr &lt;&lt; expr</td>
    <td>Сдвиг влево</td>
    <td>Shl</td>
  </tr>
  <tr>
    <td>&lt;&lt;=</td>
    <td>var &lt;&lt;= expr</td>
    <td>Сдвиг влево и присваивание</td>
    <td>ShlAssign</td>
  </tr>
  <tr>
    <td>&lt;</td>
    <td>expr &lt; expr</td>
    <td>Меньше, чем сравниваемое</td>
    <td>PartialOrd</td>
  </tr>
  <tr>
    <td>&lt;=</td>
    <td>expr &lt;= expr</td>
    <td>Меньше или равно сравниваемому</td>
    <td>PartialOrd</td>
  </tr>
  <tr>
    <td>=</td>
    <td>var = expr,<br>ident = type</td>
    <td>Присваивание/эквивалентность</td>
    <td></td>
  </tr>
  <tr>
    <td>==</td>
    <td>expr == expr</td>
    <td>Сравнение равенства</td>
    <td>PartialEq</td>
  </tr>
  <tr>
    <td>=&gt;</td>
    <td>pat =&gt; expr</td>
    <td>Часть синтаксиса рукава выражения match</td>
    <td></td>
  </tr>
  <tr>
    <td>&gt;</td>
    <td>expr &gt; expr</td>
    <td>Больше, чем сравниваемое</td>
    <td>PartialOrd</td>
  </tr>
  <tr>
    <td>&gt;=</td>
    <td>expr &gt;= expr</td>
    <td>Больше или равно сравниваемому</td>
    <td>PartialOrd</td>
  </tr>
  <tr>
    <td>&gt;&gt;</td>
    <td>expr &gt;&gt; expr</td>
    <td>Сдвиг вправо</td>
    <td>Shr</td>
  </tr>
  <tr>
    <td>&gt;&gt;=</td>
    <td>var &gt;&gt;= expr</td>
    <td>Сдвиг вправо и присваивание</td>
    <td>ShrAssign</td>
  </tr>
  <tr>
    <td>@</td>
    <td>ident @ pat</td>
    <td>Привязка к паттерну</td>
    <td></td>
  </tr>
  <tr>
    <td>^</td>
    <td>expr ^ expr</td>
    <td>Побитовое исключающее ИЛИ</td>
    <td>BitXor</td>
  </tr>
  <tr>
    <td>^=</td>
    <td>var ^= expr</td>
    <td>Побитовое исключающее ИЛИ и присваивание</td>
    <td>BitXorAssign</td>
  </tr>
  <tr>
    <td>|</td>
    <td>pat | pat</td>
    <td>Альтернативы паттернов</td>
    <td></td>
  </tr>
  <tr>
    <td>|</td>
    <td>expr | expr</td>
    <td>Побитовое ИЛИ</td>
    <td>BitOr</td>
  </tr>
  <tr>
    <td>|=</td>
    <td>var |= expr</td>
    <td>Побитовое ИЛИ и присваивание</td>
    <td>BitOrAssign</td>
  </tr>
  <tr>
    <td>||</td>
    <td>expr || expr</td>
    <td>Логическое ИЛИ</td>
    <td></td>
  </tr>
  <tr>
    <td>?</td>
    <td>expr?</td>
    <td>Передача ошибок</td>
    <td></td>
  </tr>
</table>

Неоператорные символы

В следующих таблицах содержатся все не-буквы, которые не функционируют как операторы, то есть они не ведут себя как вызов функции или метода.

Таблица Б.2 показывает символы, которые появляются по отдельности и являются действительноными в различных местах.