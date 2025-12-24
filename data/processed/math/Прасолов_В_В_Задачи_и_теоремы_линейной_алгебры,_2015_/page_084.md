---
source_image: page_084.png
page_number: 84
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.39
tokens: 5834
characters: 849
timestamp: 2025-12-24T08:09:28.193696
finish_reason: stop
---

то же самое с диаграммой \( \lambda^{(1)} \), сопоставляя соответствующим клеткам число \( n - 1 \), и т. д. Ясно, что числа в каждой строке и в каждом столбце идут в неубывающем порядке. Покажем, что в одном столбце не может быть двух клеток с числами \( n \). Числа \( n \) в первой строке стоят в столбцах \( \mu_1 + 1, \ldots, \lambda_1 \); во второй — в столбцах \( \mu_2 + 1, \ldots, \lambda_2; \ldots \); в \( n \)-й — в столбцах \( 1, \ldots, \lambda_n \). Поэтому числа \( n \) стоят в столбцах \( 1, \ldots, \lambda_n; \mu_{n-1} + 1, \ldots, \lambda_{n-1}; \ldots; \mu_1 + 1, \ldots, \lambda_1 \). Остаётся заметить, что \( \lambda_n < \mu_{n-1} + 1, \ldots, \lambda_2 < \mu_1 + 1 \). Для чисел \( n - 1, \ldots, 1 \) доказательство аналогично. Ясно также, что эта конструкция даёт в точности все таблицы формы \( \lambda \). \( \square \)