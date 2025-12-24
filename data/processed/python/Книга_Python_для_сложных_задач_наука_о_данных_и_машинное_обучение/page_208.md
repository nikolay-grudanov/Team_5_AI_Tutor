---
source_image: page_208.png
page_number: 208
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.20
tokens: 7500
characters: 1681
timestamp: 2025-12-24T00:56:36.230229
finish_reason: stop
---

Список, массив, объект Series и индекс как ключи группировки. Ключ может быть любым рядом или списком такой же длины, как и у объекта DataFrame. Например:

In[25]: L = [0, 1, 0, 1, 2, 0]
print(df); print(df.groupby(L).sum())

df                df.groupby(L).sum()
key   data1   data2        data1   data2
0     A       0      5      0      7      17
1     B       1      0      1      4      3
2     C       2      3      2      4      7
3     A       3      3
4     B       4      7
5     C       5      9

Разумеется, это значит, что есть еще один, несколько более длинный способ выполнить вышеприведенную операцию df.groupby('key'):

In[26]: print(df); print(df.groupby(df['key']).sum())

df                df.groupby(df['key']).sum()
key   data1   data2        data1   data2
0     A       0      5      A      3      8
1     B       1      0      B      5      7
2     C       2      3      C      7      12
3     A       3      3
4     B       4      7
5     C       5      9

Словарь или объект Series, связывающий индекс и группу. Еще один метод: указать словарь, задающий соответствие значений индекса и ключей группировки:

In[27]: df2 = df.set_index('key')
    mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
    print(df2); print(df2.groupby(mapping).sum())

df2                df2.groupby(mapping).sum()
key   data1   data2        data1   data2
A     0       5      consonant   12   19
B     1       0      vowel      3    8
C     2       3
A     3       3
B     4       7
C     5       9

Любая функция языка Python. Аналогично заданию соответствия можно передать функции groupby любую функцию, принимающую на входе значение индекса и возвращающую группу: