---
source_image: page_365.png
page_number: 365
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.13
tokens: 7330
characters: 1196
timestamp: 2025-12-24T01:00:45.060046
finish_reason: stop
---

1    10.34   1.66    Male    No    Sun    Dinner    3
2    21.01   3.50    Male    No    Sun    Dinner    3
3    23.68   3.31    Male    No    Sun    Dinner    2
4    24.59   3.61    Female  No    Sun    Dinner    4

In[15]: tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']

grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15));

![Пример фасетной гистограммы](../images/fig_4_120.png)

Рис. 4.120. Пример фасетной гистограммы

Графики факторов

Графики факторов тоже подходят для подобных визуализаций. Они позволяют просматривать распределение параметра по интервалам, задаваемым посредством любого другого параметра (рис. 4.121):

In[16]: with sns.axes_style(style='ticks'):
        g = sns.factorplot("day", "total_bill", "sex", data=tips,
                           kind="box")
        g.set_axis_labels("Day", "Total Bill"); # День; Итого

Совместные распределения

Аналогично графикам пар, которые мы рассматривали ранее, мы можем воспользоваться функцией sns.jointplot для отображения совместного распределения между различными наборами данных, а также соответствующих частных распределений (рис. 4.122):