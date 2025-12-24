---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.57
tokens: 7476
characters: 1561
timestamp: 2025-12-24T00:55:12.969175
finish_reason: stop
---

In[19]: data['area']

Out[19]:    California   423967
              Florida     170312
           Illinois     149995
        New York     141297
             Texas     695662
Name: area, dtype: int64

Можно обращаться к данным и с помощью атрибутов, используя в их качестве строковые имена столбцов:

In[20]: data.area

Out[20]:    California   423967
              Florida     170312
           Illinois     149995
        New York     141297
             Texas     695662
Name: area, dtype: int64

При доступе по имени атрибута-столбца фактически происходит обращение к тому же объекту, что и при словарном варианте доступа:

In[21]: data.area is data['area']

Out[21]: True

Хотя это и удобное сокращенное написание, не забывайте, что оно работает не всегда! Например, если имена столбцов — не строки или имена столбцов конфликтуют с методами объекта DataFrame, доступ по именам атрибутов невозможен. Например, у объекта DataFrame есть метод pop(), так что выражение data.pop будет обозначать его, а не столбец "pop":

In[22]: data.pop is data['pop']

Out[22]: False

Не поддавайтесь искушению присваивать значения столбцов посредством атрибутов. Лучше использовать выражение data['pop'] = z вместо data.pop = z.

Как и в случае с обсуждавшимися ранее объектами Series, такой «словарный» синтаксис можно применять для модификации объекта, например добавления еще одного столбца:

In[23]: data['density'] = data['pop'] / data['area']
data

Out[23]:
      area    pop    density
California  423967  38332521  90.413926
Florida     170312  19552860  114.806121