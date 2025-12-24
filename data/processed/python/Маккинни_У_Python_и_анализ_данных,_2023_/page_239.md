---
source_image: page_239.png
page_number: 239
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.02
tokens: 7570
characters: 1859
timestamp: 2025-12-24T02:46:31.353304
finish_reason: stop
---

In [165]: import re

In [166]: text = "foo bar\t baz \tqux"

In [167]: re.split(r"\s+", text)
Out[167]: ['foo', 'bar', 'baz', 'qux']

При обращении re.split('\s+', text) сначала компилируется регулярное выражение, а затем его методу split передается заданный текст. Можно просто откомпилировать регулярное выражение методом re.compile, создав тем самым объект, допускающий повторное использование:

In [168]: regex = re.compile(r"\s+")

In [169]: regex.split(text)
Out[169]: ['foo', 'bar', 'baz', 'qux']

Чтобы получить список всех подстрок, отвечающих данному регулярному выражению, следует воспользоваться методом findall:

In [170]: regex.findall(text)
Out[170]: [' ', '\t ', '\t']

Чтобы не прибегать к громоздкому экранированию знаков \ в регулярном выражении, пользуйтесь простыми (raw) строковыми литералами, например r'C:\x' вместо 'C:\\x'.

Создавать объект регулярного выражения с помощью метода re.compile рекомендуется, если вы планируете применять одно и то же выражение к нескольким строкам, при этом экономится процессорное время.

С findall тесно связаны методы match и search. Если findall возвращает все найденные в строке соответствия, то search — только первое. А метод match находит только соответствие, начинающееся в начале строки. В качестве не столь три-виального примера рассмотрим блок текста и регулярное выражение, распознающее большинство адресов электронной почты:

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com"""
pattern = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}"
# Флаг re.IGNORECASE делает регулярное выражение нечувствительным к регистру
regex = re.compile(pattern, flags=re.IGNORECASE)

Применение метода findall к этому тексту порождает список почтовых адресов:

In [172]: regex.findall(text)
Out[172]:
['dave@google.com',
'steve@gmail.com',
'rob@gmail.com',
'ryan@yahoo.com']