---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.93
tokens: 7603
characters: 1678
timestamp: 2025-12-24T00:55:49.738151
finish_reason: stop
---

In[38]: pop.unstack(level=0)

Out[38]:   state    California    New York    Texas
          year
2000      33871648     18976457     20851820
2010      37253956     19378102     25145561

In[39]: pop.unstack(level=1)

Out[39]:   year    2000    2010
          state
California  33871648  37253956
New York    18976457  19378102
Texas       20851820  25145561

Методу unstack() противоположен по действию метод stack(), которым можно воспользоваться, чтобы получить обратно исходный ряд данных:

In[40]: pop.unstack().stack()

Out[40]:   state    year
           California  2000  33871648
                        2010  37253956
           New York    2000  18976457
                        2010  19378102
           Texas       2000  20851820
                        2010  25145561
    dtype: int64

Создание и перестройка индексов

Еще один способ перегруппировки иерархических данных — преобразовать метки индекса в столбцы с помощью метода reset_index. Результатом вызова этого метода для нашего ассоциативного словаря населения будет объект DataFrame со столбцами state (штат) и year (год), содержащими информацию, ранее находившуюся в индексе. Для большей ясности можно при желании задать название для представленных в виде столбцов данных:

In[41]: pop_flat = pop.reset_index(name='population')
        pop_flat

Out[41]:    state  year  population
0  California  2000  33871648
1  California  2010  37253956
2  New York   2000  18976457
3  New York   2010  19378102
4  Texas      2000  20851820
5  Texas      2010  25145561

При работе с реальными данными исходные входные данные очень часто выглядят подобным образом, поэтому удобно создать объект MultiIndex из значений