---
source_image: page_460.png
page_number: 460
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.89
tokens: 7447
characters: 874
timestamp: 2025-12-24T02:52:48.795652
finish_reason: stop
---

Рис. 13.13. Процентная доля пожертвований каждого размера от общего их числа для обоих кандидатов

Статистика пожертвований по штатам
Начать можно с агрегирования данных по кандидатам и штатам:

In [235]: grouped = fec_mrbo.groupby(["cand_nm", "contbr_st"])

In [236]: totals = grouped["contb_receipt_amt"].sum().unstack(level=0).fillna(0)

In [237]: totals = totals[totals.sum(axis="columns") > 100000]

In [238]: totals.head(10)
Out[238]:
cand_nm Obama, Barack Romney, Mitt
contbr_st
AK 281840.15 86204.24
AL 543123.48 527303.51
AR 359247.28 105556.00
AZ 1506476.98 1888436.23
CA 23824984.24 11237636.60
CO 2132429.49 1506714.12
CT 2068291.26 3499475.45
DC 4373538.80 1025137.50
DE 336669.14 82712.00
FL 7318178.58 8338458.81

Поделив каждую строку на общую сумму пожертвований, мы получим для каждого кандидата процентную долю от общей суммы, приходящуюся на каждый штат: