---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.17
tokens: 7592
characters: 2132
timestamp: 2025-12-24T00:57:19.381084
finish_reason: stop
---

в каждом ли рецепте они содержатся в списке ингредиентов. Для упрощения ограничимся травами и специями:

In[28]: spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley',
    'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']

Мы можем создать булев объект DataFrame, состоящий из значений True и False, указывающих, содержится ли данный ингредиент в списке:

In[29]:
import re
spice_df = pd.DataFrame(
    dict((spice, recipes.ingredients.str.contains(spice, re.IGNORECASE))
        for spice in spice_list))

spice_df.head()

Out[29]:
    cumin oregano paprika parsley pepper rosemary sage salt tarragon thyme
0  False  False  False  False  False  False  True  False  False  False
1  False  False  False  False  False  False  False  False  False  False
2  True   False  False  False  True   False  False  True   False  False
3  False  False  False  False  False  False  False  False  False  False
4  False  False  False  False  False  False  False  False  False  False

Теперь в качестве примера допустим, что мы хотели бы найти рецепт, в котором используются петрушка (parsley), паприка (paprika) и эстрагон (tarragon). Это можно сделать очень быстро, воспользовавшись методом query() объекта DataFrame, который мы обсудим подробнее в разделе «Увеличение производительности библиотеки Pandas: eval() и query()» данной главы:

In[30]: selection = spice_df.query('parsley & paprika & tarragon')
len(selection)

Out[30]: 10

Мы нашли всего десять рецептов с таким сочетанием ингредиентов. Воспользуемся возвращаемым этой выборкой индексом, чтобы выяснить названия этих рецептов:

In[31]: recipes.name[selection.index]

Out[31]: 2069      All cremat with a Little Gem, dandelion and wa...
74964           Lobster with Thermidor butter
93768      Burton's Southern Fried Chicken with White Gravy
113926         Mijo's Slow Cooker Shredded Beef
137686     Asparagus Soup with Poached Eggs
140530         Fried Oyster Po'boys
158475  Lamb shank tagine with herb tabbouleh
158486  Southern fried chicken in buttermilk
163175  Fried Chicken Sliders with Pickles + Slaw
165243  Bar Tartine Cauliflower Salad
Name: name, dtype: object