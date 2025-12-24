---
source_image: page_173.png
page_number: 173
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.84
tokens: 7658
characters: 1540
timestamp: 2025-12-24T02:44:43.687793
finish_reason: stop
---

<table>
  <tr>
    <th></th>
    <th>b</th>
    <th>d</th>
    <th>e</th>
  </tr>
  <tr>
    <td>Utah</td>
    <td>-0.20</td>
    <td>0.48</td>
    <td>-0.52</td>
  </tr>
  <tr>
    <td>Ohio</td>
    <td>-0.56</td>
    <td>1.97</td>
    <td>1.39</td>
  </tr>
  <tr>
    <td>Texas</td>
    <td>0.09</td>
    <td>0.28</td>
    <td>0.77</td>
  </tr>
  <tr>
    <td>Oregon</td>
    <td>1.25</td>
    <td>1.01</td>
    <td>-1.30</td>
  </tr>
</table>

Этот метод называется applymap, потому что в классе Series есть метод map для применения функции к каждому элементу:

In [233]: frame["e"].map(my_format)
Out[233]:
Utah   -0.52
Ohio   1.39
Texas  0.77
Oregon -1.30
Name: e, dtype: object

Сортировка и ранжирование
Сортировка набора данных по некоторому критерию — еще одна важная встроенная операция. Для лексикографической сортировки по индексу служит метод sort_index, который возвращает новый отсортированный объект:

In [234]: obj = pd.Series(np.arange(4), index=["d", "a", "b", "c"])

In [235]: obj
Out[235]:
d    0
a    1
b    2
c    3
dtype: int64

In [236]: obj.sort_index()
Out[236]:
a    1
b    2
c    3
d    0
dtype: int64

В случае DataFrame можно сортировать по индексу, ассоциированному с любой осью:

In [237]: frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
.....:                index=["three", "one"],
.....:                columns=["d", "a", "b", "c"])

In [238]: frame
Out[238]:
     d  a  b  c
three 0  1  2  3
one    4  5  6  7

In [239]: frame.sort_index()
Out[239]:
     d  a  b  c
three 0  1  2  3
one    4  5  6  7