---
source_image: page_419.png
page_number: 419
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.09
tokens: 7564
characters: 1696
timestamp: 2025-12-24T02:51:50.949242
finish_reason: stop
---

(74, 'Europe/London'),
(191, 'America/Denver'),
(382, 'America/Los_Angeles'),
(400, 'America/Chicago'),
(521, ''),
(1251, 'America/New_York')]

Пошарив в стандартной библиотеке Python, можно найти класс collections.Counter, который позволяет решить задачу еще проще:

In [25]: from collections import Counter

In [26]: counts = Counter(time_zones)

In [27]: counts.most_common(10)
Out[27]:
[('America/New_York', 1251),
('', 521),
('America/Chicago', 400),
('America/Los_Angeles', 382),
('America/Denver', 191),
('Europe/London', 74),
('Asia/Tokyo', 37),
('Pacific/Honolulu', 36),
('Europe/Madrid', 35),
('America/Sao_Paulo', 33)]

Подсчет часовых поясов с помощью pandas
Чтобы создать экземпляр DataFrame из исходного набора записей, следует передать список записей функции pandas.DataFrame:

In [28]: frame = pd.DataFrame(records)

Мы можем получить базовую информацию об этом новом объекте DataFrame, в частности имена столбцов, выведенные типы столбцов и количество отсутствующих значений, воспользовавшись методом frame.info():

In [29]: frame.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3560 entries, 0 to 3559
Data columns (total 18 columns):
#   Column    Non-Null Count Dtype
---  ------   -------------- -----
0   a         3440 non-null object
1   c         2919 non-null object
2   nk        3440 non-null float64
3   tz        3440 non-null object
4   gr        2919 non-null object
5   g          3440 non-null object
6   h          3440 non-null object
7   l          3440 non-null object
8   al         3094 non-null object
9   hh         3440 non-null object
10  r          3440 non-null object
11  u          3440 non-null object
12  t          3440 non-null float64