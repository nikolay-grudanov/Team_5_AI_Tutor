---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.53
tokens: 7731
characters: 2194
timestamp: 2025-12-24T00:56:32.340827
finish_reason: stop
---

population    True
state         False
area (sq. mi) True
dtype: bool

В столбце area имеются пустые значения. Посмотрим, какие территории не были учтены:

In[28]: final['state'][final['area (sq. mi)'].isnull()].unique()

Out[28]: array(['United States'], dtype=object)

Видим, что наш DataFrame-объект areas не содержит площадь США в целом. Мы могли бы вставить соответствующее значение (например, воспользовавшись суммой площадей всех штатов), но в данном случае мы просто удалим пустые значения, поскольку плотность населения США в целом нас сейчас не интересует:

In[29]: final.dropna(inplace=True)
    final.head()

Out[29]:   state/region  ages  year  population  state  area (sq. mi)
      0           AL  under18  2012     1117489.0  Alabama        52423.0
      1           AL    total  2012     4817528.0  Alabama        52423.0
      2           AL  under18  2010     1130966.0  Alabama        52423.0
      3           AL    total  2010     4785570.0  Alabama        52423.0
      4           AL  under18  2011     1125763.0  Alabama        52423.0

Теперь у нас есть все необходимые нам данные. Чтобы ответить на интересующий вопрос, сначала выберем часть данных, соответствующих 2010 году и всему населению. Воспользуемся функцией query() (для этого должен быть установлен пакет numexpr, см. раздел «Увеличение производительности библиотеки Pandas: eval() и query()» данной главы):

In[30]: data2010 = final.query("year == 2010 & ages == 'total'")
    data2010.head()

Out[30]:   state/region  ages  year  population  state  area (sq. mi)
      3           AL    total  2010     4785570.0  Alabama        52423.0
      91          AK    total  2010     713868.0   Alaska       656425.0
     101          AZ    total  2010     6408790.0  Arizona      114006.0
     189          AR    total  2010     2922280.0  Arkansas      53182.0
     197          CA    total  2010    37333601.0  California    163707.0

Теперь вычислим плотность населения и выведем данные в соответствующем порядке. Начнем с переиндексации наших данных по штату, после чего вычислим результат:

In[31]: data2010.set_index('state', inplace=True)
    density = data2010['population'] / data2010['area (sq. mi)']