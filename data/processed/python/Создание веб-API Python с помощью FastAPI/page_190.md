---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.97
tokens: 8183
characters: 747
timestamp: 2025-12-24T02:20:45.290511
finish_reason: stop
---

Что такое .dockerignore?
Файл .dockerignore содержит файлы и папки, которые должны быть исключены из инструкций, определенных в файле Dockerfile.

Создание Docker образа
Чтобы создать образ приложения, выполните следующую команду в базовом каталоге:

(venv) $ docker build -t event-planner-api .

Эта команда просто указывает Docker создать образ с тегом event-planner-api из инструкций, определенных в текущем каталоге, который представлен точкой в конце команды. Процесс сборки начинается после запуска команды и выполнения инструкций:

![Пример процесса сборки Docker](../images/ch9_1.png)

Рисунок 9.1 – Процесс сборки Docker

Теперь, когда мы успешно создали образ нашего приложения, давайте вытащим образ MongoDB:

(venv) $ docker pull mongo