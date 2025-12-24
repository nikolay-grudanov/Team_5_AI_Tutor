---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 69.47
tokens: 12264
characters: 2739
timestamp: 2025-12-24T01:39:06.082502
finish_reason: stop
---

Обзор наиболее употребительных методов отображений

Таблица 3.1. Методы типов отображений types dict, collections.defaultdict и collections.OrderedDict (для краткости методы, унаследованные от object, опущены); необязательные аргументы заключены в квадратные скобки

<table>
  <tr>
    <th></th>
    <th>dict</th>
    <th>defaultdict</th>
    <th>OrderedDict</th>
    <th></th>
  </tr>
  <tr>
    <td>d.clear()</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Удаление всех элементов</td>
  </tr>
  <tr>
    <td>d.__contains__(k)</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>k входит в d</td>
  </tr>
  <tr>
    <td>d.copy()</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Поверхностная копия</td>
  </tr>
  <tr>
    <td>d.__copy__()</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Поддержка copy.copy</td>
  </tr>
  <tr>
    <td>d.default_factory</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Вызываемый объект, к которому обращается метод __missing__ в случае отсутствия значения<sup>a</sup></td>
  </tr>
  <tr>
    <td>s.__delitem__(p)</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>del d[k] — удаление элемента с ключом k</td>
  </tr>
  <tr>
    <td>d.fromkeys(itm [initial])</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Новое отображение, ключи которого поставляет итерируемый объект, и с необязательным начальным значением (по умолчанию None)</td>
  </tr>
  <tr>
    <td>d.get(k, [default])</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Получить элемент с ключом k, а если такой ключ отсутствует, вернуть default или None</td>
  </tr>
  <tr>
    <td>d.__getitem__(k)</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>d[k] — получить элемент с ключом k</td>
  </tr>
  <tr>
    <td>d.items()</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Получить представление элементов — множество пары (key, value)</td>
  </tr>
  <tr>
    <td>d.__iter__()</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Получение итератора по ключам</td>
  </tr>
  <tr>
    <td>d.keys()</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Получить представление ключей</td>
  </tr>
  <tr>
    <td>d.__len__()</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>len(d) — количество элементов</td>
  </tr>
  <tr>
    <td>d.__missing__(k)</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Вызывается, когда __getitem__ не может найти элемент</td>
  </tr>
  <tr>
    <td>d.move_to_end(k, [last])</td>
    <td></td>
    <td></td>
    <td>•</td>
    <td>Переместить ключ k в первую или последнюю позицию (last по умолчанию равно True)</td>
  </tr>
</table>

<sup>a</sup> Если метод __missing__ не определен, то вызывается метод __getitem__.