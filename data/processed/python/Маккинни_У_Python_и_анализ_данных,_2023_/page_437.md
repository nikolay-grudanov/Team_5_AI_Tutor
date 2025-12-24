---
source_image: page_437.png
page_number: 437
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.76
tokens: 7775
characters: 1716
timestamp: 2025-12-24T02:52:24.155053
finish_reason: stop
---

При выполнении такой операции группировки часто бывает полезно произвести проверку разумности результата, например удостовериться, что сумма значений в столбце pgor по всем группам равна 1.

In [117]: names.groupby(["year", "sex"])["pgor"].sum()
Out[117]:
year   sex
1880    F    1.0
        M    1.0
1881    F    1.0
        M    1.0
1882    F    1.0
        ...
2008    M    1.0
2009    F    1.0
        M    1.0
2010    F    1.0
        M    1.0
Name: pgor, Length: 262, dtype: float64

Далее я извлеку подмножество данных, чтобы упростить последующий анализ: первые 1000 имен для каждой комбинации пола и года. Это еще одна групповая операция:

In [118]: def get_top1000(group):
    ....:     return group.sort_values("births", ascending=False)[:1000]

In [119]: grouped = names.groupby(["year", "sex"])

In [120]: top1000 = grouped.apply(get_top1000)

In [121]: top1000.head()
Out[121]:
      name  sex  births  year  pgor
year sex
1880 F  0    Mary    F    7065  1880  0.077643
      1    Anna    F    2604  1880  0.028618
      2    Emma    F    2003  1880  0.022013
      3  Elizabeth  F    1939  1880  0.021309
      4    Minnie  F    1746  1880  0.019188

Групповой индекс мы можем удалить, т. к. он больше не понадобится для анализа:

In [122]: top1000 = top1000.reset_index(drop=True)
Теперь результирующий набор стал заметно меньше:
In [123]: top1000.head()
Out[123]:
      name  sex  births  year  pgor
0    Mary  F    7065  1880  0.077643
1    Anna  F    2604  1880  0.028618
2    Emma  F    2003  1880  0.022013
3  Elizabeth  F    1939  1880  0.021309
4    Minnie  F    1746  1880  0.019188

Это набор, содержащий первые 1000 записей, мы и будем использовать его для исследования данных в дальнейшем.