---
source_image: page_235.png
page_number: 235
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.07
tokens: 7766
characters: 1913
timestamp: 2025-12-24T02:46:32.417700
finish_reason: stop
---

Расширенные типы можно передавать методу astype объекта Series, что упрощает преобразования в процессе очистки:

In [145]: df = pd.DataFrame({"A": [1, 2, None, 4],
    ....:
    ....:
    "B": ["one", "two", "three", None],
    "C": [False, None, False, True]})

In [146]: df
Out[146]:
   A    B    C
0  1.0  one  False
1  2.0  two  None
2  NaN  three  False
3  4.0  None  True

In [147]: df["A"] = df["A"].astype("Int64")

In [148]: df["B"] = df["B"].astype("string")

In [149]: df["C"] = df["C"].astype("boolean")

In [150]: df
Out[150]:
   A    B    C
0  1  one  False
1  2  two  <NA>
2  <NA>  three  False
3  4  <NA>  True

Таблица 7.3. Расширенные типы данных в pandas

<table>
  <tr>
    <th>Расширенный тип</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>BooleanDtype</td>
    <td>Булев тип, допускающий null; в виде строки передавать "boolean"</td>
  </tr>
  <tr>
    <td>CategoricalDtype</td>
    <td>Категориальный тип; в виде строки передавать "category"</td>
  </tr>
  <tr>
    <td>DatetimeTZDtype</td>
    <td>Дата и время с часовым поясом</td>
  </tr>
  <tr>
    <td>Float32Dtype</td>
    <td>32-разрядный тип с плавающей точкой, допускающий null; в виде строки передавать "Float32"</td>
  </tr>
  <tr>
    <td>Float64Dtype</td>
    <td>64-разрядный тип с плавающей точкой, допускающий null; в виде строки передавать "Float64"</td>
  </tr>
  <tr>
    <td>Int8Dtype</td>
    <td>8-разрядный тип целого со знаком, допускающий null; в виде строки передавать "Int8"</td>
  </tr>
  <tr>
    <td>Int16Dtype</td>
    <td>16-разрядный тип целого со знаком, допускающий null; в виде строки передавать "Int16"</td>
  </tr>
  <tr>
    <td>Int32Dtype</td>
    <td>32-разрядный тип целого со знаком, допускающий null; в виде строки передавать "Int32"</td>
  </tr>
  <tr>
    <td>Int64Dtype</td>
    <td>64-разрядный тип целого со знаком, допускающий null; в виде строки передавать "Int64"</td>
  </tr>
</table>