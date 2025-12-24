---
source_image: page_332.png
page_number: 332
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.59
tokens: 8004
characters: 1795
timestamp: 2025-12-24T02:49:20.248458
finish_reason: stop
---

In [76]: result["tip_pct"]
Out[76]:
    count   mean   max
day smoker
Fri  No      4  0.151650  0.187735
      Yes     15  0.174783  0.263480
Sat  No      45  0.158048  0.291990
      Yes     42  0.147906  0.325733
Sun  No      57  0.160113  0.252672
      Yes     19  0.187250  0.710345
Thur No     45  0.160298  0.266312
      Yes     17  0.163863  0.241255

Как и раньше, можно передавать список кортежей, содержащий желаемые имена:

In [77]: ftuples = [("Average", "mean"), ("Variance", np.var)]

In [78]: grouped[["tip_pct", "total_bill"]].agg(ftuples)
Out[78]:
    tip_pct    total_bill
    Average  Variance  Average  Variance
day smoker
Fri  No      0.151650  0.000791  18.420000  25.596333
      Yes     0.174783  0.002631  16.813333  82.562438
Sat  No      0.158048  0.001581  19.661778  79.908965
      Yes     0.147906  0.003767  21.276667  101.387535
Sun  No      0.160113  0.001793  20.506667  66.099980
      Yes     0.187250  0.023757  24.120000  109.046044
Thur No     0.160298  0.001503  17.113111  59.625081
      Yes     0.163863  0.001551  19.190588  69.808518

Предположим далее, что требуется применить потенциально различные функции к одному или нескольким столбцам. Делается это путем передачи методу agg словаря, который содержит отображение имен столбцов на любой из рассмотренных выше объектов, задающих функции:

In [79]: grouped.agg({"tip" : np.max, "size" : "sum"})
Out[79]:
    tip  size
day smoker
Fri  No   3.50   9
      Yes  4.73  31
Sat  No   9.00  115
      Yes 10.00  104
Sun  No   6.00  167
      Yes  6.50   49
Thur No  6.70  112
      Yes  5.00   40

In [80]: grouped.agg({"tip_pct" : ["min", "max", "mean", "std"], "size" : "sum"})
Out[80]:
    tip_pct    size
    min   max  mean  std sum
day smoker
Fri  No  0.120385  0.187735  0.151650  0.028123   9