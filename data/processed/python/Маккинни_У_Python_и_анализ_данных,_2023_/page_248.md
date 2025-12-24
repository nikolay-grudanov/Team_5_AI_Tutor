---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.66
tokens: 7489
characters: 1571
timestamp: 2025-12-24T02:46:47.641388
finish_reason: stop
---

Объект типа pandas.Categorical можно также создать непосредственно из других типов последовательностей Python:

In [222]: my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])

In [223]: my_categories
Out[223]:
['foo', 'bar', 'baz', 'foo', 'bar']
Categories (3, object): ['bar', 'baz', 'foo']

Если категориальные данные получены из другого источника, то можно воспользоваться альтернативным конструктором from_codes:

In [224]: categories = ['foo', 'bar', 'baz']

In [225]: codes = [0, 1, 2, 0, 0, 1]

In [226]: my_cats_2 = pd.Categorical.from_codes(codes, categories)

In [227]: my_cats_2
Out[227]:
['foo', 'bar', 'baz', 'foo', 'foo', 'bar']
Categories (3, object): ['foo', 'bar', 'baz']

Если явно не оговорено противное, при преобразовании данных в категориальную форму конкретный порядок категорий не предполагается. Поэтому порядок элементов в массиве categories может зависеть от того, как упорядочены входные данные. Но при использовании from_codes или любого другого конструктора можно указать, что порядок категорий имеет значение:

In [228]: ordered_cat = pd.Categorical.from_codes(codes, categories, ordered=True)

In [229]: ordered_cat
Out[229]:
['foo', 'bar', 'baz', 'foo', 'foo', 'bar']
Categories (3, object): ['foo' < 'bar' < 'baz']

Результат [foo < bar < baz] показывает, что 'foo' предшествует 'bar' и т. д. Неупорядоченный категориальный объект можно сделать упорядоченным с помощью метода as_ordered:

In [230]: my_cats_2.as_ordered()
Out[230]:
['foo', 'bar', 'baz', 'foo', 'foo', 'bar']
Categories (3, object): ['foo' < 'bar' < 'baz']