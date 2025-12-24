---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.50
tokens: 7743
characters: 2098
timestamp: 2025-12-24T00:56:50.150417
finish_reason: stop
---

<table>
  <tr>
    <th></th>
    <th colspan="3">min median max</th>
    <th colspan="3">min median max</th>
  </tr>
  <tr>
    <th>key</th>
    <th>A</th>
    <th>B</th>
    <th>C</th>
    <th>A</th>
    <th>B</th>
    <th>C</th>
  </tr>
  <tr>
    <td></td>
    <td>0</td>
    <td>1.5</td>
    <td>3</td>
    <td>3</td>
    <td>4.0</td>
    <td>5</td>
  </tr>
  <tr>
    <td></td>
    <td>1</td>
    <td>2.5</td>
    <td>4</td>
    <td>0</td>
    <td>3.5</td>
    <td>7</td>
  </tr>
  <tr>
    <td></td>
    <td>2</td>
    <td>3.5</td>
    <td>5</td>
    <td>3</td>
    <td>6.0</td>
    <td>9</td>
  </tr>
</table>

Еще один удобный паттерн — передача в него словаря, связывающего имена столбцов с операциями, которые должны быть применены к этим столбцам:

In[21]: df.groupby('key').aggregate({'data1': 'min',
                                   'data2': 'max'})
Out[21]:   data1  data2
          key
          A      0      5
          B      1      7
          C      2      9

Фильтрация. Операция фильтрации дает возможность опускать данные в зависимости от свойств группы. Например, нам может понадобиться оставить в результате все группы, в которых стандартное отклонение превышает какое-либо критическое значение:

In[22]:
def filter_func(x):
    return x['data2'].std() > 4

print(df); print(df.groupby('key').std());
print(df.groupby('key').filter(filter_func))

df
  key  data1  data2
0  A      0      5
1  B      1      0
2  C      2      3
3  A      3      3
4  B      4      7
5  C      5      9

df.groupby('key').std()
  key  data1  data2
A   2.12132  1.414214
B   2.12132  4.949747
C   2.12132  4.242641

df.groupby('key').filter(filter_func)
  key  data1  data2
1  B      1      0
2  C      2      3
4  B      4      7
5  C      5      9

Функция filter() возвращает булево значение, определяющее, прошла ли группа фильтрацию. В данном случае, поскольку стандартное отклонение группы А превышает 4, она удаляется из итогового результата.

Преобразование. В то время как агрегирующая функция должна возвращать сокращенную версию данных, преобразование может вернуть версию полного