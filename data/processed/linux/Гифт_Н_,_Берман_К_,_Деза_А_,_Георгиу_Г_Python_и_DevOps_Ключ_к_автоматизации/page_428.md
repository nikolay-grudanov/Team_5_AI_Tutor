---
source_image: page_428.png
page_number: 428
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.18
tokens: 7349
characters: 1547
timestamp: 2025-12-24T03:12:04.435832
finish_reason: stop
---

WORKDIR /bzt-configs
ENTRYPOINT ["sh", "-c", "bzt -l /tmp/artifacts/bzt.log /bzt-configs/taurus.yaml"]

В этом Dockerfile выполняется командная строка вызова утилиты bzt на основе файла конфигурации taurus.yaml:

$ cat taurus.yaml
execution:
- executor: molotov
  concurrency: 10  # Количество процессов-исполнителей Molotov
  iterations: 5   # Ограничение на количество итераций для теста
  ramp-up: 30s
  hold-for: 5m
  scenario:
    script: /scripts/loadtest.py  # Должен представлять собой
                                  # корректный сценарий Molotov

В этом файле конфигурации значение параметра concurrency задано равным 10, так что мы моделируем десять работающих конкурентно или виртуальных пользователей. executor задан как тест molotov на основе сценария loadtest.py в каталоге scripts. Вот этот сценарий, представляющий собой модуль Python:

$ cat scripts/loadtest.py
import os
import json
import random
import molotov
from molotov import global_setup, scenario

@global_setup()
def init_test(args):
    BASE_URL=os.getenv('BASE_URL', '')
    molotov.set_var('base_url', BASE_URL)

@scenario(weight=50)
async def _test_list_todos(session):
    base_url= molotov.get_var('base_url')
    async with session.get(base_url + '/todos') as resp:
        assert resp.status == 200, resp.status

@scenario(weight=30)
async def _test_create_todo(session):
    base_url= molotov.get_var('base_url')
    todo_data = json.dumps({'text':
        'Created new todo during Taurus/molotov load test'})
    async with session.post(base_url + '/todos',