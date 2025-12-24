---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.19
tokens: 7547
characters: 1386
timestamp: 2025-12-24T02:44:24.157122
finish_reason: stop
---

**Арифметические операции и выравнивание данных**

pandas может сильно упростить работу с объектами, имеющими различные индексы. Так, если при сложении двух объектов в одном индексе обнаруживается значение, отсутствующее в другом, то результирующий индекс будет объединением исходных. Рассмотрим пример:

In [182]: s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])

In [183]: s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
.....: index=["a", "c", "e", "f", "g"])

In [184]: s1
Out[184]:
    a   7.3
    c  -2.5
    d   3.4
    e   1.5
dtype: float64

In [185]: s2
Out[185]:
    a  -2.1
    c   3.6
    e  -1.5
    f   4.0
    g   3.1
dtype: float64

Сложение этих объектов дает:

In [186]: s1 + s2
Out[186]:
    a   5.2
    c   1.1
    d   NaN
    e   0.0
    f   NaN
    g   NaN
dtype: float64

Вследствие внутреннего выравнивания данных образуются значения NaN в позициях, для которых не нашлось соответственной пары. Эти значения распространяются на последующие операции.

В случае DataFrame выравнивание производится как для строк, так и для столбцов:

In [187]: df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"),
.....: index=["Ohio", "Texas", "Colorado"])

In [188]: df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),
.....: index=["Utah", "Ohio", "Texas", "Oregon"])

In [189]: df1
Out[189]:
      b   c   d
Ohio  0.0  1.0  2.0