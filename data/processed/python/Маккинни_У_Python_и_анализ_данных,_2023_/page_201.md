---
source_image: page_201.png
page_number: 201
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.86
tokens: 7758
characters: 2429
timestamp: 2025-12-24T02:45:31.925859
finish_reason: stop
---

In [79]: data.to_json(sys.stdout, orient="records")
[{"a":1,"b":2,"c":3},{"a":4,"b":5,"c":6},{"a":7,"b":8,"c":9}]

XML и HTML: разбор веб-страниц
На Python написано много библиотек для чтения и записи данных в вездесущих форматах HTML и XML. В частности, библиотеки lxml, Beautiful Soup и html5lib. Хотя lxml в общем случае работает гораздо быстрее остальных, другие библиотеки лучше справляются с неправильно сформированными HTML- и XML-файлами.

В pandas имеется функция pandas.read_html, которая использует все вышеупомянутые библиотеки автоматического выделения таблиц из HTML-файлов и представления их в виде объектов DataFrame. Чтобы продемонстрировать, как это работает, я скачал из Федеральной корпорации страхования вкладов США HTML-файл (он упоминается в документации по pandas) со сведениями о банкротствах банков⁴. Сначала необходимо установить дополнительные библиотеки, необходимые функции read_html:

conda install lxml beautifulsoup4 html5lib

Если вы не пользуетесь conda, то можно с тем же успехом выполнить команду pip install lxml.

У функции pandas.read_html имеется много параметров, но по умолчанию она ищет и пытается разобрать все табличные данные внутри тегов <table>. Результатом является список объектов DataFrame:

In [80]: tables = pd.read_html("examples/fdic_failed_bank_list.html")

In [81]: len(tables)
Out[81]: 1

In [82]: failures = tables[0]

In [83]: failures.head()
Out[83]:
      Bank Name                City   ST CERT \
0    Allied Bank           Mulberry   AR   91
1 The Woodbury Banking Company  Woodbury   GA 11297
2 First CornerStone Bank     King of Prussia   PA 35312
3 Trust Company Bank         Memphis   TN   9956
4 North Milwaukee State Bank Milwaukee   WI 20364

      Acquiring Institution        Closing Date    Updated Date
0           Today's Bank  September 23, 2016  November 17, 2016
1           United Bank       August 19, 2016  November 17, 2016
2 First-Citizens Bank & Trust Company  May 6, 2016  September 6, 2016
3 The Bank of Fayette County  April 29, 2016  September 6, 2016
4 First-Citizens Bank & Trust Company  March 11, 2016  June 16, 2016

Поскольку в объекте failures много столбцов, pandas вставляет знак разрыва строки \.

Как будет показано в следующих главах, дальше мы можем произвести очистку и анализ данных, например посчитать количество банкротств по годам:

⁴ Полный список см. по адресу https://www.fdic.gov/bank/individual/failed/banklist.html.