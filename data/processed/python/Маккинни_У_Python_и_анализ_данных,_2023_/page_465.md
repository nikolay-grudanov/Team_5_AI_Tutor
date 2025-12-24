---
source_image: page_465.png
page_number: 465
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.77
tokens: 7820
characters: 1945
timestamp: 2025-12-24T02:53:15.002214
finish_reason: stop
---

Изменение формы массива

Во многих случаях изменить форму массива можно без копирования данных. Для этого следует передать кортеж с описанием новой формы методу экземпляра массива reshape. Например, предположим, что имеется одномерный массив, который мы хотели бы преобразовать в матрицу (результат показан на рис. А.3):

In [20]: arr = np.arange(8)

In [21]: arr
Out[21]: array([0, 1, 2, 3, 4, 5, 6, 7])

In [22]: arr.reshape((4, 2))
Out[22]:
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7]])

<table>
  <tr>
    <th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th>
  </tr>
  <tr>
    <td colspan="12">arr.reshape((4,3), order=?)<br>Порядок, принятый в C<br>(по строкам)</td>
  </tr>
  <tr>
    <td>0</td><td>1</td><td>2</td>
    <td>3</td><td>4</td><td>5</td>
    <td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td>
  </tr>
  <tr>
    <td colspan="3">order='C'</td>
    <td colspan="3">order='F'</td>
  </tr>
  <tr>
    <td colspan="3">
      <table border="1">
        <tr><th>0</th><th>1</th><th>2</th></tr>
        <tr><td>3</td><td>4</td><td>5</td></tr>
        <tr><td>6</td><td>7</td><td>8</td></tr>
        <tr><td>9</td><td>10</td><td>11</td></tr>
      </table>
    </td>
    <td colspan="3">
      <table border="1">
        <tr><th>0</th><th>4</th><th>8</th></tr>
        <tr><td>1</td><td>5</td><td>9</td></tr>
        <tr><td>2</td><td>6</td><td>10</td></tr>
        <tr><td>3</td><td>7</td><td>11</td></tr>
      </table>
    </td>
  </tr>
</table>

Рис. А.3. Изменение формы с преобразованием в двумерный массив, организованный как в C (по строкам) и как в Fortran (по столбцам)

Форму многомерного массива также можно изменить:

In [23]: arr.reshape((4, 2)).reshape((2, 4))
Out[23]:
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])

Одно из измерений, переданных в описателе формы, может быть равно −1, его значение будет выведено из данных: