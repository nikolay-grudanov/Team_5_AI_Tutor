---
source_image: page_212.png
page_number: 212
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.20
tokens: 7457
characters: 1491
timestamp: 2025-12-24T02:45:36.849098
finish_reason: stop
---

In [147]: cursor.description
Out[147]:
(('a', None, None, None, None, None),
 ('b', None, None, None, None, None),
 ('c', None, None, None, None, None),
 ('d', None, None, None, None, None))

In [148]: pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
Out[148]:
    a      b      c   d
0  Atlanta  Georgia  1.25  6
1  Tallahassee  Florida  2.60  3
2  Sacramento  California  1.70  5

Такое переформатирование не хочется выполнять при каждом запросе к базе данных. Проект SQLAlchemy (www.sqlalchemy.org) — популярная библиотека на Python, абстрагирующая многие различия между базами данных SQL. В pandas имеется функция read_sql, которая позволяет без труда читать данные из соединения, открытого SQLAlchemy. Для установки SQLAlchemy выполните команду

conda install sqlalchemy

Далее подключимся к той же самой базе SQLite с помощью SQLAlchemy и прочитаем данные из ранее созданной таблицы:

In [149]: import sqlalchemy as sqla

In [150]: db = sqla.create_engine("sqlite:///mydata.sqlite")

In [151]: pd.read_sql("SELECT * FROM test", db)
Out[151]:
    a      b      c   d
0  Atlanta  Georgia  1.25  6
1  Tallahassee  Florida  2.60  3
2  Sacramento  California  1.70  5

6.5. Заключение

Получение доступа к данным часто является первым шагом процесса анализа данных. В этой главе мы рассмотрели ряд полезных средств, позволяющих приступить к делу. В следующих главах мы более детально рассмотрим переформатирование данных, визуализацию, анализ временных рядов и другие вопросы.