---
source_image: page_457.png
page_number: 457
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.53
tokens: 7471
characters: 1178
timestamp: 2025-12-24T02:52:45.850824
finish_reason: stop
---

Рис. 13.12. Общая сумма пожертвований по партиям для родов занятий с максимальной суммой пожертвований

Возможно, вам интересны профессии самых щедрых жертвователей или названия компаний, которые больше всех пожертвовали Обаме или Ромни. Для этого можно сгруппировать данные по имени кандидата, а потом воспользоваться вариантом метода top, рассмотренного выше в этой главе:

def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)["contb_receipt_amt"].sum()
    return totals.nlargest(n)

Затем агрегируем по роду занятий и месту работы:

In [222]: grouped = fec_mrbo.groupby("cand_nm")

In [223]: grouped.apply(get_top_amounts, "contbr_occupation", n=7)
Out[223]:
cand_nm      contbr_occupation
Obama, Barack
RETIRED        25305116.38
ATTORNEY       11141982.97
INFORMATION REQUESTED   4866973.96
HOMEMAKER      4248875.80
PHYSICIAN      3735124.94
LAWYER         3160478.87
CONSULTANT     2459912.71
Romney, Mitt
RETIRED        11508473.59
INFORMATION REQUESTED PER BEST EFFORTS
11396894.84
HOMEMAKER      8147446.22
ATTORNEY       5364718.82
PRESIDENT      2491244.89
EXECUTIVE      2300947.03
C.E.O.         1968386.11
Name: contb_receipt_amt, dtype: float64