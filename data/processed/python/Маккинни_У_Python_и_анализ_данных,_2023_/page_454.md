---
source_image: page_454.png
page_number: 454
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.79
tokens: 7628
characters: 1706
timestamp: 2025-12-24T02:52:51.832323
finish_reason: stop
---

In [204]: unique_cands[2]
Out[204]: 'Obama, Barack'
Указать партийную принадлежность проще всего с помощью словаря11:
parties = {"Bachmann, Michelle": "Republican",
    "Cain, Herman": "Republican",
    "Gingrich, Newt": "Republican",
    "Huntsman, Jon": "Republican",
    "Johnson, Gary Earl": "Republican",
    "McCotter, Thaddeus G": "Republican",
    "Obama, Barack": "Democrat",
    "Paul, Ron": "Republican",
    "Pawlenty, Timothy": "Republican",
    "Perry, Rick": "Republican",
    "Roemer, Charles E. 'Buddy' III": "Republican",
    "Romney, Mitt": "Republican",
    "Santorum, Rick": "Republican"}

Далее, применяя этот словарь и метод map объектов Series, мы можем построить массив политических партий по именам кандидатов:

In [206]: fec["cand_nm"][123456:123461]
Out[206]:
123456 Obama, Barack
123457 Obama, Barack
123458 Obama, Barack
123459 Obama, Barack
123460 Obama, Barack
Name: cand_nm, dtype: object

In [207]: fec["cand_nm"][123456:123461].map(parties)
Out[207]:
123456 Democrat
123457 Democrat
123458 Democrat
123459 Democrat
123460 Democrat
Name: cand_nm, dtype: object

# Добавить в виде столбца
In [208]: fec["party"] = fec["cand_nm"].map(parties)

In [209]: fec["party"].value_counts()
Out[209]:
Democrat 593746
Republican 407985
Name: party, dtype: int64

Теперь два замечания касательно подготовки данных. Во-первых, данные включают как пожертвования, так и возвраты (пожертвования со знаком минус):

In [210]: (fec["contb_receipt_amt"] > 0).value_counts()
Out[210]:
True 991475
False 10256
Name: contb_receipt_amt, dtype: int64

11 Здесь сделано упрощающее предположение о том, что Гэри Джонсон – республиканец, хотя впоследствии он стал кандидатом от Либертарианской партии.