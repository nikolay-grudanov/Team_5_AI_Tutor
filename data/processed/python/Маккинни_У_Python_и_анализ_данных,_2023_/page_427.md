---
source_image: page_427.png
page_number: 427
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.80
tokens: 7988
characters: 2222
timestamp: 2025-12-24T02:52:24.261436
finish_reason: stop
---

пола и возраста. Как мы увидим, это гораздо легче сделать, если предварительно объединить все данные в одну таблицу. Применяя функцию merge из библиотеки pandas, мы сначала объединим ratings с users, а затем результат объединим с movies. Pandas определяет, по каким столбцам объединять (или соединять), ориентируясь на совпадение имен:

In [74]: data = pd.merge(pd.merge(ratings, users), movies)

In [75]: data
Out[75]:
    user_id  movie_id  rating  timestamp gender  age occupation  zip \
0           1       1193      5   978300760     F     1         10  48067
1           2       1193      5   978298413     M    56        16  70072
2          12       1193      4   978220179     M    25        12  32793
3          15       1193      4   978199279     M    25         7  22903
4          17       1193      5   978158471     M    50         1  95350
...        ...       ...     ...         ...   ...   ...         ...   ...
1000204    5949     2198      5   958846401     M    18        17  47901
1000205    5675     2703      3   976029116     M    35        14  30030
1000206    5780     2845      1   958153068     M    18        17  92886
1000207    5851     3607      5   957756608     F    18        20  55410
1000208    5938     2909      4   957273353     M    25         1  35401

title                genres
0  One Flew Over the Cuckoo's Nest (1975)  Drama
1  One Flew Over the Cuckoo's Nest (1975)  Drama
2  One Flew Over the Cuckoo's Nest (1975)  Drama
3  One Flew Over the Cuckoo's Nest (1975)  Drama
4  One Flew Over the Cuckoo's Nest (1975)  Drama
...                        ...
1000204  Modulations (1998)  Documentary
1000205  Broken Vessels (1998)  Drama
1000206  White Boys (1999)  Drama
1000207  One Little Indian (1973)  Comedy|Drama|Western
1000208  Five Wives, Three Secretaries and Me (1998)  Documentary
[1000209 rows x 10 columns]

In [76]: data.iloc[0]
Out[76]:
user_id    1
movie_id   1193
rating     5
timestamp  978300760
gender     F
age        1
occupation 10
zip        48067
title      One Flew Over the Cuckoo's Nest (1975)
genres     Drama
Name: 0, dtype: object

Чтобы получить средние рейтинги каждого фильма по группам зрителей одного пола, воспользуемся методом pivot_table: