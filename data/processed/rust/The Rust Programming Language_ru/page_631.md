---
source_image: page_631.png
page_number: 631
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 70.95
tokens: 11983
characters: 1974
timestamp: 2025-12-24T10:45:15.172978
finish_reason: stop
---

Дополнение Б: Операторы и обозначения

Это дополнение содержит глоссарий синтаксиса Rust, включая операторы и другие обозначения, которые появляются сами по себе или в контексте путей, обобщений, типажей, макросов, атрибутов, комментариев, кортежей и скобок.

Операторы

Таблица Б-1 содержит операторы языка Rust, пример появления оператора, короткое объяснение, возможность перегрузки оператора. Если оператор можно перегрузить, то показан типаж, с помощью которого его можно перегрузить.

Таблица Б-1: Операторы

<table>
  <tr>
    <th>Оператор</th>
    <th>Пример</th>
    <th>Объяснение</th>
    <th>Перегружаемость</th>
  </tr>
  <tr>
    <td>!</td>
    <td>ident!(...),<br>ident!{...},<br>ident![...]</td>
    <td>Вызов макроса</td>
    <td></td>
  </tr>
  <tr>
    <td>!</td>
    <td>!expr</td>
    <td>Побитовое или логическое отрицание</td>
    <td>Not</td>
  </tr>
  <tr>
    <td>!=</td>
    <td>expr != expr</td>
    <td>Сравнение "не равно"</td>
    <td>PartialEq</td>
  </tr>
  <tr>
    <td>%</td>
    <td>expr % expr</td>
    <td>Остаток от деления</td>
    <td>Rem</td>
  </tr>
  <tr>
    <td>%=</td>
    <td>var %= expr</td>
    <td>Остаток от деления и присваивание</td>
    <td>RemAssign</td>
  </tr>
  <tr>
    <td>&</td>
    <td>&expr, &mut expr<br>&type, &mut type, &'a type, &'a mut type</td>
    <td>Заимствование<br>Указывает что данный тип заимствуется</td>
    <td></td>
  </tr>
  <tr>
    <td>&</td>
    <td>expr & expr</td>
    <td>Побитовое И</td>
    <td>BitAnd</td>
  </tr>
  <tr>
    <td>&=</td>
    <td>var &= expr</td>
    <td>Побитовое И и присваивание</td>
    <td>BitAndAssign</td>
  </tr>
  <tr>
    <td>&&</td>
    <td>expr && expr</td>
    <td>Логическое И</td>
    <td></td>
  </tr>
  <tr>
    <td>*</td>
    <td>expr * expr</td>
    <td>Арифметическое умножение</td>
    <td>Mul</td>
  </tr>
  <tr>
    <td>*=</td>
    <td>var *= expr</td>
    <td>Арифметическое умножение и присваивание</td>
    <td>MulAssign</td>
  </tr>
</table>