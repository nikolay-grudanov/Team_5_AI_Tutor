---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.60
tokens: 7989
characters: 1821
timestamp: 2025-12-24T02:45:25.804900
finish_reason: stop
---

Теперь имеем:

In [41]: result = pd.read_csv("examples/ex6.csv")

In [42]: result
Out[42]:
    one   two   three   four   key
0   0.467976 -0.038649 -0.295344 -1.824726 L
1  -0.358893  1.404453  0.704965 -0.200638 B
2  -0.501840  0.659254 -0.421691 -0.057688 G
3   0.204886  1.074134  1.388361 -0.982404 R
4   0.354628 -0.133116  0.283763 -0.837063 Q
...
9995  2.311896 -0.417070 -1.409599 -0.515821 L
9996 -0.479893 -0.650419  0.745152 -0.646038 E
9997  0.523331  0.787112  0.486066  1.093156 K
9998 -0.362559  0.598894 -1.843201  0.887292 G
9999 -0.096376 -1.012999 -0.657431 -0.573315 Θ
[10000 rows x 5 columns]

Многоточие ... означает, что строки в середине DataFrame опущены.
Чтобы прочитать только небольшое число строк (а не весь файл), нужно задать это число в параметре nrows:

In [43]: pd.read_csv("examples/ex6.csv", nrows=5)
Out[43]:
    one   two   three   four   key
0   0.467976 -0.038649 -0.295344 -1.824726 L
1  -0.358893  1.404453  0.704965 -0.200638 B
2  -0.501840  0.659254 -0.421691 -0.057688 G
3   0.204886  1.074134  1.388361 -0.982404 R
4   0.354628 -0.133116  0.283763 -0.837063 Q

Для чтения файла порциями задайте с помощью параметра chunksize размер порции в строках:

In [44]: chunker = pd.read_csv("examples/ex6.csv", chunksize=1000)

In [45]: type(chunker)
Out[45]: pandas.io.parsers.TextFileReader

Объект TextParser, возвращаемый функцией pandas.read_csv, позволяет читать файл порциями размера chunksize. Например, можно таким образом итеративно читать файл ex6.csv, агрегируя счетчики значений в столбце "key":

chunker = pd.read_csv("examples/ex6.csv", chunksize=1000)

tot = pd.Series([], dtype='int64')
for piece in chunker:
    tot = tot.add(piece["key"].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)

Имеем:

In [47]: tot[:10]
Out[47]:
E    368.0
X    364.0