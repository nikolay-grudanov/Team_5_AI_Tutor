---
source_image: page_266.png
page_number: 266
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.05
tokens: 7321
characters: 1444
timestamp: 2025-12-24T03:07:51.139175
finish_reason: stop
---

Выполняем test_webserver.py еще раз и убеждаемся, что все наши предложения верны:

(validate) $ pytest -q --hosts='ssh://node4' test_webserver.py
....
4 passed in 3.29 seconds

Поняв идеи тестирования на Python и переориентировав их для проверки системы, можно добиться очень много. Автоматизация запуска тестов в ходе разработки приложений или даже написания и выполнения тестов для существующей инфраструктуры — два прекрасных способа упростить рутинные операции, которые могут вызвать ошибки. pytest и Testinfra — отличные проекты, начать использовать их очень просто, к тому же при необходимости они легко расширяются. Тестирование — способ по-настоящему прокачать свои навыки.

Тестирование блокнотов Jupyter с помощью pytest

Один из простейших способов создать для своей компании большие проблемы — забыть о рекомендуемых практиках проектирования ПО применительно к науке о данных и машинному обучению. Для исправления ситуации можно воспользоваться плагином nbval для pytest, с помощью которого тестировать блокноты Jupyter. Взгляните на следующий Makefile:

setup:
    python3 -m venv ~/.myrepo

install:
    pip install -r requirements.txt

test:
    python -m pytest -vv --cov=myrepolib tests/*.py
    python -m pytest --nbval notebook.ipynb

lint:
    pylint --disable=R,C myrepolib cli web

all: install lint test

Ключевой элемент здесь — флаг --nbval, благодаря которому сервер сборки может протестировать блокнот из репозитория.