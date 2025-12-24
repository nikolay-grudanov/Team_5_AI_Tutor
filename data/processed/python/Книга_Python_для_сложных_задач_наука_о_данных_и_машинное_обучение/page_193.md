---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.94
tokens: 7577
characters: 2033
timestamp: 2025-12-24T00:56:18.725727
finish_reason: stop
---

1 Jake    2   1
2 Lisa    3   4
3 Sue     4   2

Эти суффиксы будут работать для всех возможных вариантов соединений, в том числе и в случае нескольких пересекающихся по названию столбцов.

За более подробной информацией об этих вариантах загляните в раздел «Агрегирование и группировка» данной главы, в котором мы подробнее изучим реляционную алгебру, а также в раздел Merge, Join and Concatenate («Слияние, соединение и конкатенация», http://pandas.pydata.org/pandas-docs/stable/merging.html) документации библиотеки Pandas.

Пример: данные по штатам США

Операции слияния и соединения чаще всего оказываются нужны при объединении данных из различных источников. Здесь мы рассмотрим пример с определенными данными по штатам США и их населению. Файлы данных можно найти по адресу http://github.com/jakevdp/data-USstates/:

In[19]:
# Инструкции системного командного процессора для скачивания данных:
# !curl -O https://raw.githubusercontent.com/jakevdp/
#     data-USstates/master/state-population.csv
# !curl -O https://raw.githubusercontent.com/jakevdp/
#     data-USstates/master/state-areas.csv
# !curl -O https://raw.githubusercontent.com/jakevdp/
#     data-USstates/master/state-abbrevs.csv

Посмотрим на эти наборы данных с помощью функции read_csv() библиотеки Pandas:

In[20]: pop = pd.read_csv('state-population.csv')
        areas = pd.read_csv('state-areas.csv')
        abbrevs = pd.read_csv('state-abbrevs.csv')

        print(pop.head()); print(areas.head()); print(abbrevs.head())

pop.head()
    state/region    ages    year    population
0      AL         under18  2012    1117489.0
1      AL         total    2012    4817528.0
2      AL         under18  2010    1130966.0
3      AL         total    2010    4785570.0
4      AL         under18  2011    1125763.0

areas.head()
    state    area (sq. mi)
0      Alabama    52423
1      Alaska     656425
2      Arizona    114006
3      Arkansas   53182
4      Arkansas   53182
4      California 163707

abbrevs.head()
    state    abbreviation
0      Alabama    AL