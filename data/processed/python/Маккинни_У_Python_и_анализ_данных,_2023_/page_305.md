---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.29
tokens: 7131
characters: 467
timestamp: 2025-12-24T02:48:05.515504
finish_reason: stop
---

Рис. 9.16. Столбчатая диаграмма для DataFrame

Обратите внимание, что название столбцов DataFrame — «Genus» — используется в заголовке пояснительной надписи.
Для построения составной столбчатой диаграммы по объекту DataFrame нужно задать параметр stacked=True, тогда столбики, соответствующие значению в каждой строке, будут приставлены друг к другу (рис. 9.17):

In [75]: df.plot.barh(stacked=True, alpha=0.5)

Рис. 9.17. Составная столбчатая диаграмма для DataFrame