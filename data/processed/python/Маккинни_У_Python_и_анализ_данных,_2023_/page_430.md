---
source_image: page_430.png
page_number: 430
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.85
tokens: 7929
characters: 2305
timestamp: 2025-12-24T02:52:24.588759
finish_reason: stop
---

In [91]: sorted_by_diff[::-1].head()
Out[91]:
gender      F      M    diff
title
Good, The Bad and The Ugly, The (1966)   3.494949   4.221300   0.726351
Kentucky Fried Movie, The (1977)          2.878788   3.555147   0.676359
Dumb & Dumber (1994)                      2.697987   3.336595   0.638608
Longest Day, The (1962)                    3.411765   4.031447   0.619682
Cable Guy, The (1996)                     2.250000   2.863787   0.613787

А теперь допустим, что нас интересуют фильмы, вызвавшие наибольшее разногласие у зрителей независимо от пола. Разногласие можно изменить с помощью дисперсии или стандартного отклонения оценок. Чтобы найти его, сначала вычислим стандартное отклонение оценок, сгруппированных по названию, а потом оставим только активные названия:

In [92]: rating_std_by_title = data.groupby("title")[["rating"]].std()

In [93]: rating_std_by_title = rating_std_by_title.loc[active_titles]

In [94]: rating_std_by_title.head()
Out[94]:
title
'burbs, The (1989)                1.107760
10 Things I Hate About You (1999) 0.989815
101 Dalmatians (1961)              0.982103
101 Dalmatians (1996)              1.098717
12 Angry Men (1957)                0.812731
Name: rating, dtype: float64

Затем отсортируем в порядке убывания и отберем первые 10 строк, это и будут десять фильмов (в первом приближении) с наиболее сильно различающимися оценками:

In [95]: rating_std_by_title.sort_values(ascending=False)[:10]
Out[95]:
title
Dumb & Dumber (1994)               1.321333
Blair Witch Project, The (1999)    1.316368
Natural Born Killers (1994)        1.307198
Tank Girl (1995)                   1.277695
Rocky Horror Picture Show, The (1975) 1.260177
Eyes Wide Shut (1999)              1.259624
Evita (1996)                       1.253631
Billy Madison (1995)               1.249970
Fear and Loathing in Las Vegas (1998) 1.246408
Bicentennial Man (1999)             1.245533
Name: rating, dtype: float64

Вы, наверное, обратили внимание, что жанры фильма разделяются вертикальной чертой (|), поскольку один фильм может относиться к нескольким жанрам. Чтобы сгруппировать оценки по жанрам, мы можем воспользоваться методом explode объекта DataFrame. Посмотрим, как он работает. Сначала преобразуем строку жанров в список жанров, воспользовавшись методом str.split объекта Series.