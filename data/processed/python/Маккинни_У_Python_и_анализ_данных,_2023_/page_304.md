---
source_image: page_304.png
page_number: 304
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.50
tokens: 7399
characters: 738
timestamp: 2025-12-24T02:48:15.518044
finish_reason: stop
---

Рис. 9.15. Примеры горизонтальной и вертикальной столбчатых диаграмм

В случае DataFrame значения из каждой строки объединяются в группы столбиков, расположенные поодаль друг от друга. См. рис. 9.16.

In [71]: df = pd.DataFrame(np.random.uniform(size=(6, 4)),
    ....: index=["one", "two", "three", "four", "five", "six"],
    ....: columns=pd.Index(["A", "B", "C", "D"], name="Genus"))

In [72]: df
Out[72]:
   Genus      A      B      C      D
one  0.370670  0.602792  0.229159  0.486744
two  0.420082  0.571653  0.049024  0.880592
three  0.814568  0.277160  0.880316  0.431326
four  0.374020  0.899420  0.460304  0.100843
five  0.433270  0.125107  0.494675  0.961825
six  0.601648  0.478576  0.205690  0.560547

In [73]: df.plot.bar()