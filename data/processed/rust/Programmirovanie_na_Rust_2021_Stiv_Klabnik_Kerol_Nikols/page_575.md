---
source_image: page_575.png
page_number: 575
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.67
tokens: 8176
characters: 3001
timestamp: 2025-12-24T11:01:03.412116
finish_reason: stop
---

Вот таблица операторов с примерами, объяснениями и перегружаемостью:

<table>
  <tr>
    <th>Оператор</th>
    <th>Пример</th>
    <th>Объяснение</th>
    <th>Перегружаемый?</th>
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
  <tr>
    <td>*</td>
    <td>*expr</td>
    <td>Разыменование (следование к значению по указателю с помощью оператора разыменования)</td>
    <td></td>
  </tr>
  <tr>
    <td>*const type, *mut type</td>
    <td></td>
    <td>Сырой указатель</td>
    <td></td>
  </tr>
  <tr>
    <td>+</td>
    <td>trait + trait, 'a + trait</td>
    <td>Ограничение составного типа</td>
    <td></td>
  </tr>
  <tr>
    <td>+</td>
    <td>expr + expr</td>
    <td>Арифметическое сложение</td>
    <td>Add</td>
  </tr>
  <tr>
    <td>+=</td>
    <td>var += expr</td>
    <td>Арифметическое сложение и присваивание</td>
    <td>AddAssign</td>
  </tr>
  <tr>
    <td>,</td>
    <td>expr, expr</td>
    <td>Разделитель аргументов и элементов</td>
    <td></td>
  </tr>
  <tr>
    <td>-</td>
    <td>- expr</td>
    <td>Арифметическое отрицание</td>
    <td>Neg</td>
  </tr>
  <tr>
    <td>-</td>
    <td>expr - expr</td>
    <td>Арифметическое вычитание</td>
    <td>Sub</td>
  </tr>
  <tr>
    <td>-=</td>
    <td>var -= expr</td>
    <td>Арифметическое вычитание и присваивание</td>
    <td>SubAssign</td>
  </tr>
  <tr>
    <td-></td>
    <td>fn(...) -> type, |...| -> type</td>
    <td>Тип, возвращаемый из функции и замыкания</td>
    <td></td>
  </tr>
  <tr>
    <td>expr.ident</td>
    <td></td>
    <td>Доступ к члену</td>
    <td></td>
  </tr>
  <tr>
    <td>.., expr.., ..expr, expr..expr</td>
    <td></td>
    <td>Литерал интервала с правосторонним исключением</td>
    <td></td>
  </tr>
  <tr>
    <td>..=</td>
    <td>..=expr, expr..=expr</td>
    <td>Литерал интервала с правосторонним включением</td>
    <td></td>
  </tr>
  <tr>
    <td>..expr</td>
    <td></td>
    <td>Синтаксис обновления литерала структуры</td>
    <td></td>
  </tr>
  <tr>
    <td>variant(x, ..), struct_type {x, .. }</td>
    <td></td>
    <td>Привязка к паттерну "И все остальное"</td>
    <td></td>
  </tr>
  <tr>
    <td>expr...expr</td>
    <td></td>
    <td>В паттерне: паттерн включающего интервала</td>
    <td></td>
  </tr>
  <tr>
    <td>/</td>
    <td>expr / expr</td>
    <td>Арифметическое деление</td>
    <td>Div</td>
  </tr>
  <tr>
    <td>/=</td>
    <td>var /= expr</td>
    <td>Арифметическое деление и присваивание</td>
    <td>DivAssign</td>
  </tr>
  <tr>
    <td>:</td>
    <td>pat: type, ident: type</td>
    <td>Ограничения</td>
    <td></td>
  </tr>
</table>