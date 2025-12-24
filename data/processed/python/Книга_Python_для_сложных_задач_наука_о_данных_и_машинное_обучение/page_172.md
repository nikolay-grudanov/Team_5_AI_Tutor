---
source_image: page_172.png
page_number: 172
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.44
tokens: 7465
characters: 1392
timestamp: 2025-12-24T00:55:33.567589
finish_reason: stop
---

In[24]: pop.loc['California':'New York']

Out[24]: state    year
      California   2000   33871648
                  2010   37253956
      New York     2000   18976457
                  2010   19378102
      dtype: int64

С помощью отсортированных индексов можно выполнять частичную индексацию по нижним уровням, указав пустой срез в первом индексе:

In[25]: pop[:, 2000]

Out[25]: state
      California   33871648
      New York     18976457
      Texas        20851820
      dtype: int64

Другие типы индексации и выборки (обсуждаемые в разделе «Индексация и выборка данных» этой главы) тоже работают. Выборка данных на основе булевой маски:

In[26]: pop[pop > 22000000]

Out[26]: state    year
      California   2000   33871648
                  2010   37253956
      Texas        2010   25145561
      dtype: int64

Выборка на основе «прихотливой» индексации:

In[27]: pop[['California', 'Texas']]

Out[27]: state    year
      California   2000   33871648
                  2010   37253956
      Texas        2000   20851820
                  2010   25145561
      dtype: int64

Мультииндексация объектов DataFrame

Мультииндексированные объекты DataFrame ведут себя аналогичным образом. Рассмотрим наш модельный медицинский объект DataFrame:

In[28]: health_data

Out[28]: subject    Bob    Guido    Sue
      type         HR     Temp     HR     Temp     HR     Temp
      year visit