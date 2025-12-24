---
source_image: page_200.png
page_number: 200
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.05
tokens: 7651
characters: 1893
timestamp: 2025-12-24T02:45:25.892429
finish_reason: stop
---

```python
'siblings': [{'name': 'Scott',
    'age': 34,
    'hobbies': ['guitars', 'soccer']},
{'name': 'Katie', 'age': 42, 'hobbies': ['diving', 'art']}]}
```

Напротив, метод json.dumps преобразует объект Python в формат JSON:

In [71]: asjson = json.dumps(result)

In [72]: asjson
Out[72]: '{"name": "Wes", "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"], "pet": null, "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]}, {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]}'

Как именно преобразовывать объект JSON или список таких объектов в DataFrame или еще какую-то структуру данных для анализа, решать вам. Для удобства предлагается возможность передать список словарей (которые раньше были объектами JSON) конструктору DataFrame и выбрать подмножество полей данных:

In [73]: siblings = pd.DataFrame(result["siblings"], columns=["name", "age"])

In [74]: siblings
Out[74]:
   name  age
0  Scott   34
1  Katie   42

Функция pandas.read_json умеет автоматически преобразовать наборы данных определенного вида в формате JSON в объекты Series или DataFrame. Например:

In [75]: !cat examples/example.json
[{"a": 1, "b": 2, "c": 3},
 {"a": 4, "b": 5, "c": 6},
 {"a": 7, "b": 8, "c": 9}]

Подразумеваемые по умолчанию параметры pandas.read_json предполагают, что каждый объект в JSON-массиве — строка таблицы:

In [76]: data = pd.read_json("examples/example.json")

In [77]: data
Out[77]:
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9

Более полный пример чтения и манипулирования данными в формате JSON (включая и вложенные записи) приведен при рассмотрении базы данных о продуктах питания USDA в главе 13.

Чтобы экспортить данные из pandas в формате JSON, можно воспользоваться методами to_json объектов Series и DataFrame:

In [78]: data.to_json(sys.stdout)
{"a":{"0":1,"1":4,"2":7},"b":{"0":2,"1":5,"2":8},"c":{"0":3,"1":6,"2":9}}
```