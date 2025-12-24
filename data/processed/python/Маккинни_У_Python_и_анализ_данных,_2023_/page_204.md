---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.13
tokens: 7726
characters: 2412
timestamp: 2025-12-24T02:45:41.251713
finish_reason: stop
---

Функция pandas.read_xml позволяет заменить этот код односторочным выражением:

In [93]: perf2 = pd.read_xml(path)

In [94]: perf2.head()
Out[94]:
    INDICATOR_SEQ  PARENT_SEQ      AGENCY_NAME \
0           28445     NaN  Metro-North Railroad
1           28445     NaN  Metro-North Railroad
2           28445     NaN  Metro-North Railroad
3           28445     NaN  Metro-North Railroad
4           28445     NaN  Metro-North Railroad

INDICATOR_NAME \
0  On-Time Performance (West of Hudson)
1  On-Time Performance (West of Hudson)
2  On-Time Performance (West of Hudson)
3  On-Time Performance (West of Hudson)
4  On-Time Performance (West of Hudson)

DESCRIPTION \
0  Percent of commuter trains that arrive at their destinations within 5 m...
1  Percent of commuter trains that arrive at their destinations within 5 m...
2  Percent of commuter trains that arrive at their destinations within 5 m...
3  Percent of commuter trains that arrive at their destinations within 5 m...
4  Percent of commuter trains that arrive at their destinations within 5 m...

PERIOD_YEAR  PERIOD_MONTH      CATEGORY FREQUENCY DESIRED_CHANGE \
0           2008                1  Service Indicators   M   U
1           2008                2  Service Indicators   M   U
2           2008                3  Service Indicators   M   U
3           2008                4  Service Indicators   M   U
4           2008                5  Service Indicators   M   U

INDICATOR_UNIT  DECIMAL_PLACES YTD_TARGET YTD_ACTUAL MONTHLY_TARGET \
0              %                  1        95.00      96.90      95.00
1              %                  1        95.00      96.00      95.00
2              %                  1        95.00      96.30      95.00
3              %                  1        95.00      96.80      95.00
4              %                  1        95.00      96.60      95.00

MONTHLY_ACTUAL
0  96.90
1  95.00
2  96.90
3  98.30
4  95.80

Про обращение с более сложными XML-документами можно прочитать в строке документации функции pandas.read_xml, где описывается, как производить выборку и фильтрацию для извлечения конкретной таблицы.

6.2. ДВОИЧНЫЕ ФОРМАТЫ ДАННЫХ

Один из самых простых способов эффективного хранения данных в двоичном формате — воспользоваться встроенным в Python методом сериализации pickle() (NumPy). У всех объектов pandas имеется метод to_pickle, который сохраняет данные на диске в виде pickle-файла: