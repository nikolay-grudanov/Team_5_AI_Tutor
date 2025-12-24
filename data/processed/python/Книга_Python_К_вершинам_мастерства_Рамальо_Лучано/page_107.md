---
source_image: page_107.png
page_number: 107
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.62
tokens: 12110
characters: 2435
timestamp: 2025-12-24T01:39:39.359126
finish_reason: stop
---

Теория множеств

<table>
  <tr>
    <th>Мат. символ</th>
    <th>Оператор Python</th>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>s -= z</td>
    <td></td>
    <td>s.__isub__(z)</td>
    <td>Замена s разностью между s и z</td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td>s.difference_update(it,...)</td>
    <td>Замена s разностью между s и всеми множествами, построенными из итерируемых объектов it и т. д.</td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td>s.symmetric_difference(it)</td>
    <td>Дополнение s & set(it)</td>
  </tr>
  <tr>
    <td>s Δ z</td>
    <td>s ^ z</td>
    <td>s.__xor__(z)</td>
    <td>Симметрическая разность (дополнение пересечения s & z)</td>
  </tr>
  <tr>
    <td colspan="2">z ^ s</td>
    <td>z.__rxor__(s)</td>
    <td>Инверсный оператор ^</td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td>s.symmetric_difference_update(it,...)</td>
    <td>Замена s симметрической разностью между s и всеми множествами, построенными из итерируемых объектов it и т. д.</td>
  </tr>
  <tr>
    <td>s ^= z</td>
    <td></td>
    <td>s.__ixor__(z)</td>
    <td>Замена s симметрической разностью между s и z</td>
  </tr>
</table>

Когда я писал эти строки, существовал отчет об ошибке в Python (проблема 8743 (http://bugs.python.org/issue8743)) следующего содержания: «Операторы класса set (or, and, sub, xor и их аналоги для модификации на месте) требуют, чтобы параметр также был экземпляром set()». Нежелательным побочным эффектом является тот факт, что эти операторы не работают с подклассами collections.abc.Set. Эта ошибка уже исправлена в стволовых ветвях Python 2.7 и 3.4 и к моменту выхода книги должна уйти в прошлое.

В табл. 3.3 перечислены теоретико-множественные предикаты: методы и операторы, которые возвращают True ИЛИ False.

Таблица 3.3. Операторы сравнения множеств и методы, возвращающие булево значение

<table>
  <tr>
    <th>Мат. символ</th>
    <th>Оператор Python</th>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>e ∈ Z</td>
    <td>e in s</td>
    <td>s.__contains__(e)</td>
    <td>e является элементом s</td>
  </tr>
  <tr>
    <td>S ⊆ Z</td>
    <td>S <= z</td>
    <td>s.__le__(z)<br>s.issubset(it)</td>
    <td>s является подмножеством z<br>s является подмножеством множества z, построенного из итерируемого объекта it</td>
  </tr>
  <tr>
    <td colspan="4">s.isdisjoint(z) s и z дизъюнктны (т. е. не пересекаются)</td>
  </tr>
</table>