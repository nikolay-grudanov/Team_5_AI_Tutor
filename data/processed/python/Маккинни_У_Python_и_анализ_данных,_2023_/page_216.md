---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.68
tokens: 7538
characters: 1174
timestamp: 2025-12-24T02:45:53.623844
finish_reason: stop
---

In [27]: data
Out[27]:
    0   1   2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0

In [28]: data.dropna()
Out[28]:
    0   1   2
0  1.0  6.5  3.0

Если передать параметр how='all', то будут отброшены строки, которые целиком состоят из отсутствующих значений:

In [29]: data.dropna(how="all")
Out[29]:
    0   1   2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
3  NaN  6.5  3.0

Имейте в виду, что эти функции по умолчанию возвращают новые объекты, а не модифицируют содержимое исходного.
Для подобного же отбрасывания столбцов достаточно передать параметр axis=1:

In [30]: data[4] = np.nan

In [31]: data
Out[31]:
    0   1   2   4
0  1.0  6.5  3.0  NaN
1  1.0  NaN  NaN  NaN
2  NaN  NaN  NaN  NaN
3  NaN  6.5  3.0  NaN

In [32]: data.dropna(axis="columns", how="all")
Out[32]:
    0   1   2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0

Допустим, требуется оставить только строки, содержащие определенное количество отсутствующих наблюдений. Этот порог можно задать с помощью аргумента thresh:

In [33]: df = pd.DataFrame(np.random.standard_normal((7, 3)))

In [34]: df.iloc[:4, 1] = np.nan

In [35]: df.iloc[:2, 2] = np.nan

In [36]: df