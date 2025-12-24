---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.80
tokens: 7559
characters: 1802
timestamp: 2025-12-24T00:56:12.733129
finish_reason: stop
---

0    Peter   fish
1    Paul   beans
2    Mary   bread

0    Mary   wine
1    Joseph   beer
2    Mary   bread   wine

Строки результата теперь соответствуют записям в левом из входных объектов. Опция how='right' работает аналогичным образом.

Все эти опции можно непосредственно применять ко всем вышеописанным типам соединений.

Пересекающиеся названия столбцов:
ключевое слово suffixes

Вам может встретиться случай, когда в двух входных объектах присутствуют конфликтующие названия столбцов. Рассмотрим следующий пример:

In[17]: df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                           'rank': [1, 2, 3, 4]})
       df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                           'rank': [3, 1, 4, 2]})
       print(df8); print(df9); print(pd.merge(df8, df9, on="name"))

df8
   name  rank
0   Bob     1
1  Jake     2
2  Lisa     3
3   Sue     4

df9
   name  rank
0   Bob     3
1  Jake     1
2  Lisa     4
3   Sue     2

pd.merge(df8, df9, on="name")
   name  rank_x  rank_y
0   Bob      1      3
1  Jake      2      1
2  Lisa      3      4
3   Sue      4      2

Поскольку в результате должны были быть два конфликтующих названия столбцов, функция слияния автоматически добавила в названия суффиксы _x и _y, чтобы обеспечить уникальность названий столбцов результата. Если подобное поведение, принятое по умолчанию, неуместно, можно задать пользовательские суффиксы с помощью ключевого слова suffixes:

In[18]:
print(df8); print(df9);
print(pd.merge(df8, df9, on="name", suffixes=["_L", "_R"]))

df8
   name  rank
0   Bob     1
1  Jake     2
2  Lisa     3
3   Sue     4

df9
   name  rank
0   Bob     3
1  Jake     1
2  Lisa     4
3   Sue     2

pd.merge(df8, df9, on="name", suffixes=["_L", "_R"])
   name  rank_L  rank_R
0   Bob      1      3