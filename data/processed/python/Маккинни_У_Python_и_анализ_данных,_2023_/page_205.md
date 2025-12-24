---
source_image: page_205.png
page_number: 205
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.66
tokens: 7662
characters: 2110
timestamp: 2025-12-24T02:45:35.914041
finish_reason: stop
---

In [95]: frame = pd.read_csv("examples/ex1.csv")

In [96]: frame
Out[96]:
   a   b   c   d   message
0   1   2   3   4   hello
1   5   6   7   8   world
2   9  10  11  12   foo

In [97]: frame.to_pickle("examples/frame_pickle")

Вообще говоря, pickle-файлы можно прочитать только из Python-программы. Любой объект в этом формате можно прочитать с помощью встроенной функции pickle или — еще удобнее — с помощью функции pandas.read_pickle:

In [98]: pd.read_pickle("examples/frame_pickle")
Out[98]:
   a   b   c   d   message
0   1   2   3   4   hello
1   5   6   7   8   world
2   9  10  11  12   foo

pickle рекомендуется использовать только для краткосрочного хранения. Проблема в том, что невозможно гарантировать неизменность формата: сегодня вы сериализовали объект в формате pickle, а следующая версия библиотеки не сможет его десериализовать. При разработке pandas были приложены все усилия к тому, чтобы такого не случалось, но, возможно, наступит момент, когда придется «поломать» формат pickle.

В pandas встроена поддержка еще нескольких открытых двоичных форматов, в т. ч. HDF5, ORC и Apache Parquet. Например, если установить пакет pyarrow (conda install pyarrow), то можно будет читать файлы в формате Parquet с помощью функции pandas.read_parquet:

In [100]: fec = pd.read_parquet('datasets/fec/fec.parquet')

Ниже я приведу несколько примеров работы с HDF5, но призываю вас самостоятельно исследовать другие форматы, чтобы оценить их эффективность и пригодность для анализа в вашей задаче.

Чтение файлов Microsoft Excel
В pandas имеется также поддержка для чтения табличных данных в формате Excel 2003 (и более поздних версий) с помощью класса pandas.ExcelFile или функции pandas.read_excel. На внутреннем уровне ExcelFile пользуется пакетами xlrd и openpyxl для чтения файлов в формате XLS и XLSX соответственно. Эти пакеты нужно устанавливать отдельно от pandas командой pip или conda:

conda install openpyxl xlrd

Для работы с классом pandas.ExcelFile создайте его экземпляр, передав конструктору путь к файлу с расширением xls или xlsx:

In [101]: xlsx = pd.ExcelFile("examples/ex1.xlsx")