---
source_image: page_091.png
page_number: 91
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.08
tokens: 7685
characters: 2200
timestamp: 2025-12-24T02:42:24.181940
finish_reason: stop
---

Таблица 3.2. Некоторые полезные функции из модуля itertools

<table>
  <tr>
    <th>Функция</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>chain(*iterables)</td>
    <td>Генерирует последовательность сцепленных итераторов. После исчерпания элементов в первом итераторе возвращаются элементы из второго и т. д.</td>
  </tr>
  <tr>
    <td>combinations(iterable, k)</td>
    <td>Генерирует последовательность всех возможных k-кортежей, составленных из элементов iterable, без учета порядка</td>
  </tr>
  <tr>
    <td>permutations(iterable, k)</td>
    <td>Генерирует последовательность всех возможных k-кортежей, составленных из элементов iterable, с учетом порядка</td>
  </tr>
  <tr>
    <td>groupby(iterable[, keyfunc])</td>
    <td>Генерирует пары (ключ, субитератор) для каждого уникального ключа</td>
  </tr>
  <tr>
    <td>product(*iterables, repeat=1)</td>
    <td>Генерирует декартово произведение входных итерируемых величин в виде кортежей, как если бы использовался вложенный цикл for</td>
  </tr>
</table>

Обработка исключений
Обработка ошибок, или исключений, в Python — важная часть создания надежных программ. В приложениях для анализа данных многие функции работают только для входных данных определенного вида. Например, функция float может привести строку к типу числа с плавающей точкой, но если формат строки заведомо некорректен, то завершается с ошибкой ValueError:

In [224]: float("1.2345")
Out[224]: 1.2345

In [225]: float("something")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-225-5ccfe07933f4> in <module>
----> 1 float("something")
ValueError: could not convert string to float: 'something'

Пусть требуется написать версию float, которая не завершается с ошибкой, а возвращает поданный на вход аргумент. Это можно сделать, обернув вызов float блоком try/except:

def attempt_float(x):
    try:
        return float(x)
    except:
        return x

Код в части except будет выполняться, только если float(x) возбуждает исключение:

In [227]: attempt_float("1.2345")
Out[227]: 1.2345

In [228]: attempt_float("something")
Out[228]: 'something'