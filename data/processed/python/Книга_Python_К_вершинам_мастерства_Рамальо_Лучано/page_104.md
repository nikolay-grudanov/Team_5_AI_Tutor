---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.42
tokens: 12047
characters: 2245
timestamp: 2025-12-24T01:39:26.535071
finish_reason: stop
---

<code>
<class 'set'>
>>> s
{1}
>>> s.pop()
1
>>> s
set()
</code>

Литеральный синтаксис множеств вида {1, 2, 3} быстрее и понятнее, чем вызов конструктора (например, set([1, 2, 3])). При этом вторая форма медленнее, потому что для вычисления такого выражения Python должен найти класс set по имени, чтобы получить его конструктор, затем построить список и, наконец, передать этого список конструктору. А при обработке литерала {1, 2, 3} Python исполняет специализированный байт-код BUILD_SET.

Взгляните на байт-код обеих операций, выведенный дизассемблером dis.dis:

<table>
  <tr>
    <th>dis.dis:</th>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td>&gt;&gt;&gt; from dis import dis</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>&gt;&gt;&gt; dis('{1}')</td>
    <td>1 LOAD_CONST</td>
    <td>0 (1)</td>
    <td>①</td>
  </tr>
  <tr>
    <td></td>
    <td>3 BUILD_SET</td>
    <td>1</td>
    <td>②</td>
  </tr>
  <tr>
    <td></td>
    <td>6 RETURN_VALUE</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>&gt;&gt;&gt; dis('set([1])')</td>
    <td>1 LOAD_NAME</td>
    <td>0 (set)</td>
    <td>③</td>
  </tr>
  <tr>
    <td></td>
    <td>3 LOAD_CONST</td>
    <td>0 (1)</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>6 BUILD_LIST</td>
    <td>1</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>9 CALL_FUNCTION</td>
    <td>1 (1 positional, 0 keyword pair)</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>12 RETURN_VALUE</td>
    <td></td>
    <td></td>
  </tr>
</table>

① Дизассемблируем литературное выражение {1}.
② Специальный байт-код BUILD_SET выполняет почти всю работу.
③ Байт-код выражения set([1]).
④ Вместо BUILD_SET следующие три операции: LOAD_NAME, BUILD_LIST и CALL_FUNCTION.

Не существует специального синтаксиса для литералов, представляющих frozenset, — их приходится создавать с помощью конструктора. И стандартное строковое представление в Python 3 выглядит как вызов конструктора frozenset. Ниже показан пример в сеансе оболочки:

&gt;&gt;&gt; frozenset(range(10))
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

И раз уж мы заговорили о синтаксисе, то отметим, что хорошо знакомый синтаксис спискового включения был приспособлен и для построения множеств.