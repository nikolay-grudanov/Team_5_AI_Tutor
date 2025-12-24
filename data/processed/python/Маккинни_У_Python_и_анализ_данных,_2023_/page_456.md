---
source_image: page_456.png
page_number: 456
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.84
tokens: 7796
characters: 1734
timestamp: 2025-12-24T02:53:04.117852
finish_reason: stop
---

emp_mapping = {
    "INFORMATION REQUESTED PER BEST EFFORTS" : "NOT PROVIDED",
    "INFORMATION REQUESTED" : "NOT PROVIDED",
    "SELF" : "SELF-EMPLOYED",
    "SELF EMPLOYED" : "SELF-EMPLOYED",
}

def get_emp(x):
    # Если ничего не сопоставлено, вернуть x
    return emp_mapping.get(x, x)
fec["contbr_employer"] = fec["contbr_employer"].map(f)

Теперь можно воспользоваться функцией pivot_table для агрегирования данных по партиям и роду занятий, а затем отфильтровать роды занятий, на которые пришлось пожертвований на общую сумму не менее 2 млн долларов:

In [216]: by_occupation = fec.pivot_table("contb_receipt_amt",
    ....:
    ....:
    index="contbr_occupation",
    columns="party", aggfunc="sum")

In [217]: over_2mm = by_occupation[by_occupation.sum(axis="columns") > 2000000]

In [218]: over_2mm
Out[218]:
party           Democrat  Republican
contbr_occupation
ATTORNEY        11141982.97   7477194.43
CEO             2074974.79    4211040.52
CONSULTANT      2459912.71    2544725.45
ENGINEER        951525.55     1818373.70
EXECUTIVE       1355161.05    4138850.09
HOMEMAKER       4248875.80    13634275.78
INVESTOR        884133.00     2431768.92
LAWYER          3160478.87    391224.32
MANAGER         762883.22     1444532.37
NOT PROVIDED    4866973.96    20565473.01
OWNER           1001567.36    2408286.92
PHYSICIAN       3735124.94    3594320.24
PRESIDENT       1878509.95    4720923.76
PROFESSOR       2165071.08    296702.73
REAL ESTATE     528902.09     1625902.25
RETIRED         25305116.38   23561244.49
SELF-EMPLOYED  672393.40     1640252.54

Эти данные проще воспринять в виде графика (параметр 'barh' означает горизонтальную столбчатую диаграмму, см. рис. 13.12):

In [220]: over_2mm.plot(kind="barh")