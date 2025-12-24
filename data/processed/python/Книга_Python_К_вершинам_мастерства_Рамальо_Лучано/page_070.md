---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 65.22
tokens: 12249
characters: 2647
timestamp: 2025-12-24T01:38:07.399164
finish_reason: stop
---

Завершим этот раздел о массивах таблицей 2.2, в которой сравниваются свойства типов list и array.array.

Таблица 2.2. Методы и атрибуты типов list и array (нерекомендуемые методы массива, а также унаследованные от object, для краткости опущены)

<table>
  <tr>
    <th></th>
    <th>list</th>
    <th>array</th>
  </tr>
  <tr>
    <td>s.__add__(s2)</td>
    <td>•</td>
    <td>•<br>s + s2 — конкатенация</td>
  </tr>
  <tr>
    <td>s.__iadd__(s2)</td>
    <td>•</td>
    <td>•<br>s += s2 — конкатенация на месте</td>
  </tr>
  <tr>
    <td>s.append(e)</td>
    <td>•</td>
    <td>•<br>Добавление элемента в конец списка</td>
  </tr>
  <tr>
    <td>s.byteswap()</td>
    <td></td>
    <td>•<br>Перестановка всех байтов в массиве с целью изменения машинной архитектуры</td>
  </tr>
  <tr>
    <td>s.clear()</td>
    <td>•</td>
    <td>Удаление всех элементов</td>
  </tr>
  <tr>
    <td>s.__contains__(e)</td>
    <td>•</td>
    <td>•<br>e входит в s</td>
  </tr>
  <tr>
    <td>s.copy()</td>
    <td>•</td>
    <td>Поверхностная копия списка</td>
  </tr>
  <tr>
    <td>s.__copy__()</td>
    <td></td>
    <td>•<br>Поддержка метода copy.copy</td>
  </tr>
  <tr>
    <td>s.count(e)</td>
    <td>•</td>
    <td>•<br>Подсчет числа вхождений элемента</td>
  </tr>
  <tr>
    <td>s.__deepcopy__()</td>
    <td></td>
    <td>•<br>Оптимизированная поддержка метода copy.deepcopy</td>
  </tr>
  <tr>
    <td>s.__delitem__(p)</td>
    <td>•</td>
    <td>•<br>Удаление элемента в позиции p</td>
  </tr>
  <tr>
    <td>s.extend(it)</td>
    <td>•</td>
    <td>•<br>Добавление в конец списка элементов из итерируемого объекта it</td>
  </tr>
  <tr>
    <td>s.frombytes(b)</td>
    <td></td>
    <td>•<br>Добавление в конец элементов из последовательности байтов, интерпретируемых как упакованные машинные слова</td>
  </tr>
  <tr>
    <td>s.fromfile(f, n)</td>
    <td></td>
    <td>•<br>Добавление в конец n элементов из двоичного файла f, интерпретируемых как упакованные машинные слова</td>
  </tr>
  <tr>
    <td>s.fromlist(l)</td>
    <td></td>
    <td>•<br>Добавление в конец элементов из списка; если хотя бы один возбуждает исключение TypeError, то не добавляется ничего</td>
  </tr>
  <tr>
    <td>s.__getitem__(p)</td>
    <td>•</td>
    <td>•<br>s[p] — получение элемента в указанной позиции</td>
  </tr>
  <tr>
    <td>s.index(e)</td>
    <td>•</td>
    <td>•<br>Поиск позиции первого вхождения e</td>
  </tr>
  <tr>
    <td>s.insert(p, e)</td>
    <td>•</td>
    <td>Вставка элемента e перед элементом в позиции p</td>
  </tr>
  <tr>
    <td>s.itemsize</td>
    <td></td>
    <td>•<br>Размер каждого элемента массива в байтах</td>
  </tr>
</table>