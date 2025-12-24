---
source_image: page_436.png
page_number: 436
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.98
tokens: 7574
characters: 1243
timestamp: 2025-12-24T02:52:13.359533
finish_reason: stop
---

13.3. Имена, которые давали детям в США за период с 1880 по 2010 год

![Общее количество родившихся по полу и году](../images/13.4.png)

Рис. 13.4. Общее количество родившихся по полу и году

Далее вставим столбец pgor, содержащий долю младенцев, получивших данное имя, относительно общего числа родившихся. Значение pgor, равное 0.02, означает, что данное имя получили 2 из 100 младенцев. Затем сгруппируем данные по году и полу и добавим в каждую группу новый столбец:

def add_pgor(group):
    group["pgor"] = group["births"] / group["births"].sum()
    return group
names = names.groupby(["year", "sex"]).apply(add_pgor)

Получившийся в результате пополненный набор данных состоит из таких столбцов:

In [116]: names
Out[116]:
      name  sex  births  year   pgor
0     Mary   F    7065  1880  0.077643
1     Anna   F    2604  1880  0.028618
2     Emma   F    2003  1880  0.022013
3  Elizabeth   F    1939  1880  0.021309
4    Minnie   F    1746  1880  0.019188
...   ...   ...   ...   ...   ...
1690779 Zymaire   M      5  2010  0.000003
1690780 Zyonne    M      5  2010  0.000003
1690781 Zyquarius   M      5  2010  0.000003
1690782 Zyran     M      5  2010  0.000003
1690783 Zzyzx     M      5  2010  0.000003
[1690784 rows x 5 columns]