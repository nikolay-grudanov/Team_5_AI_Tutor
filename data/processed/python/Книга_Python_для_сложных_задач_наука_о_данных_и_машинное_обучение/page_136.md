---
source_image: page_136.png
page_number: 136
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.22
tokens: 7440
characters: 1660
timestamp: 2025-12-24T00:54:58.297275
finish_reason: stop
---

In[19]: states = pd.DataFrame({'population': population,
                             'area': area})
    states

Out[19]:
      area  population
California   423967     38332521
Florida      170312     19552860
Illinois     149995     12882135
New York     141297     19651127
Texas        695662     26448193

Аналогично объекту Series у объекта DataFrame имеется атрибут index, обеспечивающий доступ к меткам индекса:

In[20]: states.index

Out[20]:
Index(['California', 'Florida', 'Illinois', 'New York', 'Texas'],
      dtype='object')

Помимо этого, у объекта DataFrame есть атрибут columns, представляющий собой содержащий метки столбцов объект Index:

In[21]: states.columns

Out[21]: Index(['area', 'population'], dtype='object')

Таким образом, объект DataFrame можно рассматривать как обобщение двумерного массива NumPy, где как у строк, так и у столбцов есть обобщенные индексы для доступа к данным.

Объект DataFrame как специализированный словарь

DataFrame можно рассматривать как специализированный словарь. Если словарь задает соответствие ключей значениям, то DataFrame задает соответствие имени столбца объекту Series с данными этого столбца. Например, запрос данных по атрибуту 'area' приведет к тому, что будет возвращен объект Series, содержащий уже виденные нами ранее площади штатов:

In[22]: states['area']

Out[22]: California    423967
         Florida       170312
         Illinois      149995
         New York      141297
         Texas         695662
         Name: area, dtype: int64

Обратите внимание на возможный источник путаницы: в двумерном массиве NumPy data[0] возвращает первую строку. По этой причине объекты DataFrame