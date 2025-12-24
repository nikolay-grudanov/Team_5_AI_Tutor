---
source_image: page_209.png
page_number: 209
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.14
tokens: 7552
characters: 1934
timestamp: 2025-12-24T02:45:35.771435
finish_reason: stop
---

HDF5 не является базой данных. Лучше всего она приспособлена для работы с наборами данных, которые записываются один раз, а читаются многократно. Данные можно добавлять в файл в любой момент, но если это делают одновременно несколько клиентов, то файл можно повредить.

6.3. Взаимодействие с HTML и Web API

Многие сайты предоставляют открытый API для получения данных в формате JSON или каком-то другом. Получить доступ к таким API из Python можно разными способами; я рекомендую простой пакет requests (http://docs.python-requests.org), который можно установить с помощью pip или conda:

conda install requests

Чтобы найти последние 30 заявок, касающихся pandas на GitHub, мы можем отправить с помощью библиотеки requests такой HTTP-запрос GET:

In [126]: import requests

In [127]: url = "https://api.github.com/repos/pandas-dev/pandas/issues"

In [128]: resp = requests.get(url)

In [129]: resp.raise_for_status()

In [130]: resp
Out[130]: <Response [200]>

Я рекомендую всегда вызывать метод raise_for_status после обращения к requests.get, чтобы проверить ошибки HTTP.

Метод json объекта Response возвращает объект Python, содержащий разобраные JSON-данные, представленные в виде словаря или списка (в зависимости от того, какой JSON-код был возвращен):

In [131]: data = resp.json()

In [132]: data[0]["title"]
Out[132]: 'REF: make copy keyword non-stateful'

Поскольку результаты зависят от данных, поступающих в режиме реального времени, при выполнении этого кода вы, скорее всего, увидите совершенно другую картину.

Каждый элемент в списке data — словарь, содержащий все данные на странице заявки в GitHub (кроме комментариев). Список data можно передать конструктору DataFrame и выделить интересующие нас поля:

In [133]: issues = pd.DataFrame(data, columns=["number", "title", "labels", "state"])

In [134]: issues
Out[134]:
   number    title    labels    state
0   48062  REF: make copy keyword non-stateful
1   48061