---
source_image: page_230.png
page_number: 230
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.44
tokens: 7455
characters: 1781
timestamp: 2025-12-24T03:06:55.729932
finish_reason: stop
---

```python
'environ_filter': {
    '()': EnvironFilter
},
'formatters': {
    'BASE_FORMAT': {
        'format':
            '[%(app_environment)s][%(name)s][%(levelname)-6s] %(message)s',
    }
},
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
        'level': 'INFO',
        'formatter': 'BASE_FORMAT',
        'filters': ['environ_filter'],
    }
},
'root': {
    'level': 'INFO',
    'handlers': ['console']
})
```

В этом примере есть много нюансов и можно легко упустить несколько модифицированных мест. Во-первых, был добавлен новый класс EnvironFilter, базовым для которого служит logging.Filter. В нем объявлен метод filter, принимающий в качестве аргумента record. Именно такого описания этого метода требует базовый класс. Аргумент record далее расширяется, включая переменную среды APP_ENVIRON, по умолчанию равную DEVEL.

Во-вторых, в dictConfig добавляется новый ключ (filters), в котором фильтр называется environ_filter, указывающий на класс EnvironFilter. Наконец, в ключе handlers мы добавляем ключ filters, принимающий список, в данном случае содержащий только один фильтр — environ_filter.

Описание и наименование фильтров выглядят неуклюже, но лишь потому, что наш пример тривиален. В более сложных случаях благодаря этому настройка и расширение не требуют заполнения ассоциативного массива шаблонным кодом, упрощая, таким образом, дальнейшую модификацию и расширение.

С помощью короткой проверки в командной строке можно посмотреть, как новый фильтр отражает среду. В этом примере используется простое приложение Pecan (https://www.pecanpy.org):

$ pecan serve config.py
Starting server in PID 25585
serving on 0.0.0.0:8080, view at http://127.0.0.1:8080
2019-08-12 07:57:28,157 [DEVEL][INFO      ] [pecan.commands.serve] GET / 200