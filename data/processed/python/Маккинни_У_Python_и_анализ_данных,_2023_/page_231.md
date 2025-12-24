---
source_image: page_231.png
page_number: 231
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.01
tokens: 7741
characters: 2309
timestamp: 2025-12-24T02:46:23.875465
finish_reason: stop
---

In [121]: mnames = ["movie_id", "title", "genres"]

In [122]: movies = pd.read_table("datasets/movielens/movies.dat", sep="::",
    ....:                 header=None, names=mnames, engine="python")

In [123]: movies[:10]
Out[123]:
   movie_id        title                        genres
0         1  Toy Story (1995)  Animation|Children's|Comedy
1         2      Jumanji (1995)  Adventure|Children's|Fantasy
2         3  Grumpier Old Men (1995)  Comedy|Romance
3         4  Waiting to Exhale (1995)  Comedy|Drama
4         5  Father of the Bride Part II (1995)  Comedy
5         6           Heat (1995)  Action|Crime|Thriller
6         7          Sabrina (1995)  Comedy|Romance
7         8  Tom and Huck (1995)  Adventure|Children's
8         9  Sudden Death (1995)  Action
9        10     GoldenEye (1995)  Action|Adventure|Thriller

В pandas реализован специальный метод объекта Series str.get_dummies (методы, имена которых начинаются со str., подробнее обсуждаются в разделе 7.4 ниже) для обработки ситуации, когда принадлежность нескольким группам закодирована строкой с разделителями:

In [124]: dummies = movies["genres"].str.get_dummies("|")

In [125]: dummies.iloc[:10, :6]
Out[125]:
   Action  Adventure  Animation  Children's  Comedy  Crime
0       0          0           0            1       1      0
1       0          1           0            0       1      0
2       0          0           0            0       1      0
3       0          0           0            0       1      0
4       0          0           0            0       1      0
5       1          0           0            0       0      1
6       0          0           0            0       1      0
7       0          1           0            0       0      0
8       1          0           0            0       0      0
9       1          1           0            0       0      0

Затем, как и раньше, можно объединить этот результат с movies, добавив "Genre_" к именам столбцов в объекте DataFrame dummies с помощью метода add_prefix:

In [126]: movies_windic = movies.join(dummies.add_prefix("Genre_"))

In [127]: movies_windic.iloc[0]
Out[127]:
movie_id    1
title      Toy Story (1995)
genres     Animation|Children's|Comedy
Genre_Action    0
Genre_Adventure    0
Genre_Animation    1
Genre_Children's    1
Genre_Comedy    1