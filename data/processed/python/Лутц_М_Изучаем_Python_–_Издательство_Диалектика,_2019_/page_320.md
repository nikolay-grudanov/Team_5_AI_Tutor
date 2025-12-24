---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.55
tokens: 7699
characters: 2273
timestamp: 2025-12-24T01:17:14.054052
finish_reason: stop
---

близости JSON к словарям и спискам Python трансляция объектов Python в него и обратно тривиальна и автоматизируется стандартным библиотечным модулем json.

Скажем, словарь Python с вложенными структурами очень похож на данные JSON, хотя переменные и выражения Python поддерживают более богатые варианты структурирования (и часть показанного далее может быть произвольным выражением в коде Python):

```python
>>> name = dict(first='Bob', last='Smith')
>>> rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
>>> rec
{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
```

Отображаемый здесь финальный словарный формат является допустимым литералом в коде Python и передается для JSON почти в том виде, как есть, но модуль json делает трансляцию официальной — ниже демонстрируется трансляция объектов Python в сериализированное строковое представление JSON в памяти и обратно:

```python
>>> import json
>>> json.dumps(rec)
'{"job": ["dev", "mgr"], "name": {"last": "Smith", "first": "Bob"}, "age": 40.5}'
>>> S = json.dumps(rec)
>>> S
'{"job": ["dev", "mgr"], "name": {"last": "Smith", "first": "Bob"}, "age": 40.5}'
>>> O = json.loads(S)
>>> O
{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
>>> O == rec
True
```

Подобным же образом просто транслировать объекты Python в и из строк данных JSON в файлах. До сохранения в файле ваши данные существуют как объекты Python; модуль JSON воссоздает их из текстового представления JSON, когда загружает его из файла:

```python
>>> json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
>>> print(open('testjson.txt').read())
{
    "job": [
        "dev",
        "mgr"
    ],
    "name": {
        "last": "Smith",
        "first": "Bob"
    },
    "age": 40.5
}
>>> P = json.load(open('testjson.txt'))
>>> P
{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
```

После трансляции из текста JSON вы обрабатываете данные с использованием привычных операций над объектами Python в своем сценарии. Дополнительные сведения о JSON ищите в руководстве по библиотеке Python и в веб-сети.

Обратите внимание, что все строки в JSON представлены в Unicode, чтобы поддерживать текст с интернациональными таблицами символов, и потому после трансля-