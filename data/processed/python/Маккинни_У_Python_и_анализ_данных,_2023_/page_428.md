---
source_image: page_428.png
page_number: 428
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.12
tokens: 7809
characters: 2124
timestamp: 2025-12-24T02:52:13.795965
finish_reason: stop
---

In [77]: mean_ratings = data.pivot_table("rating", index="title",
.....:                                 columns="gender", aggfunc="mean")

In [78]: mean_ratings.head(5)
Out[78]:
gender      F      M
title
$1,000,000 Duck (1971)   3.375000   2.761905
'Night Mother (1986)     3.388889   3.352941
'Til There Was You (1997) 2.675676   2.733333
'burbs, The (1989)       2.793478   2.962085
...And Justice for All (1979) 3.828571   3.689024

В результате получается еще один объект DataFrame, содержащий средние рейтинги, в котором метками строк («индексом») являются названия фильмов, а метками столбцов — обозначения полов. Сначала я оставлю только фильмы, получившие не менее 250 оценок (число выбрано совершенно произвольно); для этого сгруппирую данные по названию и с помощью метода size() получу объект Series, содержащий размеры групп для каждого наименования:

In [79]: ratings_by_title = data.groupby("title").size()

In [80]: ratings_by_title.head()
Out[80]:
title
$1,000,000 Duck (1971)    37
'Night Mother (1986)       70
'Til There Was You (1997)  52
'burbs, The (1989)        303
...And Justice for All (1979) 199
dtype: int64

In [81]: active_titles = ratings_by_title.index[ratings_by_title >= 250]

In [82]: active_titles
Out[82]:
Index([''burbs, The (1989)', '10 Things I Hate About You (1999)',
       '101 Dalmatians (1961)', '101 Dalmatians (1996)', '12 Angry Men (1957)',
       '13th Warrior, The (1999)', '2 Days in the Valley (1996)',
       '20,000 Leagues Under the Sea (1954)', '2001: A Space Odyssey (1968)',
       '2010 (1984)',
       ...
       'X-Men (2000)', 'Year of Living Dangerously (1982)',
       'Yellow Submarine (1968)', 'You've Got Mail (1998)',
       'Young Frankenstein (1974)', 'Young Guns (1988)',
       'Young Guns II (1990)', 'Young Sherlock Holmes (1985)',
       'Zero Effect (1998)', 'eXistenZ (1999)'],
      dtype='object', name='title', length=1216)

Затем для отбора строк из приведенного выше объекта mean_ratings воспользуемся индексом фильмов, получивших не менее 250 оценок:

In [83]: mean_ratings = mean_ratings.loc[active_titles]

In [84]: mean_ratings
Out[84]: