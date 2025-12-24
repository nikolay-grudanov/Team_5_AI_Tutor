---
source_image: page_422.png
page_number: 422
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.22
tokens: 7745
characters: 2301
timestamp: 2025-12-24T02:52:02.214255
finish_reason: stop
---

<table>
  <tr>
    <th>Opera/9.80</th>
    <td>34</td>
  </tr>
  <tr>
    <th>TEST_INTERNET_AGENT</th>
    <td>24</td>
  </tr>
  <tr>
    <th>GoogleProducer</th>
    <td>21</td>
  </tr>
  <tr>
    <th>Mozilla/6.0</th>
    <td>5</td>
  </tr>
  <tr>
    <th>BlackBerry8520/5.0.0.681</th>
    <td>4</td>
  </tr>
  <tr>
    <th>dtype: int64</th>
    <td></td>
  </tr>
</table>

Предположим теперь, что требуется разделить пользователей в первых 10 часовых поясах на работающих в Windows и всех прочих. Упростим задачу, предположив, что пользователь работает в Windows, если строка агента содержит подстроку "Windows". Но строка агента не всегда присутствует, поэтому записи, в которых ее нет, я исключаю:

In [47]: cframe = frame[frame["a"].notna()].copy()

Мы хотим вычислить значение, показывающее, относится строка к пользователю Windows или нет:

In [48]: cframe["os"] = np.where(cframe["a"].str.contains("Windows"),
    ....:                "Windows", "Not Windows")

In [49]: cframe["os"].head(5)
Out[49]:
0    Windows
1    Not Windows
2    Windows
3    Not Windows
4    Windows
Name: os, dtype: object

Затем мы можем сгруппировать данные по часовому поясу и только что сформированному столбцу с типом операционной системы:

In [50]: by_tz_os = cframe.groupby(["tz", "os"])

Групповые счетчики по аналогии с рассмотренной выше функцией value_counts можно вычислить с помощью функции size. А затем преобразовать результат в таблицу с помощью unstack:

In [51]: agg_counts = by_tz_os.size().unstack().fillna(0)

In [52]: agg_counts.head()
Out[52]:
           Not Windows  Windows
os         Africa/Cairo  Africa/Casablanca  Africa/Ceuta  Africa/Johannesburg
tz
Africa/Cairo        0.0              3.0          0.0                  0.0
Africa/Casablanca   0.0              1.0          0.0                  0.0
Africa/Ceuta        0.0              2.0          0.0                  0.0
Africa/Johannesburg 0.0              1.0          0.0                  0.0

Наконец, выберем из полученной таблицы первые 10 часовых поясов. Для этого я построю косвенный индексный массив по счетчикам строк в agg_counts. После вычисления счетчиков строк с помощью agg_counts.sum("columns") я могу вызвать argsort() и получить индексный массив, который можно будет использовать для сортировки в порядке возрастания: