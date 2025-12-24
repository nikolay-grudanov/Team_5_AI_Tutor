---
source_image: page_202.png
page_number: 202
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.34
tokens: 7586
characters: 1672
timestamp: 2025-12-24T03:06:18.924062
finish_reason: stop
---

2019-05-29 22:45:02 default[2019] [2019-05-29 22:45:02 +0000] [8]
(8)
2019-05-29 22:45:02 default[2019] [2019-05-29 22:45:02 +0000] [8]
2019-05-29 22:45:02 default[2019] [2019-05-29 22:45:02 +0000] [25]
2019-05-29 22:45:02 default[2019] [2019-05-29 22:45:02 +0000] [27]
2019-05-29 22:45:04 default[2019] "GET /favicon.ico HTTP/1.1" 404
2019-05-29 22:46:25 default[2019] "GET /name/usf HTTP/1.1" 200

20. Добавьте новый маршрут и проверьте его:

@app.route('/html')
def html():
    """Возвращает пользовательский HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

21. Установите Pandas и верните результаты в формате JSON. На данном этапе имеет смысл создать Makefile и выполнить следующее:

touch Makefile
# Следующее необходимо поместить внутрь файла Makefile
install:
    pip install -r requirements.txt

Имеет смысл также настроить lint:

pylint --disable=R,C main.py
-----------------------------
Your code has been rated at 10.00/10

Синтаксис веб-маршрутов выглядит так, как показано в следующем блоке кода. Добавьте вверху импорт Pandas:

import pandas as pd

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/noahgift/sugar/\master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

При обращении к маршруту https://<вашеприложение>.appspot.com/pandas вы должны получить что-то наподобие изображенного на рис. 6.3.

22. Добавьте следующий маршрут «Википедии»:

import wikipedia
@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    return result