---
source_image: page_455.png
page_number: 455
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.09
tokens: 7624
characters: 1845
timestamp: 2025-12-24T02:52:55.299077
finish_reason: stop
---

Чтобы упростить анализ, я ограничусь только положительными суммами пожертвований:

In [211]: fec = fec[fec["contb_receipt_amt"] > 0]

Поскольку главными кандидатами были Барак Обама и Митт Ромни, я подготовлю также подмножество, содержащее данные о пожертвованиях на их кампании:

In [212]: fec_mrbo = fec[fec["cand_nm"].isin(["Obama, Barack", "Romney, Mitt"])]


Статистика пожертвований по роду занятий и месту работы

Распределение пожертвований по роду занятий — тема, которой посвящено много исследований. Например, юристы обычно жертвуют в пользу демократов, а руководители предприятий — в пользу республиканцев. Вы вовсе не обязаны верить мне на слово, можете сами проанализировать данные. Для начала решим простую задачу — получим общую статистику пожертвований по роду занятий:

In [213]: fec["contbr_occupation"].value_counts()[10:]
Out[213]:
RETIRED 233990
INFORMATION REQUESTED 35107
ATTORNEY 34286
HOMEMAKER 29931
PHYSICIAN 23432
INFORMATION REQUESTED PER BEST EFFORTS 21138
ENGINEER 14334
TEACHER 13990
CONSULTANT 13273
PROFESSOR 12555
Name: contbr_occupation, dtype: int64

Видно, что часто различные занятия на самом деле относятся к одной и той же основной профессии, с небольшими вариациями. Ниже показан код, который позволяет произвести очистку, отобразив один род занятий на другой. Обратите внимание на «трюк» с методом dict.get, который позволяет «передавать насквозь» занятия, которым ничего не сопоставлено:

occ_mapping = {
    "INFORMATION REQUESTED PER BEST EFFORTS" : "NOT PROVIDED",
    "INFORMATION REQUESTED" : "NOT PROVIDED",
    "INFORMATION REQUESTED (BEST EFFORTS)" : "NOT PROVIDED",
    "C.E.O." : "CEO"
}

def get_occ(x):
    # Если ничего не сопоставлено, вернуть x
    return occ_mapping.get(x, x)

fec["contbr_occupation"] = fec["contbr_occupation"].map(get_occ)

То же самое я проделаю для места работы: