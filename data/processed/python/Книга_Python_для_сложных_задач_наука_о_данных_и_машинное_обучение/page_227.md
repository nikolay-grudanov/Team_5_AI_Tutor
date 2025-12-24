---
source_image: page_227.png
page_number: 227
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.52
tokens: 7498
characters: 2053
timestamp: 2025-12-24T00:57:15.551442
finish_reason: stop
---

In[20]: # Читаем весь файл в массив Python
    with open('recipeitems-latest.json', 'r') as f:
        # Извлекаем каждую строку
        data = (line.strip() for line in f)
        # Преобразуем так, чтобы каждая строка была элементом списка
        data_json = "[{0}]".format(','.join(data))
    # Читаем результат в виде JSON
    recipes = pd.read_json(data_json)

In[21]: recipes.shape

Out[21]: (173278, 17)

Видим, что здесь почти 200 тысяч рецептов и 17 столбцов. Посмотрим на одну из строк, чтобы понять, что мы получили:

In[22]: recipes.iloc[0]

Out[22]:
_id                                 {'$oid': '5160756b96cc62079cc2db15'}
cookTime                           PT30M
creator                            NaN
dateModified                       NaN
datePublished                      2013-03-11
description                        Late Saturday afternoon, after Marlboro Man ha...
image                              http://static.thepioneerwoman.com/cooking/file...
ingredients                        Biscuits\n3 cups All-purpose Flour\n2 Tablespo...
name                               Drop Biscuits and Sausage Gravy
prepTime                           PT10M
recipeCategory                     NaN
recipeInstructions                 NaN
recipeYield                        12
source                             thepioneerwoman
totalTime                          NaN
ts                                 {'$date': 1365276011104}
url                                http://thepioneerwoman.com/cooking/2013/03/dro...
Name: 0, dtype: object

Здесь содержится немало информации, но большая ее часть находится в беспорядочном виде, как это обычно и бывает со взятыми из Интернета данными. В частности, список ингредиентов находится в строковом формате и нам придется аккуратно извлечь оттуда интересующую нас информацию. Начнем с того, что взглянем поближе на ингредиенты:

In[23]: recipes.ingredients.str.len().describe()

Out[23]: count    173278.000000
      mean     244.617926
      std      146.705285
      min      0.000000
      25%      147.000000