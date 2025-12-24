---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.86
tokens: 7804
characters: 2255
timestamp: 2025-12-24T02:45:17.598860
finish_reason: stop
---

2    three   9   10   11   12    foo

In [37]: result3.isna()
Out[37]:
    something   a   b   c   d   message
0      False  False  False  False  True
1      False  False  False  False  False
2      False  False  False  False  False

Если в разных столбцах применяются разные маркеры, то их можно задать с помощью словаря:

In [38]: sentinels = {"message": ["foo", "NA"], "something": ["two"]}

In [39]: pd.read_csv("examples/ex5.csv", na_values=sentinels,
.....:                keep_default_na=False)
Out[39]:
    something   a   b   c   d   message
0      one     1   2   3   4   NaN
1      NaN     5   6   8   world
2      three   9   10  11  12   NaN

В табл. 6.2 перечислены некоторые часто используемые аргументы функции pandas.read_csv.

Таблица 6.2. Некоторые аргументы функции read_csv

<table>
  <tr>
    <th>Аргумент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>path</td>
    <td>Строка, обозначающая путь в файловой системе, URL-адрес или похожий на файл объект</td>
  </tr>
  <tr>
    <td>sep или delimiter</td>
    <td>Последовательность символов или регулярное выражение, служащее для разделения полей в строке</td>
  </tr>
  <tr>
    <td>header</td>
    <td>Номер строки, содержащей имена столбцов. По умолчанию равен 0 (первая строка). Если строки-заголовка нет, должен быть равен None</td>
  </tr>
  <tr>
    <td>index_col</td>
    <td>Номера или имена столбцов, трактуемых как индекс строк в результирующем объекте. Может быть задан один номер (имя) или список номеров (имен), определяющий иерархический индекс</td>
  </tr>
  <tr>
    <td>names</td>
    <td>Список имен столбцов результирующего объекта, задается, если header=None</td>
  </tr>
  <tr>
    <td>skiprows</td>
    <td>Количество игнорируемых начальных строк или список номеров игнорируемых строк (нумерация начинается с 0)</td>
  </tr>
  <tr>
    <td>na_values</td>
    <td>Последовательность значений, интерпретируемых как маркеры отсутствия данных</td>
  </tr>
  <tr>
    <td>keep_default_na</td>
    <td>Использовать ли подразумеваемый по умолчанию список маркеров отсутствия значения (по умолчанию True)</td>
  </tr>
  <tr>
    <td>comment</td>
    <td>Один или несколько символов, начинающих комментарий, который продолжается до конца строки</td>
  </tr>
</table>