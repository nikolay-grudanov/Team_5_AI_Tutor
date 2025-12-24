---
source_image: page_367.png
page_number: 367
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.71
tokens: 7318
characters: 996
timestamp: 2025-12-24T01:00:45.462449
finish_reason: stop
---

Рис. 4.123. График совместного распределения с подбором регрессии

Столбчатые диаграммы

Графики временных рядов можно строить с помощью функции sns.factorplot. В следующем примере, показанном на рис. 4.124, мы воспользуемся данными из набора Planets («Планеты»), которые мы уже видели в разделе «Агрегирование и группировка» главы 2:

In[19]: planets = sns.load_dataset('planets')
    planets.head()

Out[19]:
      method  number  orbital_period   mass  distance  year
0  Radial Velocity      1         269.300   7.10      77.40  2006
1  Radial Velocity      1        874.774   2.21      56.95  2008
2  Radial Velocity      1        763.000   2.60      19.84  2011
3  Radial Velocity      1       326.030  19.40     110.62  2007
4  Radial Velocity      1       516.220  10.50     119.47  2009

In[20]: with sns.axes_style('white'):
    g = sns.factorplot("year", data=planets, aspect=2,  # Год
                        kind="count", color='steelblue')  # Количество
    g.set_xticklabels(step=5)