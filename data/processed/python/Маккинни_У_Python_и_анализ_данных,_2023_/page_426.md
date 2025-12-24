---
source_image: page_426.png
page_number: 426
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.61
tokens: 7917
characters: 2102
timestamp: 2025-12-24T02:52:19.840233
finish_reason: stop
---

ratings = pd.read_table("datasets/movielens/ratings.dat", sep="::",
    header=None, names=rnames, engine="python")
mnames = ["movie_id", "title", "genres"]
movies = pd.read_table("datasets/movielens/movies.dat", sep="::",
header=None, names=mnames, engine="python")

Проверить, что все получилось, можно, взглянув на каждый объект DataFrame:

In [70]: users.head(5)
Out[70]:
   user_id gender age occupation zip
0        1      F   1           10  48067
1        2      M  56           16  70072
2        3      M  25           15  55117
3        4      M  45            7  02460
4        5      M  25           20  55455

In [71]: ratings.head(5)
Out[71]:
   user_id  movie_id  rating  timestamp
0        1       1193      5  978300760
1        1        661      3  978302109
2        1        914      3  978301968
3        1       3408      4  978300275
4        1       2355      5  978824291

In [72]: movies.head(5)
Out[72]:
   movie_id                title                        genres
0        1     Toy Story (1995)  Animation|Children's|Comedy
1        2         Jumanji (1995)  Adventure|Children's|Fantasy
2        3  Grumpier Old Men (1995)  Comedy|Romance
3        4  Waiting to Exhale (1995)  Comedy|Drama
4        5  Father of the Bride Part II (1995)  Comedy

In [73]: ratings
Out[73]:
   user_id  movie_id  rating  timestamp
0        1       1193      5  978300760
1        1        661      3  978302109
2        1        914      3  978301968
3        1       3408      4  978300275
4        1       2355      5  978824291
...      ...      ...      ...      ...
1000204  6040      1091      1  956716541
1000205  6040      1094      5  956704887
1000206  6040       562      5  956704746
1000207  6040      1096      4  956715648
1000208  6040      1097      4  956715569
[1000209 rows x 4 columns]

Отметим, что возраст и род занятий кодируются целыми числами, а расшифровка приведена в прилагаемом к набору данных файлу README. Анализ данных, хранящихся в трех таблицах, — непростая задача. Пусть, например, требуется вычислить средние рейтинги для конкретного фильма в разрезе