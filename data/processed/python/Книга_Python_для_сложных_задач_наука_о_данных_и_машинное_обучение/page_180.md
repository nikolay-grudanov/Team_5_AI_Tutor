---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.56
tokens: 7511
characters: 1776
timestamp: 2025-12-24T00:55:55.939015
finish_reason: stop
---

180 Глава 3 • Манипуляции над данными с помощью пакета Pandas

In[5]: x = [[1, 2],
           [3, 4]]
    np.concatenate([x, x], axis=1)

Out[5]: array([[1, 2, 1, 2],
              [3, 4, 3, 4]])

Простая конкатенация с помощью метода pd.concat

В библиотеке Pandas имеется функция, pd.concat(), синтаксис которой аналогичен функции np.concatenate, однако она содержит множество параметров, которые мы вскоре обсудим:

# Сигнатура функции pd.concat в библиотеке Pandas v0.18
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)

Функцию pd.concat можно использовать для простой конкатенации объектов Series или DataFrame аналогично тому, как функцию np.concatenate() можно применять для простой конкатенации массивов:

In[6]: ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
    ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
    pd.concat([ser1, ser2])

Out[6]:  1    A
         2    B
         3    C
         4    D
         5    E
         6    F
    dtype: object

Она также подходит для конкатенации объектов более высокой размерности, таких как DataFrame:

In[7]: df1 = make_df('AB', [1, 2])
    df2 = make_df('AB', [3, 4])
    print(df1); print(df2); print(pd.concat([df1, df2]))
df1        df2        pd.concat([df1, df2])
   A   B      A   B      A   B
1  A1  B1    3  A3  B3    1  A1  B1
2  A2  B2    4  A4  B4    2  A2  B2
                                 3  A3  B3
                                 4  A4  B4

По умолчанию конкатенация происходит в объекте DataFrame построчно, то есть axis=0. Аналогично функции np.concatenate() функция pd.concat() позволяет указывать ось, по которой будет выполняться конкатенация. Рассмотрим следующий пример: