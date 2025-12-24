---
source_image: page_458.png
page_number: 458
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.12
tokens: 7887
characters: 2080
timestamp: 2025-12-24T02:53:06.767160
finish_reason: stop
---

13.5. База данных Федеральной избирательной комиссии

In [224]: grouped.apply(get_top_amounts, "contbr_employer", n=10)
Out[224]:
cand_nm contbr_employer
Obama, Barack    RETIRED                22694358.85
                 SELF-EMPLOYED          17080985.96
                 NOT EMPLOYED          8586308.70
                 INFORMATION REQUESTED  5053480.37
                 HOMEMAKER              2605408.54
                 SELF                   1076531.20
                 SELF EMPLOYED          469290.00
                 STUDENT                318831.45
                 VOLUNTEER               257104.00
                 MICROSOFT              215585.36
Romney, Mitt     INFORMATION REQUESTED PER BEST EFFORTS
                 12059527.24
                 RETIRED                11506225.71
                 HOMEMAKER              8147196.22
                 SELF-EMPLOYED          7409860.98
                 STUDENT                496490.94
                 CREDIT SUISSE          281150.00
                 MORGAN STANLEY         267266.00
                 GOLDMAN SACH & CO.     238250.00
                 BARCLAYS CAPITAL       162750.00
                 H.I.G. CAPITAL          139500.00
Name: contb_receipt_amt, dtype: float64

Распределение суммы пожертвований по интервалам

Полезный вид анализа данных — дискретизация сумм пожертвований с помощью функции cut:

In [225]: bins = np.array([0, 1, 10, 100, 1000, 10000,
.....:           100_000, 1_000_000, 10_000_000])
In [226]: labels = pd.cut(fec_mrbo["contb_receipt_amt"], bins)

In [227]: labels
Out[227]:
411 (10, 100]
412 (100, 1000]
413 (100, 1000]
414 (10, 100]
415 (10, 100]
...
701381 (10, 100]
701382 (100, 1000]
701383 (1, 10]
701384 (10, 100]
701385 (100, 1000]
Name: contb_receipt_amt, Length: 694282, dtype: category
Categories (8, interval[int64, right]): [(0, 1] < (1, 10] < (10, 100] < (100, 1000] < (1000, 10000] < (10000, 100000] < (100000, 1000000] < (1000000, 10000000]]

Затем можно сгруппировать данные для Обамы и Ромни по имени и метке интервала и построить гистограмму сумм пожертвований: