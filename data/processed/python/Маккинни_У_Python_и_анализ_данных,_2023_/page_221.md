---
source_image: page_221.png
page_number: 221
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.75
tokens: 7566
characters: 1591
timestamp: 2025-12-24T02:45:58.704101
finish_reason: stop
---

Преобразование данных с помощью функции или отображения

Часто бывает необходимо произвести преобразование набора данных, исходя из значений в некотором массиве, объекте Series или столбце объекта DataFrame. Рассмотрим гипотетические данные о сортах мяса:

In [57]: data = pd.DataFrame({"food": ["bacon", "pulled pork", "bacon",
    ....:                                 "pastrami", "corned beef", "bacon",
    ....:                                 "pastrami", "honey ham", "nova lox"],
    ....:     "ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

In [58]: data
Out[58]:
   food  ounces
0   bacon   4.0
1 pulled pork   3.0
2   bacon   12.0
3   pastrami   6.0
4 corned beef   7.5
5   bacon   8.0
6   pastrami   3.0
7 honey ham   5.0
8 nova lox   6.0

Допустим, что требуется добавить столбец, в котором указано соответствующее сорту мяса животное. Создадим отображение сортов мяса на виды животных:

meat_to_animal = {
    "bacon": "pig",
    "pulled pork": "pig",
    "pastrami": "cow",
    "corned beef": "cow",
    "honey ham": "pig",
    "nova lox": "salmon"
}

Метод map объекта Series (см. раздел «Применение функций и отображение» главы 5) принимает функцию или похожий на словарь объект, содержащий отображение, которое реализует преобразование значений:

In [60]: data["animal"] = data["food"].map(meat_to_animal)

In [61]: data
Out[61]:
      food  ounces  animal
0   bacon   4.0    pig
1 pulled pork   3.0    pig
2   bacon   12.0   pig
3   pastrami   6.0   cow
4 corned beef   7.5   cow
5   bacon   8.0    pig
6   pastrami   3.0   cow
7 honey ham   5.0    pig
8 nova lox   6.0  salmon