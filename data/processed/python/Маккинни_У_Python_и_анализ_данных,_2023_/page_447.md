---
source_image: page_447.png
page_number: 447
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.46
tokens: 7507
characters: 1641
timestamp: 2025-12-24T02:52:38.487740
finish_reason: stop
---

13.4. БАЗА ДАННЫХ О ПРОДУКТАХ ПИТАНИЯ МИНИСТЕРСТВА СЕЛЬСКОГО ХОЗЯЙСТВА США

Министерство сельского хозяйства США публикует данные о пищевой ценности продуктов питания. Программист Эшли Уильямс (Ashley Williams) преобразовал эту базу данных в формат JSON. Записи выглядят следующим образом:

{
    "id": 21441,
    "description": "KENTUCKY FRIED CHICKEN, Fried Chicken, EXTRA CRISPY, Wing, meat and skin with breading",
    "tags": ["KFC"],
    "manufacturer": "Kentucky Fried Chicken",
    "group": "Fast Foods",
    "portions": [
        {
            "amount": 1,
            "unit": "wing, with skin",
            "grams": 68.0
        },
        ...
    ],
    "nutrients": [
        {
            "value": 20.8,
            "units": "g",
            "description": "Protein",
            "group": "Composition"
        },
        ...
    ]
}

У каждого продукта питания есть ряд идентифицирующих атрибутов и два списка: питательные элементы и размеры порций. Для анализа данные в такой форме подходят плохо, поэтому необходимо их переформатировать.

Загрузить этот файл в Python-программу можно с помощью любой библиотеки для работы с JSON. Я воспользуюсь стандартным модулем Python json:

In [169]: import json

In [170]: db = json.load(open("datasets/usda_food/database.json"))

In [171]: len(db)
Out[171]: 6636

Каждая запись в db — словарь, содержащий все данные об одном продукте питания. Поле 'nutrients' — это список словарей, по одному для каждого питательного элемента:

In [172]: db[0].keys()
Out[172]: dict_keys(['id', 'description', 'tags', 'manufacturer', 'group', 'portions', 'nutrients'])

In [173]: db[0]["nutrients"][0]