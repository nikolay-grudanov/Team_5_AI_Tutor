---
source_image: page_194.png
page_number: 194
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.24
tokens: 8137
characters: 480
timestamp: 2025-12-24T02:20:45.363400
finish_reason: stop
---

Эта команда запускает службы в автономном режиме:

![Запуск приложения с помощью инструмента docker-compose](../images/chapter9/fig9_3.png)

Рисунок 9.3 – Запускаем приложение с помощью инструмента docker-compose

Службы приложений созданы и развернуты. Давайте проверим, проверив список запущенных контейнеров:

(venv) $ docker ps

Результат выглядит следующим образом:

![Список запущенных контейнеров](../images/chapter9/fig9_4.png)

Рисунок 9.4 – Список запущенных контейнеров