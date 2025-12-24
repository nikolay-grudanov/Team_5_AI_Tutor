---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.05
tokens: 11423
characters: 721
timestamp: 2025-12-24T06:16:53.533700
finish_reason: stop
---

Type of random forest: classification
Number of trees: 500
No. of variables tried at each split: 3

OOB estimate of error rate: 34.38%
Confusion matrix:
    paid off default class.error
paid off   15078   8058   0.3482884
default     7849  15287   0.3392548

Аргумент importance=TRUE запрашивает, чтобы randomForest сохранил дополнительную информацию о важности разных переменных. Функция varImpPlot построит график относительной результативности переменных:

varImpPlot(rf_all, type=1)
varImpPlot(rf_all, type=2)

Результат показан на рис. 6.8.

![Важность переменных для полной подгонки модели к данным о ссудах](../images/chapter6/fig6_8.png)

Рис. 6.8. Важность переменных для полной подгонки модели к данным о ссудах