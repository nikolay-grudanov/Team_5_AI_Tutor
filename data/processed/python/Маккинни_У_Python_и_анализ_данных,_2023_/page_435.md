---
source_image: page_435.png
page_number: 435
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.77
tokens: 7669
characters: 1651
timestamp: 2025-12-24T02:52:17.458067
finish_reason: stop
---

pieces = []
for year in range(1880, 2011):
    path = f"datasets/babynames/yob{year}.txt"
    frame = pd.read_csv(path, names=["name", "sex", "births"])

    # Добавить столбец для года
    frame["year"] = year
    pieces.append(frame)

# Собрать все данные в один объект DataFrame
names = pd.concat(pieces, ignore_index=True)

Обратим внимание на два момента. Во-первых, напомним, что concat по умолчанию объединяет объекты DataFrame построчно. Во-вторых, следует задать параметр ignore_index=True, потому что нам неинтересно сохранять исходные номера строк, прочитанных методом read_csv. Таким образом, мы получили очень большой DataFrame, содержащий данные обо всех именах за все годы.

In [111]: names
Out[111]:
      name  sex  births  year
0     Mary   F     7065  1880
1     Anna   F     2604  1880
2     Emma   F     2003  1880
3  Elizabeth   F     1939  1880
4    Minnie   F     1746  1880
...    ...   ..     ...   ...
1690779  Zymaire   M        5  2010
1690780  Zyonne   M        5  2010
1690781  Zyquarius   M        5  2010
1690782  Zyran   M        5  2010
1690783  Zzyzx   M        5  2010
[1690784 rows x 4 columns]

Имея эти данные, мы уже можем приступить к агрегированию на уровне года и пола, используя метод groupby или pivot_table (см. рис. 13.4):

In [112]: total_births = names.pivot_table("births", index="year",
    ....:                                 columns="sex", aggfunc=sum)

In [113]: total_births.tail()
Out[113]:
      F      M
year
2006  1896468  2050234
2007  1916888  2069242
2008  1883645  2032310
2009  1827643  1973359
2010  1759010  1898382

In [114]: total_births.plot(title="Total births by sex and year")