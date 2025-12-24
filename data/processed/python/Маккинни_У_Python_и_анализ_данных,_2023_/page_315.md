---
source_image: page_315.png
page_number: 315
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.08
tokens: 7137
characters: 467
timestamp: 2025-12-24T02:48:26.451109
finish_reason: stop
---

Рис. 9.27. Процент чаевых в зависимости от дня; фасетки по времени суток и курению

Функция catplot поддерживает и другие типы графиков, которые могут оказаться полезными в зависимости от того, что мы пытаемся показать. Например, диаграммы размаха (на которых изображаются медиана, квартили и выбросы) могут оказаться эффективным средством визуализации (рис. 9.28):

In [114]: sns.catplot(x="tip_pct", y="day", kind="box",
    ....:     data=tips[tips.tip_pct < 0.5])