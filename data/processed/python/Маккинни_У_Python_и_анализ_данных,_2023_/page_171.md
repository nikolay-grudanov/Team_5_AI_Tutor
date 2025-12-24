---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.51
tokens: 7664
characters: 1417
timestamp: 2025-12-24T02:44:38.290791
finish_reason: stop
---

Если вы хотите вместо этого сопоставлять строки, а укладывать столбцы, то должны будете воспользоваться каким-нибудь арифметическим методом, указав сопоставление по индексу. Например:

In [219]: series3 = frame["d"]

In [220]: frame
Out[220]:
      b   d   e
Utah  0.0  1.0  2.0
Ohio  3.0  4.0  5.0
Texas 6.0  7.0  8.0
Oregon 9.0 10.0 11.0

In [221]: series3
Out[221]:
Utah    1.0
Ohio    4.0
Texas   7.0
Oregon  10.0
Name: d, dtype: float64

In [222]: frame.sub(series3, axis="index")
Out[222]:
      b   d   e
Utah -1.0  0.0  1.0
Ohio -1.0  0.0  1.0
Texas -1.0  0.0  1.0
Oregon -1.0  0.0  1.0

Передаваемый номер оси — это ось, вдоль которой производится сопоставление. В данном случае мы хотим сопоставлять с индексом строк DataFrame (axis="index") и укладывать поперек.

Применение функций и отображение
Универсальные функции NumPy (поэлементные методы массивов) отлично работают и с объектами pandas:

In [223]: frame = pd.DataFrame(np.random.standard_normal((4, 3)),
    ....:                 columns=list("bde"),
    ....:                 index=["Utah", "Ohio", "Texas", "Oregon"])

In [224]: frame
Out[224]:
      b         d         e
Utah -0.204708  0.478943 -0.519439
Ohio -0.555730  1.965781  1.393406
Texas 0.092908  0.281746  0.769023
Oregon 1.246435  1.007189 -1.296221

In [225]: np.abs(frame)
Out[225]:
      b         d         e
Utah  0.204708  0.478943  0.519439
Ohio  0.555730  1.965781  1.393406