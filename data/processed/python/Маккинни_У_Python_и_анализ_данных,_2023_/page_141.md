---
source_image: page_141.png
page_number: 141
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.65
tokens: 7590
characters: 1730
timestamp: 2025-12-24T02:43:49.459958
finish_reason: stop
---

Если имеется словарь Python, содержащий данные, то из него можно создать объект Series:

In [30]: sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}

In [31]: obj3 = pd.Series(sdata)

In [32]: obj3
Out[32]:
Ohio    35000
Texas   71000
Oregon  16000
Utah    5000
dtype: int64

Объект Series можно преобразовать обратно в словарь методом to_dict:

In [33]: obj3.to_dict()
Out[33]: {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

Если передается только словарь, то в индексе получившегося объекта Series ключи будут храниться в порядке, который определяется методом словаря keys и зависит от того, в каком порядке ключи вставлялись. Этот порядок можно переопределить, передав индекс, содержащий ключи словаря в том порядке, в каком они должны находиться в результирующем объекте Series:

In [34]: states = ["California", "Ohio", "Oregon", "Texas"]

In [35]: obj4 = pd.Series(sdata, index=states)

In [36]: obj4
Out[36]:
California      NaN
Ohio            35000.0
Oregon          16000.0
Texas           71000.0
dtype: float64

В данном случае три значения, найденных в sdata, помещены в соответствующие им позиции, а для метки 'California' никакого значения не нашлось, поэтому ей соответствует признак NaN (не число), которым в pandas обозначаются отсутствующие значения. Поскольку строки 'Utah' не было в списке states, то ее нет и в результирующем объекте.

Говоря об отсутствующих данных, я буду употреблять термины «NA» и «null» как синонимы. Для распознавания отсутствующих данных в pandas следует использовать функции isna и notna:

In [37]: pd.isna(obj4)
Out[37]:
California    True
Ohio          False
Oregon        False
Texas         False
dtype: bool

In [38]: pd.notna(obj4)
Out[38]: