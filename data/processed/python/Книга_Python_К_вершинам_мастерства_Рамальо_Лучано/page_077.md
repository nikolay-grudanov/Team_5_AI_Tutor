---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.13
tokens: 12233
characters: 2582
timestamp: 2025-12-24T01:38:18.160331
finish_reason: stop
---

Когда список не подходит

Операции append и popleft атомарны, поэтому deque можно безопасно использовать как LIFO-очередь в многопоточных приложениях без явных блокировок.

Таблица 2.3. Методы, реализованные в классах list и deque (унаследованные от object для краткости опущены)

<table>
  <tr>
    <th></th>
    <th>list</th>
    <th>deque</th>
  </tr>
  <tr>
    <td>s.__add__(s2)</td>
    <td>•</td>
    <td>s + s2 — конкатенация</td>
  </tr>
  <tr>
    <td>s.__iadd__(s2)</td>
    <td>•</td>
    <td>s += s2 — конкатенация на месте</td>
  </tr>
  <tr>
    <td>s.append(e)</td>
    <td>•</td>
    <td>Добавление элемента справа (после последнего)</td>
  </tr>
  <tr>
    <td>s.appendleft(e)</td>
    <td>•</td>
    <td>Добавление элемента слева (перед первым)</td>
  </tr>
  <tr>
    <td>s.clear()</td>
    <td>•</td>
    <td>Удаление всех элементов</td>
  </tr>
  <tr>
    <td>s.__contains__(e)</td>
    <td>•</td>
    <td>e входит в s</td>
  </tr>
  <tr>
    <td>s.copy()</td>
    <td>•</td>
    <td>Поверхностная копия списка</td>
  </tr>
  <tr>
    <td>s.__copy__()</td>
    <td>•</td>
    <td>Поддержка copy.copy (поверхностная копия)</td>
  </tr>
  <tr>
    <td>s.count(e)</td>
    <td>•</td>
    <td>Подсчет числа вхождений элемента</td>
  </tr>
  <tr>
    <td>s.__delitem__(p)</td>
    <td>•</td>
    <td>Удаление элемента в позиции p</td>
  </tr>
  <tr>
    <td>s.extend(i)</td>
    <td>•</td>
    <td>Добавление элементов из итерируемого объекта it справа</td>
  </tr>
  <tr>
    <td>s.extendleft(i)</td>
    <td>•</td>
    <td>Добавление элементов из итерируемого объекта it слева</td>
  </tr>
  <tr>
    <td>s.__getitem__(p)</td>
    <td>•</td>
    <td>s[p] — получение элемента в указанной позиции</td>
  </tr>
  <tr>
    <td>s.index(e)</td>
    <td>•</td>
    <td>Поиск позиции первого вхождения e</td>
  </tr>
  <tr>
    <td>s.insert(p, e)</td>
    <td>•</td>
    <td>Вставка элемента e перед элементом в позиции p</td>
  </tr>
  <tr>
    <td>s.__iter__()</td>
    <td>•</td>
    <td>Получение итератора</td>
  </tr>
  <tr>
    <td>s.__len__()</td>
    <td>•</td>
    <td>len(s) — количество элементов</td>
  </tr>
  <tr>
    <td>s.__mul__(n)</td>
    <td>•</td>
    <td>s * n — кратная конкатенация</td>
  </tr>
  <tr>
    <td>s.__imul__(n)</td>
    <td>•</td>
    <td>s *= n — кратная конкатенация на месте</td>
  </tr>
  <tr>
    <td>s.__rmul__(n)</td>
    <td>•</td>
    <td>n * s — инверсная кратная конкатенация<sup>a</sup></td>
  </tr>
  <tr>
    <td>s.pop()</td>
    <td>•</td>
    <td>Удалить и вернуть последний элемент<sup>b</sup></td>
  </tr>
</table>