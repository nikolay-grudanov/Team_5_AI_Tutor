---
source_image: page_069.png
page_number: 69
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.59
tokens: 8341
characters: 1184
timestamp: 2025-12-24T02:17:43.694725
finish_reason: stop
---

формате:

```html
{{ variable | filter_name(*args) }}
```

Если нет аргументов, определение становится следующим:

```html
{{ variable | filter_name }}
```

Давайте рассмотрим некоторые распространенные фильтры в следующих подразделах.

**Фильтр по умолчанию**
Переменная фильтра по умолчанию используется для замены вывода переданного значения, если оно оказывается None:

```html
{{ todo.item | default('This is a default todo item') }}
This is a default todo item
```

**Эвакуационный фильтр**
Этот фильтр используется для отображения необработанного вывода HTML:

```html
{{ "<title>Todo Application</title>" | escape }}
<title>Todo Application</title>
```

**Фильтры преобразования**
Эти фильтры включают фильтры int и float, используемые для преобразования из одного типа данных в другой:

```html
{{ 3.142 | int}}
3
{{ 31 | float }}
31.0
```

**Фильтр объединения**
Этот фильтр используется для объединения элементов списка в строку, как в Python:

```html
{{ ['Packt', 'produces', 'great', 'books!'] | join(' ') }}
Packt produces great books!
```

**Фильтр длины**
Этот фильтр используется для возврата длины переданного объекта. Он выполняет ту же роль, что и len() в Python: