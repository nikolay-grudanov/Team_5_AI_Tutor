---
source_image: page_101.png
page_number: 101
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.20
tokens: 7551
characters: 1777
timestamp: 2025-12-24T00:54:11.443337
finish_reason: stop
---

Out[9]: array([ True,  True, False,  True,  True], dtype=bool)

In[10]: x == 3  # равно

Out[10]: array([False, False,  True, False, False], dtype=bool)

Можно также выполнять поэлементное сравнение двух массивов и использовать составные выражения:

In[11]: (2 * x) == (x ** 2)

Out[11]: array([False,  True, False, False, False], dtype=bool)

Как и в случае арифметических операторов, операторы сравнения реализованы в библиотеке NumPy как универсальные функции (табл. 2.4). Например, когда вы пишете x < 3, библиотека NumPy на самом деле использует внутри функцию np.less(x, 3).

Таблица 2.4. Краткий список операторов сравнения и эквивалентных им универсальных функций

<table>
  <tr>
    <th>Оператор</th>
    <th>Эквивалентная универсальная функция</th>
  </tr>
  <tr>
    <td>= =</td>
    <td>np.equal</td>
  </tr>
  <tr>
    <td>!=</td>
    <td>np.not_equal</td>
  </tr>
  <tr>
    <td>&lt;</td>
    <td>np.less</td>
  </tr>
  <tr>
    <td>&lt;=</td>
    <td>np.less_equal</td>
  </tr>
  <tr>
    <td>&gt;</td>
    <td>np.greater</td>
  </tr>
  <tr>
    <td>&gt;=</td>
    <td>np.greater_equal</td>
  </tr>
</table>

Как и в случае с арифметическими универсальными функциями, они могут работать с массивами любого размера и формы. Вот пример для двумерного массива:

In[12]: rng = np.random.RandomState(0)
        x = rng.randint(10, size=(3, 4))
        x

Out[12]: array([[5, 0, 3, 3],
                [7, 9, 3, 5],
                [2, 4, 7, 6]])

In[13]: x < 6

Out[13]: array([[ True,  True,  True,  True],
                [False, False,  True,  True],
                [ True,  True, False, False]], dtype=bool)

Во всех случаях результат представляет собой булев массив, и в библиотеке NumPy имеется набор простых паттернов для работы с этими булевыми результатами.