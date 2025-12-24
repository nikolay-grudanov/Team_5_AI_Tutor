---
source_image: page_474.png
page_number: 474
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.54
tokens: 7696
characters: 1488
timestamp: 2025-12-24T02:53:25.842461
finish_reason: stop
---

In [89]: arr
Out[89]:
array([[1.7247, 2.6182, 0.7774],
       [0.8286, -0.959 , -1.2094],
       [-1.4123, 0.5415, 0.7519],
       [-0.6588, -1.2287, 0.2576]])

In [90]: row_means = arr.mean(1)

In [91]: row_means.shape
Out[91]: (4,)

In [92]: row_means.reshape((4, 1))
Out[92]:
array([[1.7068],
       [-0.4466],
       [-0.0396],
       [-0.5433]])

In [93]: demeaned = arr - row_means.reshape((4, 1))

In [94]: demeaned.mean(1)
Out[94]: array([-0., 0., 0., 0.])

Эта операция проиллюстрирована на рис. А.5.

<table>
  <tr>
    <th>(4,3)</th>
    <th>(4,1)</th>
    <th>(4,3)</th>
  </tr>
  <tr>
    <td>
      <table>
        <tr><th>0</th><th>0</th><th>0</th></tr>
        <tr><th>1</th><th>1</th><th>1</th></tr>
        <tr><th>2</th><th>2</th><th>2</th></tr>
        <tr><th>3</th><th>3</th><th>3</th></tr>
      </table>
    </td>
    <td>
      <table>
        <tr><th>1</th><th>1</th><th>1</th></tr>
        <tr><th>2</th><th>2</th><th>2</th></tr>
        <tr><th>3</th><th>3</th><th>3</th></tr>
        <tr><th>4</th><th>4</th><th>4</th></tr>
      </table>
    </td>
    <td>
      <table>
        <tr><th>1</th><th>1</th><th>1</th></tr>
        <tr><th>3</th><th>3</th><th>3</th></tr>
        <tr><th>5</th><th>5</th><th>5</th></tr>
        <tr><th>7</th><th>7</th><th>7</th></tr>
      </table>
    </td>
  </tr>
</table>

Рис. А.5. Укладывание по оси 1 двумерного массива

На рис. А.6 приведена еще одна иллюстрация, где мы вычитаем двумерный массив из трехмерного по оси 0.