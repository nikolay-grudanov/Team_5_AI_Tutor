---
source_image: page_232.png
page_number: 232
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.73
tokens: 7618
characters: 1739
timestamp: 2025-12-24T02:46:20.404130
finish_reason: stop
---

Genre_Crime
Genre_Documentary
Genre_Drama
Genre_Fantasy
Genre_Film-Noir
Genre_Horror
Genre_Musical
Genre_Mystery
Genre_Romance
Genre_Sci-Fi
Genre_Thriller
Genre_War
Genre_Western
Name: 0, dtype: object

Для очень больших наборов данных такой способ построения индикаторных переменных для нескольких категорий быстрым не назовешь. Было бы лучше реализовать низкоуровневую функцию, которая пишет напрямую в массив NumPy, а затем обернуть результат объектом DataFrame.

В статистических приложениях бывает полезно сочетать функцию pandas.get_dummies с той или иной функцией дискретизации, например pandas.cut:

In [128]: np.random.seed(12345) # чтобы результат был повторяемым

In [129]: values = np.random.uniform(size=10)
In [130]: values
Out[130]:
array([0.9296, 0.3164, 0.1839, 0.2046, 0.5677, 0.5955, 0.9645, 0.6532,
       0.7489, 0.6536])

In [131]: bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

In [132]: pd.get_dummies(pd.cut(values, bins))
Out[132]:
   (0.0, 0.2]  (0.2, 0.4]  (0.4, 0.6]  (0.6, 0.8]  (0.8, 1.0]
0           0           0           0           0           1
1           0           1           0           0           0
2           1           0           0           0           0
3           0           1           0           0           0
4           0           0           1           0           0
5           0           0           1           0           0
6           0           0           0           0           1
7           0           0           0           1           0
8           0           0           0           1           0
9           0           0           0           1           0

Мы еще вернемся к функции pandas.get_dummies в разделе «Создание индикаторных функций для моделирования» ниже.