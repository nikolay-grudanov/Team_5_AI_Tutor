---
source_image: page_453.png
page_number: 453
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.63
tokens: 7703
characters: 1974
timestamp: 2025-12-24T02:52:58.614458
finish_reason: stop
---

9 contb_receipt_amt 1001731 non-null float64
10 contb_receipt_dt 1001731 non-null object
11 receipt_desc 14166 non-null object
12 memo_cd 92482 non-null object
13 memo_text 97770 non-null object
14 form_tp 1001731 non-null object
15 file_num 1001731 non-null int64
dtypes: float64(1), int64(1), object(14)
memory usage: 122.3+ MB

Несколько человек просили меня заменить набор данных о выборах 2012 года набором, относящимся к 2016 или 2020 году. К сожалению, более поздние наборы данных, предоставляемые Федеральной избирательной комиссией, стали больше и сложнее, и я решил, что детали работы с ними будут только отвлекать от техники анализа, которую я хотел проиллюстрировать.

Ниже приведен пример записи в объекте DataFrame:

In [201]: fec.iloc[123456]
Out[201]:
cmte_id C00431445
cand_id P80003338
cand_nm Obama, Barack
contbr_nm ELLMAN, IRA
contbr_city TEMPE
contbr_st AZ
contbr_zip 852816719
contbr_employer ARIZONA STATE UNIVERSITY
contbr_occupation PROFESSOR
contb_receipt_amt 50.0
contb_receipt_dt 01-DEC-11
receipt_desc NaN
memo_cd NaN
memo_text NaN
form_tp SA17A
file_num 772372
Name: 123456, dtype: object

Наверное, вы сходу сможете придумать множество способов манипуляции этими данными для извлечения полезной статистики о спонсорах и закономерностях жертвования. Далее я покажу различные виды анализа, чтобы проиллюстрировать рассмотренные в книге технические приемы.
Как видите, данные не содержат сведений о принадлежности кандидата к политической партии, а эту информацию было бы полезно добавить. Получить список различных кандидатов можно с помощью функции unique:

In [202]: unique_cands = fec["cand_nm"].unique()

In [203]: unique_cands
Out[203]:
array(['Bachmann, Michelle', 'Romney, Mitt', 'Obama, Barack',
       'Roemer, Charles E. 'Buddy' III', 'Pawlenty, Timothy',
       'Johnson, Gary Earl', 'Paul, Ron', 'Santorum, Rick',
       'Cain, Herman', 'Gingrich, Newt', 'McCotter, Thaddeus G',
       'Huntsman, Jon', 'Perry, Rick'], dtype=object)