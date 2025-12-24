---
source_image: page_303.png
page_number: 303
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.44
tokens: 7508
characters: 1442
timestamp: 2025-12-24T02:48:23.570551
finish_reason: stop
---

Таблица 9.4. Параметры метода DataFrame.plot

<table>
  <tr>
    <th>Аргумент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>subplots</td>
    <td>Рисовать график каждого столбца DataFrame в отдельном подграфике</td>
  </tr>
  <tr>
    <td>layouts</td>
    <td>2-кортеж (строки, столбцы), определяющий расположение подграфиков</td>
  </tr>
  <tr>
    <td>sharex</td>
    <td>Если subplots=True, то совместно использовать ось X, объединяя риски и границы</td>
  </tr>
  <tr>
    <td>sharey</td>
    <td>Если subplots=True, то совместно использовать ось Y</td>
  </tr>
  <tr>
    <td>legend</td>
    <td>Помещать в подграфик пояснительную надпись (по умолчанию True)</td>
  </tr>
  <tr>
    <td>sort_columns</td>
    <td>Строить графики столбцов в алфавитном порядке; по умолчанию используется существующий порядок столбцов</td>
  </tr>
</table>

О построении графиков временных рядов см. главу 11.

Столбчатые диаграммы
Методы plot.bar() и plot.barh() строят соответственно вертикальную и горизонтальную столбчатые диаграммы. В этом случае индекс Series или DataFrame будет использоваться для нанесения рисок на ось x (bar) или y (barh) (см. рис. 9.15):

In [66]: fig, axes = plt.subplots(2, 1)

In [67]: data = pd.Series(np.random.uniform(size=16), index=list("abcdefghijklmnopqrstuvwxyz"))

In [68]: data.plot.bar(ax=axes[0], color="black", alpha=0.7)
Out[68]: <AxesSubplot:>

In [69]: data.plot.barh(ax=axes[1], color="black", alpha=0.7)