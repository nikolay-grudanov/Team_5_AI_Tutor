---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.46
tokens: 8153
characters: 516
timestamp: 2025-12-24T02:20:31.010547
finish_reason: stop
---

Вот результат:

![Создан отчет о покрытии](../images/ch08/coverage_report.png)

Рисунок 8.15 – Создан отчет о покрытии

Далее давайте просмотрим отчет, сгенерированный командой coverage run -m pytest. Мы можем выбрать просмотр отчета на терминале или на веб-странице, создав отчет в формате HTML. Мы сделаем оба.

Давайте рассмотрим отчет с терминала:

(venv) $ coverage report

Вот результат:

![Отчет о покрытии с терминала](../images/ch08/coverage_report_terminal.png)

Рисунок 8.16 – Отчет о покрытии с терминала