---
source_image: page_438.png
page_number: 438
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.94
tokens: 7489
characters: 1413
timestamp: 2025-12-24T02:52:09.935590
finish_reason: stop
---

13.3. Имена, которые давали детям в США за период с 1880 по 2010 год

Анализ тенденций в выборе имен
Имея полный набор данных и первые 1000 записей, мы можем приступить к анализу различных интересных тенденций. Для начала разобьем набор Топ 1000 на части, относящиеся к мальчикам и девочкам.

In [124]: boys = top1000[top1000["sex"] == "M"]

In [125]: girls = top1000[top1000["sex"] == "F"]

Можно нанести на график простые временные ряды, например количество Джонов и Мэри в каждом году, но для этого потребуется предварительное переформатирование. Сформируем сводную таблицу, в которой представлено общее число родившихся по годам и по именам:

In [126]: total_births = top1000.pivot_table("births", index="year",
    ....: columns="name",
    ....: aggfunc=sum)

Теперь можно нанести на график несколько имен, воспользовавшись методом plot объекта DataFrame (результат показан на рис. 13.5):

In [127]: total_births.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 131 entries, 1880 to 2010
Columns: 6868 entries, Aaden to Zuri
dtypes: float64(6868)
memory usage: 6.9 MB

In [128]: subset = total_births[["John", "Harry", "Mary", "Marilyn"]]

In [129]: subset.plot(subplots=True, figsize=(12, 10),
    ....: title="Number of births per year")

Глядя на рисунок, можно сделать вывод, что эти имена в Америке вышли из моды. Но на самом деле картина несколько сложнее, как станет ясно в следующем разделе.