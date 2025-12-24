---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.95
tokens: 7772
characters: 2889
timestamp: 2025-12-24T02:45:43.017285
finish_reason: stop
---

Используя lxml.objectify, мы разбираем файл и получаем ссылку на корневой узел XML-документа от метода getroot:

In [86]: from lxml import objectify

In [87]: path = "datasets/mta_perf/Performance_MNR.xml"

In [88]: with open(path) as f:
    ....:     parsed = objectify.parse(f)

In [89]: root = parsed.getroot()

Свойство root.INDICATOR возвращает генератор, последовательно отдающий все элементы <INDICATOR>. Для каждой записи мы заполняем словарь имен тегов (например, YTD_ACTUAL) значениями данных (некоторые теги пропускаются):

data = []

skip_fields = ["PARENT_SEQ", "INDICATOR_SEQ",
               "DESIRED_CHANGE", "DECIMAL_PLACES"]
for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
Наконец, преобразуем этот список словарей в объект DataFrame:
In [91]: perf = pd.DataFrame(data)

In [92]: perf.head()
Out[92]:
      AGENCY_NAME                INDICATOR_NAME \
0  Metro-North Railroad On-Time Performance (West of Hudson)  Percent of commuter trains that arrive at their destinations within 5 m...
1  Metro-North Railroad On-Time Performance (West of Hudson)  Percent of commuter trains that arrive at their destinations within 5 m...
2  Metro-North Railroad On-Time Performance (West of Hudson)  Percent of commuter trains that arrive at their destinations within 5 m...
3  Metro-North Railroad On-Time Performance (West of Hudson)  Percent of commuter trains that arrive at their destinations within 5 m...
4  Metro-North Railroad On-Time Performance (West of Hudson)  Percent of commuter trains that arrive at their destinations within 5 m...

      DESCRIPTION \
0  Percent of commuter trains that arrive at their destinations within 5 m...
1  Percent of commuter trains that arrive at their destinations within 5 m...
2  Percent of commuter trains that arrive at their destinations within 5 m...
3  Percent of commuter trains that arrive at their destinations within 5 m...
4  Percent of commuter trains that arrive at their destinations within 5 m...

      PERIOD_YEAR  PERIOD_MONTH  CATEGORY  FREQUENCY  INDICATOR_UNIT \
0           2008              1  Service Indicators   M         %
1           2008              2  Service Indicators   M         %
2           2008              3  Service Indicators   M         %
3           2008              4  Service Indicators   M         %
4           2008              5  Service Indicators   M         %

      YTD_TARGET  YTD_ACTUAL  MONTHLY_TARGET  MONTHLY_ACTUAL
0          95.0       96.9             95.0             96.9
1          95.0       96.0             95.0             95.0
2          95.0       96.3             95.0             96.9
3          95.0       96.8             95.0             98.3
4          95.0       96.6             95.0             95.8