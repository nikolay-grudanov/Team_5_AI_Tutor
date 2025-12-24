---
source_image: page_409.png
page_number: 409
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 73.13
tokens: 12494
characters: 3131
timestamp: 2025-12-24T01:54:14.108858
finish_reason: stop
---

Перегрузка оператора умножения на скаляр *

Таблица 13.1. Имена методов инфиксных операторов (операторы, вычисляемые на месте, связаны с составным присваиванием; операторы сравнения описаны в табл. 13.2)

<table>
  <tr>
    <th>Оператор</th>
    <th>Прямой</th>
    <th>Инверсный</th>
    <th>На месте</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>+</td>
    <td>__add__</td>
    <td>__radd__</td>
    <td>__iadd__</td>
    <td>Сложение или конкатенация</td>
  </tr>
  <tr>
    <td>-</td>
    <td>__sub__</td>
    <td>__rsub__</td>
    <td>__isub__</td>
    <td>Вычитание</td>
  </tr>
  <tr>
    <td>*</td>
    <td>__mul__</td>
    <td>__rmul__</td>
    <td>__imul__</td>
    <td>Умножение или повторение</td>
  </tr>
  <tr>
    <td>/</td>
    <td>__truediv__</td>
    <td>__rtruediv__</td>
    <td>__itruediv__</td>
    <td>Истинное деление</td>
  </tr>
  <tr>
    <td>//</td>
    <td>__floordiv__</td>
    <td>__rfloordiv__</td>
    <td>__ifloordiv__</td>
    <td>Деление с округлением</td>
  </tr>
  <tr>
    <td>%</td>
    <td>__mod__</td>
    <td>__rmod__</td>
    <td>__imod__</td>
    <td>Деление по модулю</td>
  </tr>
  <tr>
    <td>divmod()</td>
    <td>__divmod__</td>
    <td>__rdivmod__</td>
    <td>__idivmod__</td>
    <td>Возвращает кортеж, содержащий частное и остаток</td>
  </tr>
  <tr>
    <td>**, pow()</td>
    <td>__pow__</td>
    <td>__rpow__</td>
    <td>__ipow__</td>
    <td>Возведение в степень<sup>a</sup></td>
  </tr>
  <tr>
    <td>@</td>
    <td>__matmul__</td>
    <td>__rmatmul__</td>
    <td>__imatmul__</td>
    <td>Матричное умножение<sup>b</sup></td>
  </tr>
  <tr>
    <td>&</td>
    <td>__and__</td>
    <td>__rand__</td>
    <td>__iand__</td>
    <td>Поразрядное И</td>
  </tr>
  <tr>
    <td>|</td>
    <td>__or__</td>
    <td>__ror__</td>
    <td>__ior__</td>
    <td>Поразрядное ИЛИ</td>
  </tr>
  <tr>
    <td>^</td>
    <td>__xor__</td>
    <td>__rxor__</td>
    <td>__ixor__</td>
    <td>Поразрядное ИСКЛЮЧАЮЩЕЕ ИЛИ</td>
  </tr>
  <tr>
    <td>&lt;&lt;</td>
    <td>__lshift__</td>
    <td>__rlshift__</td>
    <td>__ilshift__</td>
    <td>Поразрядный сдвиг влево</td>
  </tr>
  <tr>
    <td>&gt;&gt;</td>
    <td>__rshift__</td>
    <td>__rrshift__</td>
    <td>__irshift__</td>
    <td>Поразрядный сдвиг вправо</td>
  </tr>
</table>

<sup>a</sup> Оператор pow принимает необязательный третий аргумент, modulo: pow(a, b, modulo), поддерживаемый также специальными методами, если они вызываются напрямую (например, a.__pow__(b, modulo)).

<sup>b</sup> Появился в версии Python 3.5.

Еще одна категория инфиксных операторов — операторы сравнения, для них действуют несколько иные правила. Мы рассмотрим их в следующем разделе. А на врезке ниже рассказывается об операторе, включенном в версию Python 3.5, которая на момент написания этой книги еще не была выпущена.

Новый инфиксный оператор @ в версии Python 3.5

В версии Python 3.4 нет инфиксного оператора скалярного произведения. Однако в версии Python 3.5 pre-alpha уже реализовано предложение из документа «PEP 465 — A dedicated infix operator for matrix multiplication» (https://www.python.org/dev/peps/pep-0465/), согласно