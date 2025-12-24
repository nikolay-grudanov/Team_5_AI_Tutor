---
source_image: page_429.png
page_number: 429
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.48
tokens: 8004
characters: 2046
timestamp: 2025-12-24T02:52:30.125256
finish_reason: stop
---

gender F M
title
'burbs, The (1989)    2.793478  2.962085
10 Things I Hate About You (1999)  3.646552  3.311966
101 Dalmatians (1961)   3.791444  3.500000
101 Dalmatians (1996)   3.240000  2.911215
12 Angry Men (1957)     4.184397  4.328421
...
Young Guns (1988)      3.371795  3.425620
Young Guns II (1990)   2.934783  2.904025
Young Sherlock Holmes (1985)  3.514706  3.363344
Zero Effect (1998)     3.864407  3.723140
eXistenZ (1999)        3.098592  3.289086
[1216 rows x 2 columns]

Чтобы найти фильмы, оказавшиеся на первом месте у зрителей-женщин, мы можем отсортировать результат по столбцу F в порядке убывания:

In [86]: top_female_ratings = mean_ratings.sort_values("F", ascending=False)

In [87]: top_female_ratings.head()
Out[87]:
gender                F         M
title
Close Shave, A (1995)  4.644444  4.473795
Wrong Trousers, The (1993)  4.588235  4.478261
Sunset Blvd. (a.k.a. Sunset Boulevard) (1950)  4.572650  4.464589
Wallace & Gromit: The Best of Aardman Animation (1996)  4.563107  4.385075
Schindler's List (1993)  4.562602  4.491415

Измерение несогласия в оценках
Допустим, мы хотим найти фильмы, по которым мужчины и женщины сильнее всего разошлись в оценках. Для этого можно добавить столбец mean_ratings, содержащий разность средних, а затем отсортировать по нему:

In [88]: mean_ratings["diff"] = mean_ratings["M"] - mean_ratings["F"]

Сортировка по столбцу 'diff' дает фильмы с наибольшей разностью оценок, которые больше нравятся женщинам:

In [89]: sorted_by_diff = mean_ratings.sort_values("diff")

In [90]: sorted_by_diff.head()
Out[90]:
gender                F         M         diff
title
Dirty Dancing (1987)  3.790378  2.959596  -0.830782
Jumpin' Jack Flash (1986)  3.254717  2.578358  -0.676359
Grease (1978)        3.975265  3.367041  -0.608224
Little Women (1994)   3.870588  3.321739  -0.548849
Steel Magnolias (1989)  3.901734  3.365957  -0.535777

Изменив порядок строк на противоположный и снова отобрав первые 10 строк, мы получим фильмы, которым мужчины поставили высокие, а женщины — низкие оценки: