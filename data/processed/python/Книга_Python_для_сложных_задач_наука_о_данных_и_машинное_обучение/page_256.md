---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.74
tokens: 7528
characters: 1594
timestamp: 2025-12-24T00:58:02.206544
finish_reason: stop
---

In[9]: np.allclose(df1 + df2 + df3 + df4,
    pd.eval('df1 + df2 + df3 + df4'))

Out[9]: True

Поддерживаемые функцией pd.eval() операции. На момент выпуска версии 0.16 библиотеки Pandas функция pd.eval() поддерживает широкий спектр операций. Для их демонстрации мы будем использовать следующие целочисленные объекты DataFrame:

In[10]: df1, df2, df3, df4, df5 = (pd.DataFrame(rng.randint(0, 1000, (100, 3))))
        for i in range(5))

Арифметические операторы. Функция pd.eval() поддерживает все арифметические операторы. Например:

In[11]: result1 = -df1 * df2 / (df3 + df4) - df5
    result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
    np.allclose(result1, result2)

Out[11]: True

Операторы сравнения. Функция pd.eval() поддерживает все операторы сравнения, включая выражения, организованные цепочкой:

In[12]: result1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
    result2 = pd.eval('df1 < df2 <= df3 != df4')
    np.allclose(result1, result2)

Out[12]: True

Побитовые операторы. Функция pd.eval() поддерживает побитовые операторы & и |:

In[13]: result1 = (df1 < 0.5) & (df2 < 0.5) | (df3 < df4)
    result2 = pd.eval('(df1 < 0.5) & (df2 < 0.5) | (df3 < df4)')
    np.allclose(result1, result2)

Out[13]: True

Кроме того, она допускает использование литералов and и or в булевых выражениях:

In[14]: result3 = pd.eval('(df1 < 0.5) and (df2 < 0.5) or (df3 < df4)')
    np.allclose(result1, result3)

Out[14]: True

Атрибуты объектов и индексы. Функция pd.eval() поддерживает доступ к атрибутам объектов с помощью синтаксиса obj.attr и к индексам посредством синтаксиса obj[index]: