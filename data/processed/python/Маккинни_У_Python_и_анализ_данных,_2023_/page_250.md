---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.83
tokens: 7608
characters: 1589
timestamp: 2025-12-24T02:46:54.570663
finish_reason: stop
---

In [239]: bins = pd.Series(bins, name='quartile')

In [240]: results = (pd.Series(draws)
.....:         .groupby(bins)
.....:         .agg(['count', 'min', 'max'])
.....:         .reset_index())

In [241]: results
Out[241]:
    quartile  count      min      max
0        Q1   250 -3.119609 -0.678494
1        Q2   250 -0.673305  0.008009
2        Q3   250  0.018753  0.686183
3        Q4   250  0.688282  3.211418

В столбце результата 'quartile' сохранена исходная категориальная информация из bins, включая упорядочение:

In [242]: results['quartile']
Out[242]:
0    Q1
1    Q2
2    Q3
3    Q4
Name: quartile, dtype: category
Categories (4, object): ['Q1' < 'Q2' < 'Q3' < 'Q4']

Повышение производительности с помощью перехода к категориальным данным
В начале этого раздела я сказал, что категориальные типы могут улучшить производительность и потребление памяти, теперь приведу несколько примеров. Рассмотрим объект Series, содержащий 10 млн элементов и небольшое число различных категорий:

In [243]: N = 10_000_000

In [244]: labels = pd.Series(['foo', 'bar', 'baz', 'qux'] * (N // 4))

Теперь преобразуем labels в категориальную форму:

In [245]: categories = labels.astype('category')

Заметим, что labels занимает гораздо меньше памяти, чем categories:

In [246]: labels.memory_usage(deep=True)
Out[246]: 600000128

In [247]: categories.memory_usage(deep=True)
Out[247]: 10000540

Разумеется, переход к категориям обходится не бесплатно, но это одноразовые затраты:

In [248]: %time _ = labels.astype('category')
CPU times: user 469 ms, sys: 106 ms, total: 574 ms
Wall time: 577 ms