---
source_image: page_225.png
page_number: 225
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.48
tokens: 7492
characters: 1643
timestamp: 2025-12-24T00:57:10.540877
finish_reason: stop
---

Эти методы get() и slice() также дают возможность обращаться к элементам возвращаемых методом split() массивов. Например, для извлечения фамилии из каждой записи можно использовать вместе методы split() и get():

In[14]: monte.str.split().str.get(-1)

Out[14]: 0    Chapman
         1    Cleese
         2    Gilliam
         3    Idle
         4    Jones
         5    Palin
      dtype: object

Индикаторные переменные. Еще один метод, требующий некоторых дополнительных пояснений, — get_dummies(). Удобно, когда в данных имеется столбец, содержащий кодированный индикатор. Например, у нас есть набор данных, содержащий информацию в виде кодов, таких как А="родился в США", В="родился в Великобритании", С="любит сыр", D="любит мясные консервы":

In[15]:
full_monte = pd.DataFrame({'name': monte,
                           'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C', 'B|C|D']})
full_monte

Out[15]:    info           name
0   B|C|D  Graham Chapman
1     B|D      John Cleese
2     A|C   Terry Gilliam
3     B|D        Eric Idle
4     B|C   Terry Jones
5   B|C|D  Michael Palin

Метод get_dummies() дает возможность быстро разбить все индикаторные переменные, преобразовав их в объект DataFrame:

In[16]: full_monte['info'].str.get_dummies('|')

Out[16]:   A  B  C  D
0  0  1  1  1
1  0  1  0  1
2  1  0  1  0
3  0  1  0  1
4  0  1  1  0
5  0  1  1  1

Используя эти операции как «строительные блоки», можно создать бесчисленное множество обрабатывающих строки процедур для очистки данных.

Мы не будем углубляться в эти методы, но я рекомендую прочитать раздел Working with Text Data («Работа с текстовыми данными») из онлайн-документации