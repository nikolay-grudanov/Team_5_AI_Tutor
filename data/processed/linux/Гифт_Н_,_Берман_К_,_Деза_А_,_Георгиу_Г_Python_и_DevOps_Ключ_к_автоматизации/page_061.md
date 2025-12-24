---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.21
tokens: 7399
characters: 1395
timestamp: 2025-12-24T03:02:32.319329
finish_reason: stop
---

Классы символов

Помимо наборов символов, в модуле re Python есть еще классы символов, представляющие собой уже готовые наборы символов. В числе наиболее распространенных — \w, эквивалентный [a-zA-Z0-9_], и \d, эквивалентный [0-9]. Для сопоставления с несколькими символами можно задействовать модификатор +:

>>> re.search(r'\w+', cc_list)
<re.Match object; span=(0, 4), match='Ezra'>

Так что можно заменить наш примитивный поисковый шаблон для адреса электронной почты на использующий \w:

>>> re.search(r'\w+@\w+\.\w+', cc_list)
<re.Match object; span=(13, 29), match='ekoenig@vpwk.com'>

Группы

С помощью скобок можно описывать группы в шаблоне для сопоставления, на которые можно ссылаться через объект шаблона. Они нумеруются в порядке вхождения в шаблон, причем нулевая группа соответствует шаблону в целом:

>>> re.search(r'(\w+)@(\w+)\.(\w+)', cc_list)
<re.Match object; span=(13, 29), match='ekoenig@vpwk.com'>
>>> matched = re.search(r'(\w+)@(\w+)\.(\w+)', cc_list)
>>> matched.group(0)
'ekoenig@vpwk.com'
>>> matched.group(1)
'ekoenig'
>>> matched.group(2)
'vpwk'
>>> matched.group(3)
'com'

Поименованные группы

Группам можно присваивать названия путем добавления ?P<Название> в их описания. В этом случае можно будет ссылаться на группы по названию вместо номера:

>>> matched = re.search(r'(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
>>> matched.group('name')
'ekoenig'