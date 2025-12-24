---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.36
tokens: 7594
characters: 1724
timestamp: 2025-12-24T02:45:31.547927
finish_reason: stop
---

Этот объект может показать список рабочих листов в файле:

In [102]: xlsx.sheet_names
Out[102]: ['Sheet1']

Прочитать данные из рабочего листа в объект DataFrame позволяет метод parse:

In [103]: xlsx.parse(sheet_name="Sheet1")
Out[103]:
    Unnamed: 0   a   b   c   d message
0           0   1   2   3   4 hello
1           1   5   6   7   8 world
2           2   9  10  11  12 foo

В этой таблице Excel имеется индексный столбец, поэтому мы можем указать его в аргументе index_col:

In [104]: xlsx.parse(sheet_name="Sheet1", index_col=0)
Out[104]:
     a   b   c   d message
0   1   2   3   4 hello
1   5   6   7   8 world
2   9  10  11  12 foo

Если вы собираетесь читать несколько рабочих листов из файла, то быстрее создать объект pandas.ExcelFile, но можно просто передать имя файла функции pandas.read_excel:

In [105]: frame = pd.read_excel("examples/ex1.xlsx", sheet_name="Sheet1")

In [106]: frame
Out[106]:
    Unnamed: 0   a   b   c   d message
0           0   1   2   3   4 hello
1           1   5   6   7   8 world
2           2   9  10  11  12 foo

Для записи данных pandas в файл формата Excel следует сначала создать объект ExcelWriter, а затем записать в него данные, пользуясь методом to_excel объектов pandas:

In [107]: writer = pd.ExcelWriter("examples/ex2.xlsx")

In [108]: frame.to_excel(writer, "Sheet1")

In [109]: writer.save()

Можно вместо этого передать методу to_excel путь к файлу, избежав тем самым создания ExcelWriter:

In [110]: frame.to_excel("examples/ex2.xlsx")

Формат HDF5
HDF5 — хорошо зарекомендовавший себя файловый формат для хранения больших объемов научных данных в виде массивов. Для работы с ним используется библиотека, написанная на С и имеющая интерфейсы ко многим языкам,