---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 75.22
tokens: 12031
characters: 2137
timestamp: 2025-12-24T01:36:34.449034
finish_reason: stop
---

Глава 1. Модель данных в языке Python

Таблицы 1.1 и 1.2 дают представление о том, что имеется в нашем распоряжении.

Методы сгруппированы в таблицы не совсем так, как в официальной документации.

Таблица 1.1. Имена специальных методов (операторы не включены)

<table>
  <tr>
    <th>Категория</th>
    <th>Имена методов</th>
  </tr>
  <tr>
    <td>Представление в виде строк и байтов</td>
    <td>__repr__, __str__, __format__, __bytes__</td>
  </tr>
  <tr>
    <td>Преобразование в число</td>
    <td>__abs__, __bool__, __complex__, __int__, __float__, __hash__, __index__</td>
  </tr>
  <tr>
    <td>Эмуляция коллекций</td>
    <td>__len__, __getitem__, __setitem__, __delitem__, __contains__</td>
  </tr>
  <tr>
    <td>Итерирование</td>
    <td>__iter__, __reversed__, __next__</td>
  </tr>
  <tr>
    <td>Эмуляция объектов, допускающих вызов</td>
    <td>__call__</td>
  </tr>
  <tr>
    <td>Управление контекстом</td>
    <td>__enter__, __exit__</td>
  </tr>
  <tr>
    <td>Создание и уничтожение объектов</td>
    <td>__new__, __init__, __del__</td>
  </tr>
  <tr>
    <td>Управление атрибутами</td>
    <td>__getattr__, __getattribute__, __setattr__, __delattr__, __dir__</td>
  </tr>
  <tr>
    <td>Дескрипторы атрибутов</td>
    <td>__get__, __set__, __delete__</td>
  </tr>
  <tr>
    <td>Сервисы классов</td>
    <td>__prepare__, __instancecheck__, __subclasscheck__</td>
  </tr>
</table>

Таблица 1.2. Имена специальных методов для операторов

<table>
  <tr>
    <th>Категория</th>
    <th>Имена методов</th>
  </tr>
  <tr>
    <td>Унарные числовые операторы</td>
    <td>__neg__ -, __pos__ +, __abs__ abs()</td>
  </tr>
  <tr>
    <td>Операторы сравнения</td>
    <td>__lt__ <>, __le__ <=, __eq__ ==, __ne__ !=, __gt__ >, __ge__ >=</td>
  </tr>
  <tr>
    <td>Арифметические операторы</td>
    <td>__add__ +, __sub__ -, __mul__ *, __truediv__ /, __floordiv__ //, __mod__ %, __divmod__ divmod(), __pow__ ** or pow(), __round__ round()</td>
  </tr>
  <tr>
    <td>Инверсные арифметические операторы</td>
    <td>__radd__, __rsub__, __rmul__, __rtruediv__, __rfloordiv__, __rmod__, __rdivmod__, __rpow__</td>
  </tr>
</table>