---
source_image: page_191.png
page_number: 191
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.94
tokens: 7640
characters: 2324
timestamp: 2025-12-24T00:56:18.468973
finish_reason: stop
---

Задание операций над множествами для соединений

Во всех предыдущих примерах мы игнорировали один важный нюанс выполнения соединения — вид используемой при соединении операции алгебры множеств. Это играет важную роль в случаях, когда какое-либо значение есть в одном ключевом столбце, но отсутствует в другом. Рассмотрим следующий пример:

In[13]: df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                           'food': ['fish', 'beans', 'bread']},
                           columns=['name', 'food'])
    df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                        'drink': ['wine', 'beer']},
                        columns=['name', 'drink'])
    print(df6); print(df7); print(pd.merge(df6, df7))

df6
   name   food
0  Peter   fish
1  Paul  beans
2  Mary  bread

df7
   name   drink
0  Mary   wine
1 Joseph   beer

pd.merge(df6, df7)
   name   food   drink
0  Mary  bread   wine

Здесь мы слили воедино два набора данных, у которых совпадает только одна запись name: Mary. По умолчанию результат будет содержать пересечение двух входных множеств — внутреннее соединение (inner join). Можно указать это явным образом, с помощью ключевого слова how, имеющего по умолчанию значение 'inner':

In[14]: pd.merge(df6, df7, how='inner')

Out[14]:    name   food   drink
0      Mary  bread   wine

Другие возможные значения ключевого слова how: 'outer', 'left' и 'right'. Внешнее соединение (outer join) означает соединение по объединению входных столбцов и заполняет значениями NA все пропуски значений:

In[15]: print(df6); print(df7); print(pd.merge(df6, df7, how='outer'))

df6
   name   food
0  Peter   fish
1  Paul  beans
2  Mary  bread

df7
   name   drink
0  Mary   wine
1 Joseph   beer

pd.merge(df6, df7, how='outer')
   name   food   drink
0  Peter   fish   NaN
1  Paul  beans   NaN
2  Mary  bread  wine
3 Joseph   NaN  beer

Левое соединение (left join) и правое соединение (right join) выполняют соединение по записям слева и справа соответственно. Например:

In[16]: print(df6); print(df7); print(pd.merge(df6, df7, how='left'))

df6
   name   food
0  Peter   fish
1  Paul  beans
2  Mary  bread

df7
   name   drink
0  Mary   wine
1 Joseph   beer

pd.merge(df6, df7, how='left')
   name   food   drink
0  Peter   fish   NaN
1  Paul  beans   NaN
2  Mary  bread  wine
3 Joseph   NaN  beer