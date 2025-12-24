---
source_image: page_428.png
page_number: 428
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.93
tokens: 7522
characters: 2072
timestamp: 2025-12-24T01:02:20.598664
finish_reason: stop
---

Испытанным методом для такого случая является прямое кодирование (one-hot encoding), означающее создание дополнительных столбцов-индикаторов наличия/отсутствия категории с помощью значений 1 или 0 соответственно. При наличии данных в виде списка словарей для этой цели можно воспользоваться утилитой DictVectorizer библиотеки Scikit-Learn:

In[3]: from sklearn.feature_extraction import DictVectorizer
    vec = DictVectorizer(sparse=False, dtype=int)
    vec.fit_transform(data)

Out[3]: array([[   0,      1,      0, 850000,      4],
                [   1,      0,      0, 700000,      3],
                [   0,      0,      1, 650000,      3],
                [   1,      0,      0, 600000,      2]], dtype=int64)

Обратите внимание, что столбец neighborhood превратился в три отдельных столбца, отражающих три метки микрорайонов, и что в каждой строке стоит 1 в соответствующем ее микрорайону столбце. После подобного кодирования категориальных признаков можно продолжить обучение модели Scikit-Learn обычным образом.

Чтобы узнать, что означает каждый столбец, можно посмотреть названия признаков:

In[4]: vec.get_feature_names()

Out[4]: ['neighborhood=Fremont',
         'neighborhood=Queen Anne',
         'neighborhood=Wallingford',
         'price',
         'rooms']

У этого подхода имеется один очевидный недостаток: если количество значений категории велико, размер набора данных может значительно вырасти. Однако поскольку кодированные данные состоят в основном из нулей, эффективным решением будет разреженный формат вывода:

In[5]: vec = DictVectorizer(sparse=True, dtype=int)
    vec.fit_transform(data)

Out[5]: <4x5 sparse matrix of type '<class 'numpy.int64'>'
    with 12 stored elements in Compressed Sparse Row format>

Многие (хотя пока не все) оцениватели библиотеки Scikit-Learn допускают передачу им подобных разреженных входных данных при обучении и оценке моделей. Для поддержки подобного кодирования библиотека Scikit-Learn включает две дополнительные утилиты: sklearn.preprocessing.OneHotEncoder и sklearn.feature_extraction.FeatureHasher.