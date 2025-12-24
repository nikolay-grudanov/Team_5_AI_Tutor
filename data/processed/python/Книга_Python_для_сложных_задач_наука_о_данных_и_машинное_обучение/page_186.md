---
source_image: page_186.png
page_number: 186
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.55
tokens: 7717
characters: 2411
timestamp: 2025-12-24T00:56:16.782215
finish_reason: stop
---

186 Глава 3 • Манипуляции над данными с помощью пакета Pandas

<table>
  <tr>
    <th>1</th>
    <th>Jake</th>
    <th>Engineering</th>
    <th>2012</th>
  </tr>
  <tr>
    <th>2</th>
    <th>Lisa</th>
    <th>Engineering</th>
    <th>2004</th>
  </tr>
  <tr>
    <th>3</th>
    <th>Sue</th>
    <th>HR</th>
    <th>2014</th>
  </tr>
</table>

Функция pd.merge() распознает, что в обоих объектах DataFrame имеется столбец employee, и автоматически выполняет соединение, используя этот столбец в качестве ключа. Результатом слияния становится новый объект DataFrame, объединяющий информацию из двух входных объектов. Обратите внимание, что порядок записей в столбцах не обязательно сохраняется: в данном случае сортировка столбца employee различна в объектах df1 и df2 и функция pd.merge() обрабатывает эту ситуацию корректным образом. Кроме того, не забывайте, что слияние игнорирует индекс, за исключением особого случая слияния по индексу (см. пункт «Ключевые слова left_index и right_index» подраздела «Задание ключа слияния» данного раздела).

Соединения «многие-к-одному»

«Многие-к-одному» — соединения, при которых один из двух ключевых столбцов содержит дублирующиеся значения. В случае соединения «многие-к-одному» в итоговом объекте DataFrame эти дублирующиеся записи будут сохранены. Рассмотрим следующий пример соединения «многие-к-одному»:

In[4]: df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                           'supervisor': ['Carly', 'Guido', 'Steve']})
print(df3); print(df4); print(pd.merge(df3, df4))

df3
  employee   group  hire_date
0   Bob      Accounting     2008
1   Jake     Engineering    2012
2   Lisa     Engineering    2004
3   Sue      HR             2014

df4
  group supervisor
0  Accounting   Carly
1  Engineering Guido
2    HR         Steve

pd.merge(df3, df4)
  employee   group  hire_date supervisor
0   Bob      Accounting     2008   Carly
1   Jake     Engineering    2012   Guido
2   Lisa     Engineering    2004   Guido
3   Sue      HR             2014   Steve

В итоговом объекте DataFrame имеется дополнительный столбец с информацией о руководителе (supervisor) с повторением информации в одном или нескольких местах в соответствии с вводимыми данными.

Соединения «многие-ко-многим»

Соединения «многие-ко-многим» семантически несколько более сложны, но тем не менее четко определены. Если столбец ключа как в левом, так и в правом массивах