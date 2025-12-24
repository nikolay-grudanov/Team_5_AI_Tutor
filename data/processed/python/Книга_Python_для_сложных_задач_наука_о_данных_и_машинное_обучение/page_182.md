---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.39
tokens: 7588
characters: 2174
timestamp: 2025-12-24T00:56:07.925819
finish_reason: stop
---

In[10]: try:
        pd.concat([x, y], verify_integrity=True)
    except ValueError as e:
        print("ValueError:", e)

ValueError: Indexes have overlapping values: [0, 1]

Игнорирование индекса. Иногда индекс сам по себе не имеет значения и лучше его просто проигнорировать. Для этого достаточно установить флаг ignore_index. В случае равного True значения этого флага конкатенация приведет к созданию нового целочисленного индекса для итогового объекта Series:

In[11]: print(x); print(y); print(pd.concat([x, y], ignore_index=True))

    x                y                pd.concat([x, y], ignore_index=True)
      A   B           A   B           A   B
    0  A0  B0         0  A2  B2       0  A0  B0
    1  A1  B1         1  A3  B3       1  A1  B1
                        2  A2  B2
                        3  A3  B3

Добывление ключей мультииндекса. Еще один вариант — воспользоваться параметром keys для задания меток для источников данных. Результатом будут иерархически индексированные ряды, содержащие данные:

In[12]: print(x); print(y); print(pd.concat([x, y], keys=['x', 'y']))

    x                y                pd.concat([x, y], keys=['x', 'y'])
      A   B           A   B           A   B
    0  A0  B0         0  A2  B2       x  0  A0  B0
    1  A1  B1         1  A3  B3       1  A1  B1
                                    y  0  A2  B2
                                    1  A3  B3

Результат представляет собой мультииндексированный объект DataFrame, так что мы сможем воспользоваться описанным в разделе «Иерархическая индексация» этой главы, чтобы преобразовать эти данные в требуемое нам представление.

Конкатенация с использованием соединений

В рассматриваемых примерах в основном производится конкатенация объектов DataFrame с общими названиями столбцов. На практике у данных из разных источников могут быть различные наборы имен столбцов. На этот случай у функции pd.concat() имеется несколько опций. Изучим объединение следующих двух объектов DataFrame, у которых столбцы (но не все!) называются одинаково:

In[13]: df5 = make_df('ABC', [1, 2])
        df6 = make_df('BCD', [3, 4])
        print(df5); print(df6); print(pd.concat([df5, df6]))