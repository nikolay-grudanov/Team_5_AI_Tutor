---
source_image: page_432.png
page_number: 432
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.35
tokens: 7908
characters: 1497
timestamp: 2025-12-24T02:52:24.230028
finish_reason: stop
---

Теперь можно объединить все три таблицы и сгруппировать по жанру:

In [102]: ratings_with_genre = pd.merge(pd.merge(movies_exploded, ratings), users)

In [103]: ratings_with_genre.iloc[0]
Out[103]:
movie_id    1
title       Toy Story (1995)
genre       Animation
user_id     1
rating      5
timestamp   978824268
gender      F
age         1
occupation  10
zip         48067
Name: 0, dtype: object

In [104]: genre_ratings = (ratings_with_genre.groupby(["genre", "age"])
.....:        ["rating"].mean()
.....:        .unstack("age"))

In [105]: genre_ratings[:10]
Out[105]:
                1    18    25    35    45    50
genre
Action      3.506385 3.447097 3.453358 3.538107 3.528543 3.611333
Adventure   3.449975 3.408525 3.443163 3.515291 3.528963 3.628163
Animation   3.476113 3.624014 3.701228 3.740545 3.734856 3.780020
Children's  3.241642 3.294257 3.426873 3.518423 3.527593 3.556555
Comedy      3.497491 3.460417 3.490385 3.561984 3.591789 3.646868
Crime       3.710170 3.668054 3.680321 3.733736 3.750661 3.810688
Documentary 3.730769 3.865865 3.946690 3.953747 3.966521 3.908108
Drama       3.794735 3.721930 3.726428 3.782512 3.784356 3.878415
Fantasy     3.317647 3.353778 3.452484 3.482301 3.532468 3.581570
Film-Noir   4.145455 3.997368 4.058725 4.064910 4.105376 4.175401

age      56
genre
Action   3.610709
Adventure 3.649064
Animation 3.756233
Children's 3.621822
Comedy    3.650949
Crime     3.832549
Documentary 3.961538
Drama     3.933465
Fantasy   3.532700
Film-Noir 4.125932