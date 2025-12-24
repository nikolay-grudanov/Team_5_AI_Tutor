---
source_image: page_443.png
page_number: 443
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.42
tokens: 7160
characters: 530
timestamp: 2025-12-24T02:52:07.688858
finish_reason: stop
---

Далее я нормирую эту таблицу на общее число родившихся, чтобы вычислить новую таблицу, содержащую долю от общего количества родившихся для каждого пола и каждой последней буквы:

Зная доли букв, я теперь могу нарисовать столбчатые диаграммы для каждого пола, разбив их по годам (см. рис. 13.8).

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop["M"].plot(kind="bar", rot=0, ax=axes[0], title="Male")
letter_prop["F"].plot(kind="bar", rot=0, ax=axes[1], title="Female",
    legend=False)