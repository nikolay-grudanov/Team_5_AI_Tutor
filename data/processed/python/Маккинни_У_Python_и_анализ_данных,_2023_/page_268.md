---
source_image: page_268.png
page_number: 268
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.49
tokens: 7728
characters: 1551
timestamp: 2025-12-24T02:47:26.108272
finish_reason: stop
---

In [69]: lefth
Out[69]:
    key1   key2   data
0   Ohio   2000   0
1   Ohio   2001   1
2   Ohio   2002   2
3  Nevada   2001   3
4  Nevada   2002   4

In [70]: righth
Out[70]:
      event1   event2
Nevada   2001   0   1
          2000   2   3
Ohio     2000   4   5
          2000   6   7
          2001   8   9
          2002  10  11

В этом случае необходимо перечислить столбцы, по которым производится соединение, в виде списка (обратите внимание на обработку повторяющихся значений в индексе, когда how='outer'):

In [71]: pd.merge(lefth, righth, left_on=["key1", "key2"], right_index=True)
Out[71]:
    key1   key2   data   event1   event2
0   Ohio   2000   0   4   5
1   Ohio   2000   0   6   7
2   Ohio   2001   1   8   9
3   Ohio   2002   2  10  11
3  Nevada   2001   3   0   1

In [72]: pd.merge(lefth, righth, left_on=["key1", "key2"],
.....:     right_index=True, how="outer")
Out[72]:
    key1   key2   data   event1   event2
0   Ohio   2000   0   4   5
1   Ohio   2000   0   6   7
2   Ohio   2001   1   8   9
3   Ohio   2002   2  10  11
3  Nevada   2001   3   0   1
4  Nevada   2002   4 <NA> <NA>
4  Nevada   2000 <NA>   2   3

Использовать индексы в обеих частях слияния тоже возможно:

In [73]: left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
.....:     index=["a", "c", "e"],
.....:     columns=["Ohio", "Nevada"]).astype("Int64")

In [74]: right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
.....:     index=["b", "c", "d", "e"],
.....:     columns=["Missouri", "Alabama"]).astype("Int64")

In [75]: left2
Out[75]: